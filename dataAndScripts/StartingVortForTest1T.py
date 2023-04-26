# state file generated using paraview version 5.9.1-5-g35227227

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 9

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

a = int(sys.argv[1])

# create a new 'XML Unstructured Grid Reader'
startVortDgm0vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm0.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm0.vtu'])
startVortDgm0vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm1vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm1.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm1.vtu'])
startVortDgm1vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm2vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm2.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm2.vtu'])
startVortDgm2vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm3vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm3.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm3.vtu'])
startVortDgm3vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm4vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm4.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm4.vtu'])
startVortDgm4vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm5vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm5.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm5.vtu'])
startVortDgm5vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm6vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm6.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm6.vtu'])
startVortDgm6vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm7vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm7.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm7.vtu'])
startVortDgm7vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm8vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm8.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm8.vtu'])
startVortDgm8vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm9vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm9.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm9.vtu'])
startVortDgm9vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm10vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm10.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm10.vtu'])
startVortDgm10vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
startVortDgm11vtu = XMLUnstructuredGridReader(registrationName='StartVortDgm11.vtu', FileName=['wassersteinMergeTreesData/data/StartVortNewDgms/StartVortDgm11.vtu'])
startVortDgm11vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
startVortDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# Properties modified on startVortDgm0vtu
startVortDgm0vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm0vtu)

# Properties modified on startVortDgm1vtu
startVortDgm1vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm1vtu)

# Properties modified on startVortDgm2vtu
startVortDgm2vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm2vtu)

# Properties modified on startVortDgm3vtu
startVortDgm3vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm3vtu)

# Properties modified on startVortDgm4vtu
startVortDgm4vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm4vtu)

# Properties modified on startVortDgm5vtu
startVortDgm5vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm5vtu)

# Properties modified on startVortDgm6vtu
startVortDgm6vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm6vtu)

# Properties modified on startVortDgm7vtu
startVortDgm7vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm7vtu)

# Properties modified on startVortDgm8vtu
startVortDgm8vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm8vtu)

# Properties modified on startVortDgm9vtu
startVortDgm9vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm9vtu)

# Properties modified on startVortDgm10vtu
startVortDgm10vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm10vtu)

# Properties modified on startVortDgm11vtu
startVortDgm11vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=startVortDgm11vtu)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[startVortDgm0vtu, startVortDgm1vtu, startVortDgm2vtu, startVortDgm3vtu, startVortDgm4vtu, startVortDgm5vtu, startVortDgm6vtu, startVortDgm7vtu, startVortDgm8vtu, startVortDgm9vtu, startVortDgm10vtu, startVortDgm11vtu])
groupDatasets1.BlockNames = ['StartVortDgm0.vtu', 'StartVortDgm1.vtu', 'StartVortDgm2.vtu', 'StartVortDgm3.vtu', 'StartVortDgm4.vtu', 'StartVortDgm5.vtu', 'StartVortDgm6.vtu', 'StartVortDgm7.vtu', 'StartVortDgm8.vtu', 'StartVortDgm9.vtu', 'StartVortDgm10.vtu', 'StartVortDgm11.vtu']

UpdatePipeline(time=0.0, proxy=groupDatasets1)

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=groupDatasets1,
    optionalinput=None)


tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 2
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0.25
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 2.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = a


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# restore active source
SaveData('DictionaryStartingVortex.vtm' , OutputPort(tTKPersistenceDiagramDictEncoding1 , 0))
SaveData('WeightsStartingVortex.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 1), Precision = 8)
