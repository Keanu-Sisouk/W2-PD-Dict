#include <ttkMacros.h>
#include <ttkUtils.h>
#include <ttkWeightedBarycenter.h>
#include <vtkCellData.h>
#include <vtkDataArray.h>
#include <vtkDoubleArray.h>
#include <vtkFieldData.h>
#include <vtkFloatArray.h>
#include <vtkInformation.h>
#include <vtkIntArray.h>
#include <vtkMultiBlockDataSet.h>
#include <vtkNew.h>
#include <vtkPointData.h>
#include <vtkUnstructuredGrid.h>

#include <numeric>

using namespace ttk;

vtkStandardNewMacro(ttkWeightedBarycenter);

ttkWeightedBarycenter::ttkWeightedBarycenter() {
  SetNumberOfInputPorts(1);
  SetNumberOfOutputPorts(3);
}

int ttkWeightedBarycenter::FillInputPortInformation(int port,
                                                    vtkInformation *info) {
  if(port == 0) {
    info->Set(vtkDataObject::DATA_TYPE_NAME(), "vtkMultiBlockDataSet");
  } else {
    return 0;
  }
  return 1;
}

int ttkWeightedBarycenter::FillOutputPortInformation(int port,
                                                     vtkInformation *info) {
  if(port == 0 || port == 1 || port == 2) {
    info->Set(vtkDataObject::DATA_TYPE_NAME(), "vtkMultiBlockDataSet");
  } else {
    return 0;
  }
  return 1;
}

void ttkWeightedBarycenter::Modified() {
  needUpdate_ = true;
  ttkAlgorithm::Modified();
}

int ttkWeightedBarycenter::RequestData(vtkInformation * /*request*/,
                                       vtkInformationVector **inputVector,
                                       vtkInformationVector *outputVector) {

  Memory m;

  auto blocks = vtkMultiBlockDataSet::GetData(inputVector[0], 0);

  // Flat storage for diagrams extracted from blocks
  std::vector<vtkUnstructuredGrid *> input;

  // Number of input diagrams
  int numInputs = 0;

  if(blocks != nullptr) {
    numInputs = blocks->GetNumberOfBlocks();
    input.resize(numInputs);
    for(int i = 0; i < numInputs; ++i) {
      input[i] = vtkUnstructuredGrid::SafeDownCast(blocks->GetBlock(i));
      if(this->GetMTime() < input[i]->GetMTime()) {
        needUpdate_ = true;
      }
    }
  }

  // Get output pointers
  auto output_clusters = vtkMultiBlockDataSet::GetData(outputVector, 0);
  auto output_centroids = vtkMultiBlockDataSet::GetData(outputVector, 1);
  auto output_matchings = vtkMultiBlockDataSet::GetData(outputVector, 2);

  if(needUpdate_) {
    // clear data before computation
    intermediateDiagrams_ = {};
    all_matchings_ = {};
    final_centroids_ = {};

    intermediateDiagrams_.resize(numInputs);
    all_matchings_.resize(3);

    // store the persistence of every min-max global pair
    std::vector<double> max_persistences(numInputs);

    for(int i = 0; i < numInputs; i++) {
      VTUToDiagram(this->intermediateDiagrams_[i], input[i], *this);
      max_persistences[i] = intermediateDiagrams_[i][0].persistence();
    }

    this->max_dimension_total_
      = *std::max_element(max_persistences.begin(), max_persistences.end());

    if(this->Method == METHOD::PROGRESSIVE) {

      if(!UseInterruptible) {
        TimeLimit = 999999999;
      }

      inv_clustering_.resize(numInputs);
      for(int i_input = 0; i_input < numInputs; i_input++) {
        inv_clustering_[i_input] = 0;
      }

      std::vector<double> weights{};

      // Read weights from data string
      // If the weights are not correct (the number does not match the number of
      // inputs, or they do not sum to 1), the function
      // computeWeighterBarycenter defaults to compute with uniform weights
      if(!DataString.empty()) {
        std::string weights_string = DataString;
        std::replace(weights_string.begin(), weights_string.end(), ',', ' ');

        std::stringstream ss(weights_string);
        std::istream_iterator<std::string> begin(ss);
        std::istream_iterator<std::string> end;
        std::vector<std::string> vstrings(begin, end);

        weights.resize(vstrings.size());

        for(size_t iweight = 0; iweight < vstrings.size(); iweight++) {
          double w = std::stod(vstrings[iweight]);
          weights[iweight] = w;
        }
      }

      ttk::DiagramType barycenter;
      std::vector<std::vector<ttk::MatchingType>> matchings;

      computeWeightedBarycenter(
        intermediateDiagrams_, weights, barycenter, matchings, *this, true);

      std::cout << "PRINT MATCHINGS" << std::endl;
      for(size_t ii = 0; ii < matchings.size(); ii++) {
        std::cout << " j = " << ii << std::endl;
        for(size_t jj = 0; jj < matchings[ii].size(); jj++) {
          std::cout << "    " << std::get<0>(matchings[ii][jj]) << " "
                    << std::get<1>(matchings[ii][jj]) << " "
                    << std::get<2>(matchings[ii][jj]) << std::endl;
        }
      }
      final_centroids_.resize(1);
      final_centroids_[0] = std::move(barycenter);
      all_matchings_[0] = std::move(matchings);
      needUpdate_ = false;

    } else if(this->Method == METHOD::AUCTION) {

      final_centroids_.resize(1);
      inv_clustering_.resize(numInputs);
      for(int i_input = 0; i_input < numInputs; i_input++) {
        inv_clustering_[i_input] = 0;
      }
      PersistenceDiagramBarycenter pdBarycenter;

      const auto wassersteinMetric = std::to_string(WassersteinMetric);
      pdBarycenter.setWasserstein(wassersteinMetric);
      pdBarycenter.setMethod(2);
      pdBarycenter.setNumberOfInputs(numInputs);
      pdBarycenter.setDeterministic(Deterministic);
      pdBarycenter.setUseProgressive(UseProgressive);
      pdBarycenter.setDebugLevel(debugLevel_);
      pdBarycenter.setThreadNumber(threadNumber_);
      pdBarycenter.setAlpha(Alpha);
      pdBarycenter.setLambda(Lambda);
      pdBarycenter.execute(
        intermediateDiagrams_, final_centroids_[0], all_matchings_);

      needUpdate_ = false;
    }
  }

  outputClusteredDiagrams(output_clusters, input, this->inv_clustering_,
                          this->DisplayMethod, this->Spacing,
                          this->max_dimension_total_);
  outputCentroids(output_centroids, this->final_centroids_, this->DisplayMethod,
                  this->Spacing, this->max_dimension_total_);
  outputMatchings(
    output_matchings, this->NumberOfClusters, this->intermediateDiagrams_,
    this->all_matchings_, this->final_centroids_, this->inv_clustering_,
    this->DisplayMethod, this->Spacing, this->max_dimension_total_);

  // forward input diagrams FieldData to output_clusters blocks
  for(size_t i = 0; i < input.size(); ++i) {
    const auto diag{input[i]};
    const auto block{
      vtkUnstructuredGrid::SafeDownCast(output_clusters->GetBlock(i))};
    if(block != nullptr && block->GetFieldData() != nullptr
       && diag->GetFieldData() != nullptr) {
      block->GetFieldData()->ShallowCopy(diag->GetFieldData());
      // add clusterId to FieldData
      vtkNew<vtkIntArray> cid{};
      cid->SetName("ClusterId");
      cid->SetNumberOfTuples(1);
      cid->SetTuple1(0, this->inv_clustering_[i]);
      block->GetFieldData()->AddArray(cid);
    }
  }

  // add distance results to output_matchings FieldData
  vtkNew<vtkDoubleArray> minSad{};
  minSad->SetName("MinSaddleCost");
  minSad->SetNumberOfTuples(1);
  minSad->SetTuple1(0, this->distances[0]);

  vtkNew<vtkDoubleArray> sadSad{};
  sadSad->SetName("SaddleSaddleCost");
  sadSad->SetNumberOfTuples(1);
  sadSad->SetTuple1(0, this->distances[1]);

  vtkNew<vtkDoubleArray> sadMax{};
  sadMax->SetName("SaddleMaxCost");
  sadMax->SetNumberOfTuples(1);
  sadMax->SetTuple1(0, this->distances[2]);

  vtkNew<vtkDoubleArray> wass{};
  wass->SetName("WassersteinDistance");
  wass->SetNumberOfTuples(1);
  wass->SetTuple1(
    0, std::accumulate(this->distances.begin(), this->distances.end(), 0.0));

  for(size_t i = 0; i < output_matchings->GetNumberOfBlocks(); ++i) {
    const auto block{
      vtkUnstructuredGrid::SafeDownCast(output_matchings->GetBlock(i))};
    if(block != nullptr && block->GetFieldData() != nullptr) {
      block->GetFieldData()->AddArray(minSad);
      block->GetFieldData()->AddArray(sadSad);
      block->GetFieldData()->AddArray(sadMax);
      block->GetFieldData()->AddArray(wass);
    }
  }

  return 1;
}

void ttkWeightedBarycenter::outputClusteredDiagrams(
  vtkMultiBlockDataSet *output,
  const std::vector<vtkUnstructuredGrid *> &diags,
  const std::vector<int> &inv_clustering,
  const DISPLAY dm,
  const double spacing,
  const double max_persistence) const {

  // index of diagram in its cluster
  std::vector<int> diagIdInClust{};
  // number of diagrams per cluster
  std::vector<int> clustSize{};

  // prep work for displaying diagrams as cluster stars
  if(dm == DISPLAY::STARS) {
    // total number of clusters
    const auto nClusters
      = 1 + *std::max_element(inv_clustering.begin(), inv_clustering.end());
    clustSize.resize(nClusters, 0);
    diagIdInClust.resize(diags.size());
    for(size_t i = 0; i < inv_clustering.size(); ++i) {
      auto &diagsInClust = clustSize[inv_clustering[i]];
      diagIdInClust[i] = diagsInClust;
      diagsInClust++;
    }
  }

  output->SetNumberOfBlocks(diags.size());

  for(size_t i = 0; i < diags.size(); ++i) {
    vtkNew<vtkUnstructuredGrid> vtu{};
    vtu->ShallowCopy(diags[i]);

    vtkNew<vtkIntArray> diagId{};
    diagId->SetName("DiagramID");
    diagId->SetNumberOfTuples(vtu->GetNumberOfPoints());
    diagId->Fill(i);
    vtu->GetPointData()->AddArray(diagId);

    vtkNew<vtkIntArray> clusterId{};
    clusterId->SetName("ClusterID");
    clusterId->SetNumberOfComponents(1);
    clusterId->SetNumberOfTuples(vtu->GetNumberOfPoints());
    clusterId->Fill(inv_clustering[i]);
    vtu->GetPointData()->AddArray(clusterId);

    // add Persistence data array on vertices
    vtkNew<vtkDoubleArray> pointPers{};
    pointPers->SetName("Persistence");
    pointPers->SetNumberOfTuples(vtu->GetNumberOfPoints());
    vtu->GetPointData()->AddArray(pointPers);

    // diagonal uses two existing points
    for(int j = 0; j < vtu->GetNumberOfCells() - 1; ++j) {
      const auto persArray = vtu->GetCellData()->GetArray("Persistence");
      const auto pers = persArray->GetTuple1(j);
      pointPers->SetTuple1(2 * j + 0, pers);
      pointPers->SetTuple1(2 * j + 1, pers);
    }

    if(dm == DISPLAY::MATCHINGS && spacing > 0) {
      // translate diagrams along the Z axis
      TranslateDiagram(
        vtu, std::array<double, 3>{0, 0, i == 0 ? -spacing : spacing});
      output->SetBlock(i, vtu);
    } else if(dm == DISPLAY::STARS && spacing > 0) {
      const auto c = inv_clustering[i];
      const auto angle = 2.0 * M_PI * static_cast<double>(diagIdInClust[i])
                         / static_cast<double>(clustSize[c]);
      // translate diagrams in the XY plane
      TranslateDiagram(
        vtu, std::array<double, 3>{
               3.0 * (spacing + 0.2) * max_persistence * c
                 + spacing * max_persistence * std::cos(angle) + 0.2,
               spacing * max_persistence * std::sin(angle), 0});
    }
    // add diagram to output multi-block dataset
    output->SetBlock(i, vtu);
  }
}

void ttkWeightedBarycenter::outputCentroids(
  vtkMultiBlockDataSet *output,
  const std::vector<ttk::DiagramType> &final_centroids,
  const DISPLAY dm,
  const double spacing,
  const double max_persistence) const {

  vtkNew<vtkDoubleArray> dummy{};

  for(size_t i = 0; i < final_centroids.size(); ++i) {
    vtkNew<vtkUnstructuredGrid> vtu{};
    DiagramToVTU(vtu, final_centroids[i], dummy, *this, 3, false);

    if(dm == DISPLAY::STARS && spacing > 0) {
      // shift centroid along the X axis
      TranslateDiagram(
        vtu, std::array<double, 3>{
               3.0 * (spacing + 0.2) * max_persistence * i, 0, 0});
    }
    // add centroid to output multi-block dataset
    output->SetBlock(i, vtu);
  }
}

void ttkWeightedBarycenter::outputMatchings(
  vtkMultiBlockDataSet *output,
  const size_t nClusters,
  const std::vector<ttk::DiagramType> &diags,
  const std::vector<std::vector<std::vector<ttk::MatchingType>>>
    &matchingsPerCluster,
  const std::vector<ttk::DiagramType> &centroids,
  const std::vector<int> &inv_clustering,
  const DISPLAY dm,
  const double spacing,
  const double max_persistence) const {

  // index of diagram in its cluster
  std::vector<int> diagIdInClust{};
  // number of diagrams per cluster
  std::vector<int> clustSize{};

  // prep work for displaying diagrams as cluster stars
  if(dm == DISPLAY::STARS) {
    clustSize.resize(nClusters, 0);
    diagIdInClust.resize(diags.size());
    for(size_t i = 0; i < inv_clustering.size(); ++i) {
      auto &diagsInClust = clustSize[inv_clustering[i]];
      diagIdInClust[i] = diagsInClust;
      diagsInClust++;
    }
  }

  // count the number of bidders per centroid pair
  // (when with only 1 cluster and 2 diagrams)
  std::vector<int> matchings_count(centroids[0].size());
  std::vector<int> count_to_good{};

  for(size_t i = 0; i < diags.size(); ++i) {
    const auto cid = inv_clustering[i];
    const auto &diag{diags[i]};
    const auto &matchings{matchingsPerCluster[cid][i]};

    vtkNew<vtkUnstructuredGrid> matchingsGrid{};

    const auto nCells{matchings.size()};
    const auto nPoints{2 * matchings.size()};

    vtkNew<vtkPoints> points{};
    points->SetNumberOfPoints(nPoints);
    matchingsGrid->SetPoints(points);

    // point data
    vtkNew<vtkIntArray> diagIdVerts{};
    diagIdVerts->SetName("DiagramID");
    diagIdVerts->SetNumberOfTuples(nPoints);
    matchingsGrid->GetPointData()->AddArray(diagIdVerts);

    vtkNew<vtkIntArray> pointId{};
    pointId->SetName("PointID");
    pointId->SetNumberOfTuples(nPoints);
    matchingsGrid->GetPointData()->AddArray(pointId);

    // cell data
    vtkNew<vtkIntArray> diagIdCells{};
    diagIdCells->SetName("DiagramID");
    diagIdCells->SetNumberOfTuples(nCells);
    matchingsGrid->GetCellData()->AddArray(diagIdCells);

    vtkNew<vtkIntArray> clusterId{};
    clusterId->SetName("ClusterID");
    clusterId->SetNumberOfTuples(nCells);
    clusterId->Fill(cid);
    matchingsGrid->GetCellData()->AddArray(clusterId);

    vtkNew<vtkDoubleArray> matchCost{};
    matchCost->SetName("Cost");
    matchCost->SetNumberOfTuples(nCells);
    matchingsGrid->GetCellData()->AddArray(matchCost);

    vtkNew<vtkIntArray> pairType{};
    pairType->SetName("PairType");
    pairType->SetNumberOfTuples(nCells);
    matchingsGrid->GetCellData()->AddArray(pairType);

    vtkNew<vtkIntArray> isDiagonal{};
    isDiagonal->SetName("IsDiagonal");
    isDiagonal->SetNumberOfTuples(nCells);
    matchingsGrid->GetCellData()->AddArray(isDiagonal);

    for(size_t j = 0; j < matchings.size(); ++j) {
      const auto &m{matchings[j]};
      const auto bidderId{std::get<0>(m)};
      const auto goodId{std::get<1>(m)};

      // avoid out-of-bound accesses
      if(goodId >= static_cast<ttk::SimplexId>(centroids[cid].size())
         || bidderId >= static_cast<ttk::SimplexId>(diag.size())) {
        this->printWrn("Out-of-bounds access averted");
        continue;
      }

      if(nClusters == 1 and bidderId >= 0) {
        matchings_count[goodId] += 1;
        count_to_good.push_back(goodId);
      }

      const auto &p0{centroids[cid][goodId]};
      std::array<double, 3> coords0{p0.birth.sfValue, p0.death.sfValue, 0};

      std::array<double, 3> coords1{};

      if(bidderId >= 0) {
        const auto &p1{diag[bidderId]};
        coords1[0] = p1.birth.sfValue;
        coords1[1] = p1.death.sfValue;
        coords1[2] = 0;
        isDiagonal->SetTuple1(j, 0);
      } else {
        double diagonal_projection = (p0.birth.sfValue + p0.death.sfValue) / 2;
        coords1[0] = diagonal_projection;
        coords1[1] = diagonal_projection;
        coords1[2] = 0;
        isDiagonal->SetTuple1(j, 1);
      }

      if(dm == DISPLAY::STARS && spacing > 0) {
        const auto angle = 2.0 * M_PI * static_cast<double>(diagIdInClust[i])
                           / static_cast<double>(clustSize[cid]);
        const auto shift
          = 3.0 * (std::abs(spacing) + 0.2) * max_persistence * cid;
        coords0[0] += shift;
        coords1[0] += shift + spacing * max_persistence * std::cos(angle);
        coords1[1] += spacing * max_persistence * std::sin(angle);

      } else if(dm == DISPLAY::MATCHINGS) {
        coords1[2] = (diags.size() == 2 && i == 0) ? -spacing : spacing;
      }

      points->SetPoint(2 * j + 0, coords0.data());
      points->SetPoint(2 * j + 1, coords1.data());
      std::array<vtkIdType, 2> ids{
        2 * static_cast<vtkIdType>(j) + 0,
        2 * static_cast<vtkIdType>(j) + 1,
      };
      matchingsGrid->InsertNextCell(VTK_LINE, 2, ids.data());

      diagIdCells->SetTuple1(j, i);
      matchCost->SetTuple1(j, std::get<2>(m));
      diagIdVerts->SetTuple1(2 * j + 0, i);
      diagIdVerts->SetTuple1(2 * j + 1, i);
      pointId->SetTuple1(2 * j + 0, goodId);
      pointId->SetTuple1(2 * j + 1, bidderId);
      pairType->SetTuple1(j, p0.dim);
    }

    output->SetBlock(i, matchingsGrid);
  }

  // add matchings number
  if(nClusters == 1 && diags.size() == 2) {
    size_t nPrevCells{};
    for(size_t i = 0; i < diags.size(); ++i) {
      vtkNew<vtkIntArray> matchNumber{};
      matchNumber->SetName("MatchNumber");
      const auto matchings
        = vtkUnstructuredGrid::SafeDownCast(output->GetBlock(i));
      const auto nCells = matchings->GetNumberOfCells();
      matchNumber->SetNumberOfTuples(nCells);
      for(int j = 0; j < nCells; j++) {
        const auto goodId = count_to_good[j + (i == 0 ? 0 : nPrevCells)];
        matchNumber->SetTuple1(j, matchings_count[goodId]);
      }
      matchings->GetCellData()->AddArray(matchNumber);
      nPrevCells = nCells;
    }
  }
}
