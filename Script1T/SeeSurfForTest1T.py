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
seeSurfDgm39vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm39.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm39.vtu'])
seeSurfDgm39vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm39vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm39vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm43vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm43.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm43.vtu'])
seeSurfDgm43vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm43vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm43vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm27vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm27.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm27.vtu'])
seeSurfDgm27vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm27vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm27vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm24vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm24.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm24.vtu'])
seeSurfDgm24vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm24vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm24vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm31vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm31.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm31.vtu'])
seeSurfDgm31vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm31vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm31vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm42vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm42.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm42.vtu'])
seeSurfDgm42vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm42vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm42vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm28vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm28.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm28.vtu'])
seeSurfDgm28vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm28vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm28vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm41vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm41.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm41.vtu'])
seeSurfDgm41vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm41vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm41vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm40vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm40.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm40.vtu'])
seeSurfDgm40vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm40vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm40vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm25vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm25.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm25.vtu'])
seeSurfDgm25vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm25vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm25vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm4vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm4.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm4.vtu'])
seeSurfDgm4vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm4vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm38vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm38.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm38.vtu'])
seeSurfDgm38vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm38vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm38vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm29vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm29.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm29.vtu'])
seeSurfDgm29vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm29vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm29vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm37vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm37.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm37.vtu'])
seeSurfDgm37vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm37vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm37vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm13vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm13.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm13.vtu'])
seeSurfDgm13vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm13vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm13vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm36vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm36.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm36.vtu'])
seeSurfDgm36vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm36vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm36vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm14vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm14.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm14.vtu'])
seeSurfDgm14vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm14vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm14vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm35vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm35.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm35.vtu'])
seeSurfDgm35vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm35vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm35vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm30vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm30.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm30.vtu'])
seeSurfDgm30vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm30vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm30vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm21vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm21.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm21.vtu'])
seeSurfDgm21vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm21vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm21vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm1vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm1.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm1.vtu'])
seeSurfDgm1vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm1vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm10vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm10.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm10.vtu'])
seeSurfDgm10vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm10vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm32vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm32.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm32.vtu'])
seeSurfDgm32vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm32vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm32vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm12vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm12.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm12.vtu'])
seeSurfDgm12vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm12vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm12vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm9vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm9.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm9.vtu'])
seeSurfDgm9vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm9vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm3vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm3.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm3.vtu'])
seeSurfDgm3vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm3vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm8vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm8.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm8.vtu'])
seeSurfDgm8vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm8vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm33vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm33.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm33.vtu'])
seeSurfDgm33vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm33vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm33vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm17vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm17.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm17.vtu'])
seeSurfDgm17vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm17vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm17vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm7vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm7.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm7.vtu'])
seeSurfDgm7vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm7vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm11vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm11.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm11.vtu'])
seeSurfDgm11vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm11vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm19vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm19.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm19.vtu'])
seeSurfDgm19vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm19vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm19vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm6vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm6.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm6.vtu'])
seeSurfDgm6vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm6vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm23vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm23.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm23.vtu'])
seeSurfDgm23vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm23vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm23vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm22vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm22.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm22.vtu'])
seeSurfDgm22vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm22vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm22vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm16vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm16.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm16.vtu'])
seeSurfDgm16vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm16vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm16vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm34vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm34.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm34.vtu'])
seeSurfDgm34vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm34vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm34vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm20vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm20.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm20.vtu'])
seeSurfDgm20vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm20vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm20vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm15vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm15.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm15.vtu'])
seeSurfDgm15vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm15vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm15vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm5vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm5.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm5.vtu'])
seeSurfDgm5vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm5vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm2vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm2.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm2.vtu'])
seeSurfDgm2vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm2vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm48vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm48.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm48.vtu'])
seeSurfDgm48vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm48vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm48vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm18vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm18.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm18.vtu'])
seeSurfDgm18vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm18vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm18vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm47vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm47.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm47.vtu'])
seeSurfDgm47vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm47vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm47vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm46vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm46.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm46.vtu'])
seeSurfDgm46vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm46vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm46vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm26vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm26.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm26.vtu'])
seeSurfDgm26vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm26vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm26vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm45vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm45.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm45.vtu'])
seeSurfDgm45vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm45vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm45vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
seeSurfDgm44vtu = XMLUnstructuredGridReader(registrationName='SeeSurfDgm44.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/SeeSurfNewDgms/SeeSurfDgm44.vtu'])
seeSurfDgm44vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
seeSurfDgm44vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
seeSurfDgm44vtu.TimeArray = 'None'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[seeSurfDgm1vtu, seeSurfDgm2vtu, seeSurfDgm3vtu, seeSurfDgm4vtu, seeSurfDgm5vtu, seeSurfDgm6vtu, seeSurfDgm7vtu, seeSurfDgm8vtu, seeSurfDgm9vtu, seeSurfDgm10vtu, seeSurfDgm11vtu, seeSurfDgm12vtu, seeSurfDgm13vtu, seeSurfDgm14vtu, seeSurfDgm15vtu, seeSurfDgm16vtu, seeSurfDgm17vtu, seeSurfDgm18vtu, seeSurfDgm19vtu, seeSurfDgm20vtu, seeSurfDgm21vtu, seeSurfDgm22vtu, seeSurfDgm23vtu, seeSurfDgm24vtu, seeSurfDgm25vtu, seeSurfDgm26vtu, seeSurfDgm27vtu, seeSurfDgm28vtu, seeSurfDgm29vtu, seeSurfDgm30vtu, seeSurfDgm31vtu, seeSurfDgm32vtu, seeSurfDgm33vtu, seeSurfDgm34vtu, seeSurfDgm35vtu, seeSurfDgm36vtu, seeSurfDgm37vtu, seeSurfDgm38vtu, seeSurfDgm39vtu, seeSurfDgm40vtu, seeSurfDgm41vtu, seeSurfDgm42vtu, seeSurfDgm43vtu, seeSurfDgm44vtu, seeSurfDgm45vtu, seeSurfDgm46vtu, seeSurfDgm47vtu, seeSurfDgm48vtu])

tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=groupDatasets1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 4
tTKPersistenceDiagramDictEncoding1.percentthreshold = 1.15
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 20.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


SaveData('TimersSeeSurf1PercProgMaxMinTest1T.csv', OutputPort(tTKPersistenceDiagramDictEncoding1, 5))
