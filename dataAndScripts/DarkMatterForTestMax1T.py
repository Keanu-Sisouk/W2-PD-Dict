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
darkMatterDgm38vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm38.vtu', FileName=['DarkMatterDgm38.vtu'])
darkMatterDgm38vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm38vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm38vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm39vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm39.vtu', FileName=['DarkMatterDgm39.vtu'])
darkMatterDgm39vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm39vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm39vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm8vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm8.vtu', FileName=['DarkMatterDgm8.vtu'])
darkMatterDgm8vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm8vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm27vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm27.vtu', FileName=['DarkMatterDgm27.vtu'])
darkMatterDgm27vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm27vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm27vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm24vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm24.vtu', FileName=['DarkMatterDgm24.vtu'])
darkMatterDgm24vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm24vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm24vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm31vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm31.vtu', FileName=['DarkMatterDgm31.vtu'])
darkMatterDgm31vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm31vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm31vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm7vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm7.vtu', FileName=['DarkMatterDgm7.vtu'])
darkMatterDgm7vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm7vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm28vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm28.vtu', FileName=['DarkMatterDgm28.vtu'])
darkMatterDgm28vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm28vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm28vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm6vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm6.vtu', FileName=['DarkMatterDgm6.vtu'])
darkMatterDgm6vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm6vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm5vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm5.vtu', FileName=['DarkMatterDgm5.vtu'])
darkMatterDgm5vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm5vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm25vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm25.vtu', FileName=['DarkMatterDgm25.vtu'])
darkMatterDgm25vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm25vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm25vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm4vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm4.vtu', FileName=['DarkMatterDgm4.vtu'])
darkMatterDgm4vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm4vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm29vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm29.vtu', FileName=['DarkMatterDgm29.vtu'])
darkMatterDgm29vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm29vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm29vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm37vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm37.vtu', FileName=['DarkMatterDgm37.vtu'])
darkMatterDgm37vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm37vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm37vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm14vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm14.vtu', FileName=['DarkMatterDgm14.vtu'])
darkMatterDgm14vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm14vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm14vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm36vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm36.vtu', FileName=['DarkMatterDgm36.vtu'])
darkMatterDgm36vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm36vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm36vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm11vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm11.vtu', FileName=['DarkMatterDgm11.vtu'])
darkMatterDgm11vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm11vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm30vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm30.vtu', FileName=['DarkMatterDgm30.vtu'])
darkMatterDgm30vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm30vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm30vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm35vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm35.vtu', FileName=['DarkMatterDgm35.vtu'])
darkMatterDgm35vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm35vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm35vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm21vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm21.vtu', FileName=['DarkMatterDgm21.vtu'])
darkMatterDgm21vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm21vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm21vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm1vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm1.vtu', FileName=['DarkMatterDgm1.vtu'])
darkMatterDgm1vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm1vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm12vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm12.vtu', FileName=['DarkMatterDgm12.vtu'])
darkMatterDgm12vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm12vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm12vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm32vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm32.vtu', FileName=['DarkMatterDgm32.vtu'])
darkMatterDgm32vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm32vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm32vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm13vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm13.vtu', FileName=['DarkMatterDgm13.vtu'])
darkMatterDgm13vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm13vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm13vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm3vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm3.vtu', FileName=['DarkMatterDgm3.vtu'])
darkMatterDgm3vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm3vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm33vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm33.vtu', FileName=['DarkMatterDgm33.vtu'])
darkMatterDgm33vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm33vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm33vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm17vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm17.vtu', FileName=['DarkMatterDgm17.vtu'])
darkMatterDgm17vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm17vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm17vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm16vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm16.vtu', FileName=['DarkMatterDgm16.vtu'])
darkMatterDgm16vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm16vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm16vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm19vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm19.vtu', FileName=['DarkMatterDgm19.vtu'])
darkMatterDgm19vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm19vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm19vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm23vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm23.vtu', FileName=['DarkMatterDgm23.vtu'])
darkMatterDgm23vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm23vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm23vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm20vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm20.vtu', FileName=['DarkMatterDgm20.vtu'])
darkMatterDgm20vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm20vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm20vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm15vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm15.vtu', FileName=['DarkMatterDgm15.vtu'])
darkMatterDgm15vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm15vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm15vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm22vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm22.vtu', FileName=['DarkMatterDgm22.vtu'])
darkMatterDgm22vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm22vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm22vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm10vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm10.vtu', FileName=['DarkMatterDgm10.vtu'])
darkMatterDgm10vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm10vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm34vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm34.vtu', FileName=['DarkMatterDgm34.vtu'])
darkMatterDgm34vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm34vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm34vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm2vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm2.vtu', FileName=['DarkMatterDgm2.vtu'])
darkMatterDgm2vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm2vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm0vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm0.vtu', FileName=['DarkMatterDgm0.vtu'])
darkMatterDgm0vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm0vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm18vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm18.vtu', FileName=['DarkMatterDgm18.vtu'])
darkMatterDgm18vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm18vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm18vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm26vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm26.vtu', FileName=['DarkMatterDgm26.vtu'])
darkMatterDgm26vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm26vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm26vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
darkMatterDgm9vtu = XMLUnstructuredGridReader(registrationName='DarkMatterDgm9.vtu', FileName=['DarkMatterDgm9.vtu'])
darkMatterDgm9vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
darkMatterDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
darkMatterDgm9vtu.TimeArray = 'None'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[darkMatterDgm0vtu, darkMatterDgm1vtu, darkMatterDgm2vtu, darkMatterDgm3vtu, darkMatterDgm4vtu, darkMatterDgm5vtu, darkMatterDgm6vtu, darkMatterDgm7vtu, darkMatterDgm8vtu, darkMatterDgm9vtu, darkMatterDgm10vtu, darkMatterDgm11vtu, darkMatterDgm12vtu, darkMatterDgm13vtu, darkMatterDgm14vtu, darkMatterDgm15vtu, darkMatterDgm16vtu, darkMatterDgm17vtu, darkMatterDgm18vtu, darkMatterDgm19vtu, darkMatterDgm20vtu, darkMatterDgm21vtu, darkMatterDgm22vtu, darkMatterDgm23vtu, darkMatterDgm24vtu, darkMatterDgm25vtu, darkMatterDgm26vtu, darkMatterDgm27vtu, darkMatterDgm28vtu, darkMatterDgm29vtu, darkMatterDgm30vtu, darkMatterDgm31vtu, darkMatterDgm32vtu, darkMatterDgm33vtu, darkMatterDgm34vtu, darkMatterDgm35vtu, darkMatterDgm36vtu, darkMatterDgm37vtu, darkMatterDgm38vtu, darkMatterDgm39vtu])

# create a new 'Threshold'
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
tTKPersistenceDiagramDictEncoding1.percentthreshold = 10
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 10.0
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.MaxEpoch = 1000
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# set active source
SetActiveSource(tTKPersistenceDiagramDictEncoding1)