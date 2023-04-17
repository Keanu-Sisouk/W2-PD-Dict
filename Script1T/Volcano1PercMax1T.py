# state file generated using paraview version 5.9.1-5-g35227227

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 9

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
volcano_2011_164_pmvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_164_pm.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_164_pm.vtu'])
volcano_2011_164_pmvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_164_pmvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_164_pmvtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
volcano_2011_157_amvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_157_am.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_157_am.vtu'])
volcano_2011_157_amvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_157_amvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_157_amvtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
volcano_2011_151_amvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_151_am.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_151_am.vtu'])
volcano_2011_151_amvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_151_amvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_151_amvtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
volcano_2011_165_amvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_165_am.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_165_am.vtu'])
volcano_2011_165_amvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_165_amvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_165_amvtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
volcano_2011_156_pmvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_156_pm.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_156_pm.vtu'])
volcano_2011_156_pmvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_156_pmvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_156_pmvtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
volcano_2011_157_pmvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_157_pm.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_157_pm.vtu'])
volcano_2011_157_pmvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_157_pmvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_157_pmvtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
volcano_2011_165_pmvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_165_pm.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_165_pm.vtu'])
volcano_2011_165_pmvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_165_pmvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_165_pmvtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram2', Input=volcano_2011_151_amvtu)
tTKPersistenceDiagram2.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram2.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram2.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram2.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
volcano_2011_151_pmvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_151_pm.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_151_pm.vtu'])
volcano_2011_151_pmvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_151_pmvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_151_pmvtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram6 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram6', Input=volcano_2011_165_amvtu)
tTKPersistenceDiagram6.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram6.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram6.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram6.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram12 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram12', Input=volcano_2011_165_pmvtu)
tTKPersistenceDiagram12.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram12.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram12.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram12.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram10 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram10', Input=volcano_2011_157_pmvtu)
tTKPersistenceDiagram10.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram10.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram10.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram10.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
volcano_2011_150_amvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_150_am.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_150_am.vtu'])
volcano_2011_150_amvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_150_amvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_150_amvtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=volcano_2011_150_amvtu)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram1.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram1.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
volcano_2011_156_amvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_156_am.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_156_am.vtu'])
volcano_2011_156_amvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_156_amvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_156_amvtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram3', Input=volcano_2011_156_amvtu)
tTKPersistenceDiagram3.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram3.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram3.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram3.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram8 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram8', Input=volcano_2011_151_pmvtu)
tTKPersistenceDiagram8.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram8.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram8.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram8.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram11 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram11', Input=volcano_2011_164_pmvtu)
tTKPersistenceDiagram11.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram11.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram11.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram11.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
volcano_2011_150_pmvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_150_pm.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_150_pm.vtu'])
volcano_2011_150_pmvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_150_pmvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_150_pmvtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram7 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram7', Input=volcano_2011_150_pmvtu)
tTKPersistenceDiagram7.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram7.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram7.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram7.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram9 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram9', Input=volcano_2011_156_pmvtu)
tTKPersistenceDiagram9.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram9.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram9.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram9.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
volcano_2011_164_amvtu = XMLUnstructuredGridReader(registrationName='volcano_2011_164_am.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2014_volcanic_eruptions_2D/volcano_2011_164_am.vtu'])
volcano_2011_164_amvtu.CellArrayStatus = ['vtkGhostType']
volcano_2011_164_amvtu.PointArrayStatus = ['SO2', 'ash', 'time', 'vtkValidPointMask', 'vtkGhostType', 'ttkOffsetScalarField']
volcano_2011_164_amvtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram5', Input=volcano_2011_164_amvtu)
tTKPersistenceDiagram5.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram5.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram5.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram5.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram4', Input=volcano_2011_157_amvtu)
tTKPersistenceDiagram4.ScalarField = ['POINTS', 'SO2']
tTKPersistenceDiagram4.InputOffsetField = ['POINTS', 'SO2']
tTKPersistenceDiagram4.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram4.Saddlesaddlediagramdimension1slowest = 0

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[tTKPersistenceDiagram1, tTKPersistenceDiagram2, tTKPersistenceDiagram3, tTKPersistenceDiagram4, tTKPersistenceDiagram5, tTKPersistenceDiagram6, tTKPersistenceDiagram7, tTKPersistenceDiagram8, tTKPersistenceDiagram9, tTKPersistenceDiagram10, tTKPersistenceDiagram11, tTKPersistenceDiagram12])

threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [3.0 , 3.0]
threshold1.LowerThreshold = 3.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0.25
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 10.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.MaxEpoch = 1000
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1

# ----------------------------------------------------------------
# restore active source

SaveData('TimersVolcano1PercProgMaxTest1T.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 5))
