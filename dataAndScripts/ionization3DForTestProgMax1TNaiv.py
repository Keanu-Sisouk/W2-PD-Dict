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
ionization3DDgm8vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm8.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm8.vtu'])
ionization3DDgm8vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm8vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm5vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm5.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm5.vtu'])
ionization3DDgm5vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm5vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm9vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm9.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm9.vtu'])
ionization3DDgm9vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm9vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm11vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm11.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm11.vtu'])
ionization3DDgm11vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm11vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm1vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm1.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm1.vtu'])
ionization3DDgm1vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm1vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm2vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm2.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm2.vtu'])
ionization3DDgm2vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm2vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm13vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm13.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm13.vtu'])
ionization3DDgm13vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm13vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm13vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm14vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm14.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm14.vtu'])
ionization3DDgm14vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm14vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm14vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm12vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm12.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm12.vtu'])
ionization3DDgm12vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm12vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm12vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm10vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm10.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm10.vtu'])
ionization3DDgm10vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm10vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm7vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm7.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm7.vtu'])
ionization3DDgm7vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm7vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm4vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm4.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm4.vtu'])
ionization3DDgm4vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm4vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm3vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm3.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm3.vtu'])
ionization3DDgm3vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm3vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm15vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm15.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm15.vtu'])
ionization3DDgm15vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm15vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm15vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm0vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm0.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm0.vtu'])
ionization3DDgm0vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm0vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
ionization3DDgm6vtu = XMLUnstructuredGridReader(registrationName='ionization3DDgm6.vtu', FileName=['wassersteinMergeTreesData/2008_ionization_front_3D/ionization3DDgm6.vtu'])
ionization3DDgm6vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
ionization3DDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
ionization3DDgm6vtu.TimeArray = 'None'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[ionization3DDgm0vtu, ionization3DDgm1vtu, ionization3DDgm2vtu, ionization3DDgm3vtu, ionization3DDgm4vtu, ionization3DDgm5vtu, ionization3DDgm6vtu, ionization3DDgm7vtu, ionization3DDgm8vtu, ionization3DDgm9vtu, ionization3DDgm10vtu, ionization3DDgm11vtu, ionization3DDgm12vtu, ionization3DDgm13vtu, ionization3DDgm14vtu, ionization3DDgm15vtu])

threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [0.0 , 3.0]
threshold1.LowerThreshold = 0.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 4
tTKPersistenceDiagramDictEncoding1.percentthreshold = 1
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 3.3
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 0
tTKPersistenceDiagramDictEncoding1.Stoppingcondition = 1
tTKPersistenceDiagramDictEncoding1.MaxEpoch = 1000
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# set active source
SetActiveSource(tTKPersistenceDiagramDictEncoding1)