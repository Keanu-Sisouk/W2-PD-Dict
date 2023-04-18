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
ionization2DDgm8vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm8.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm8.vtu'])
ionization2DDgm8vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm8vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm5vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm5.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm5.vtu'])
ionization2DDgm5vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm5vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm9vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm9.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm9.vtu'])
ionization2DDgm9vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm9vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm11vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm11.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm11.vtu'])
ionization2DDgm11vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm11vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm1vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm1.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm1.vtu'])
ionization2DDgm1vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm1vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm2vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm2.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm2.vtu'])
ionization2DDgm2vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm2vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm13vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm13.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm13.vtu'])
ionization2DDgm13vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm13vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm13vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm14vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm14.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm14.vtu'])
ionization2DDgm14vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm14vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm14vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm12vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm12.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm12.vtu'])
ionization2DDgm12vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm12vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm12vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm10vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm10.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm10.vtu'])
ionization2DDgm10vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm10vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm7vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm7.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm7.vtu'])
ionization2DDgm7vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm7vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm4vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm4.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm4.vtu'])
ionization2DDgm4vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm4vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm3vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm3.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm3.vtu'])
ionization2DDgm3vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm3vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm15vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm15.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm15.vtu'])
ionization2DDgm15vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm15vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm15vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm0vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm0.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm0.vtu'])
ionization2DDgm0vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm0vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization2DDgm6vtu = XMLUnstructuredGridReader(registrationName='ionization2DDgm6.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_2D/ionization2DDgm6.vtu'])
ionization2DDgm6vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization2DDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization2DDgm6vtu.TimeArray = 'None'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[ionization2DDgm0vtu, ionization2DDgm1vtu, ionization2DDgm2vtu, ionization2DDgm3vtu, ionization2DDgm4vtu, ionization2DDgm5vtu, ionization2DDgm6vtu, ionization2DDgm7vtu, ionization2DDgm8vtu, ionization2DDgm9vtu, ionization2DDgm10vtu, ionization2DDgm11vtu, ionization2DDgm12vtu, ionization2DDgm13vtu, ionization2DDgm14vtu, ionization2DDgm15vtu])

threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [0.0 , 3.0]
threshold1.LowerThreshold = 3.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 4
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 2.5
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 0
tTKPersistenceDiagramDictEncoding1.Stoppingcondition = 1
tTKPersistenceDiagramDictEncoding1.CompressionMode = 1
tTKPersistenceDiagramDictEncoding1.MaxEpoch = 1000
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# set active source
SetActiveSource(tTKPersistenceDiagramDictEncoding1)