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
asteroidDgm7vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm7.vtu', FileName=['AsteroidDgm7.vtu'])
asteroidDgm7vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm7vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm12vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm12.vtu', FileName=['AsteroidDgm12.vtu'])
asteroidDgm12vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm12vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm12vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm13vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm13.vtu', FileName=['AsteroidDgm13.vtu'])
asteroidDgm13vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm13vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm13vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm11vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm11.vtu', FileName=['AsteroidDgm11.vtu'])
asteroidDgm11vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm11vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm14vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm14.vtu', FileName=['AsteroidDgm14.vtu'])
asteroidDgm14vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm14vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm14vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm10vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm10.vtu', FileName=['AsteroidDgm10.vtu'])
asteroidDgm10vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm10vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm15vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm15.vtu', FileName=['AsteroidDgm15.vtu'])
asteroidDgm15vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm15vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm15vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm2vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm2.vtu', FileName=['AsteroidDgm2.vtu'])
asteroidDgm2vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm2vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm6vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm6.vtu', FileName=['AsteroidDgm6.vtu'])
asteroidDgm6vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm6vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm0vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm0.vtu', FileName=['AsteroidDgm0.vtu'])
asteroidDgm0vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm0vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm9vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm9.vtu', FileName=['AsteroidDgm9.vtu'])
asteroidDgm9vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm9vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm4vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm4.vtu', FileName=['AsteroidDgm4.vtu'])
asteroidDgm4vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm4vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm18vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm18.vtu', FileName=['AsteroidDgm18.vtu'])
asteroidDgm18vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm18vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm18vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm5vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm5.vtu', FileName=['AsteroidDgm5.vtu'])
asteroidDgm5vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm5vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm8vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm8.vtu', FileName=['AsteroidDgm8.vtu'])
asteroidDgm8vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm8vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm17vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm17.vtu', FileName=['AsteroidDgm17.vtu'])
asteroidDgm17vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm17vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm17vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm3vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm3.vtu', FileName=['AsteroidDgm3.vtu'])
asteroidDgm3vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm3vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm19vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm19.vtu', FileName=['AsteroidDgm19.vtu'])
asteroidDgm19vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm19vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm19vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm16vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm16.vtu', FileName=['AsteroidDgm16.vtu'])
asteroidDgm16vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm16vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm16vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
asteroidDgm1vtu = XMLUnstructuredGridReader(registrationName='AsteroidDgm1.vtu', FileName=['AsteroidDgm1.vtu'])
asteroidDgm1vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
asteroidDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
asteroidDgm1vtu.TimeArray = 'None'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[asteroidDgm0vtu, asteroidDgm1vtu, asteroidDgm2vtu, asteroidDgm3vtu, asteroidDgm4vtu, asteroidDgm5vtu, asteroidDgm6vtu, asteroidDgm7vtu, asteroidDgm8vtu, asteroidDgm9vtu, asteroidDgm10vtu, asteroidDgm11vtu, asteroidDgm12vtu, asteroidDgm13vtu, asteroidDgm14vtu, asteroidDgm15vtu, asteroidDgm16vtu, asteroidDgm17vtu, asteroidDgm18vtu, asteroidDgm19vtu])

threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [3.0 , 3.0]
threshold1.LowerThreshold = 3.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 4
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0.05
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 5.2
tTKPersistenceDiagramDictEncoding1.Stoppingcondition = 1
tTKPersistenceDiagramDictEncoding1.MaxEpoch = 1000
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.CompressionMode = 1
tTKPersistenceDiagramDictEncoding1.ThreadNumber = a

# ----------------------------------------------------------------

UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# ----------------------------------------------------------------
# restore active source
SaveData('DictionaryAsteroid.vtm' , OutputPort(tTKPersistenceDiagramDictEncoding1 , 0))
SaveData('WeightsAsteroid.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 1), Precision = 8)
