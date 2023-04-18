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
viscousDgm0vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm0.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm0.vtu'])
viscousDgm0vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm1vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm1.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm1.vtu'])
viscousDgm1vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm2vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm2.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm2.vtu'])
viscousDgm2vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm3vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm3.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm3.vtu'])
viscousDgm3vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm4vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm4.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm4.vtu'])
viscousDgm4vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm5vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm5.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm5.vtu'])
viscousDgm5vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm6vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm6.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm6.vtu'])
viscousDgm6vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm7vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm7.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm7.vtu'])
viscousDgm7vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm8vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm8.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm8.vtu'])
viscousDgm8vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm9vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm9.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm9.vtu'])
viscousDgm9vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm10vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm10.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm10.vtu'])
viscousDgm10vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm11vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm11.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm11.vtu'])
viscousDgm11vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm12vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm12.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm12.vtu'])
viscousDgm12vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm12vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm13vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm13.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm13.vtu'])
viscousDgm13vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm13vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
viscousDgm14vtu = XMLUnstructuredGridReader(registrationName='ViscousDgm14.vtu', FileName=['wassersteinMergeTreesData/2016_viscous_fingering_3D/ViscousDgm14.vtu'])
viscousDgm14vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
viscousDgm14vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# Properties modified on viscousDgm0vtu
viscousDgm0vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm0vtu)

# Properties modified on viscousDgm1vtu
viscousDgm1vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm1vtu)

# Properties modified on viscousDgm2vtu
viscousDgm2vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm2vtu)

# Properties modified on viscousDgm3vtu
viscousDgm3vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm3vtu)

# Properties modified on viscousDgm4vtu
viscousDgm4vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm4vtu)

# Properties modified on viscousDgm5vtu
viscousDgm5vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm5vtu)

# Properties modified on viscousDgm6vtu
viscousDgm6vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm6vtu)

# Properties modified on viscousDgm7vtu
viscousDgm7vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm7vtu)

# Properties modified on viscousDgm8vtu
viscousDgm8vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm8vtu)

# Properties modified on viscousDgm9vtu
viscousDgm9vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm9vtu)

# Properties modified on viscousDgm10vtu
viscousDgm10vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm10vtu)

# Properties modified on viscousDgm11vtu
viscousDgm11vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm11vtu)

# Properties modified on viscousDgm12vtu
viscousDgm12vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm12vtu)

# Properties modified on viscousDgm13vtu
viscousDgm13vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm13vtu)

# Properties modified on viscousDgm14vtu
viscousDgm14vtu.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=viscousDgm14vtu)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[viscousDgm0vtu, viscousDgm1vtu, viscousDgm2vtu, viscousDgm3vtu, viscousDgm4vtu, viscousDgm5vtu, viscousDgm6vtu, viscousDgm7vtu, viscousDgm8vtu, viscousDgm9vtu, viscousDgm10vtu, viscousDgm11vtu, viscousDgm12vtu, viscousDgm13vtu, viscousDgm14vtu])
groupDatasets1.BlockNames = ['ViscousDgm0.vtu', 'ViscousDgm1.vtu', 'ViscousDgm2.vtu', 'ViscousDgm3.vtu', 'ViscousDgm4.vtu', 'ViscousDgm5.vtu', 'ViscousDgm6.vtu', 'ViscousDgm7.vtu', 'ViscousDgm8.vtu', 'ViscousDgm9.vtu', 'ViscousDgm10.vtu', 'ViscousDgm11.vtu', 'ViscousDgm12.vtu', 'ViscousDgm13.vtu', 'ViscousDgm14.vtu']

UpdatePipeline(time=0.0, proxy=groupDatasets1)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [3.0 , 3.0]
threshold1.LowerThreshold = 3.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 2.3
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 0
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# set active source
SetActiveSource(tTKPersistenceDiagramDictEncoding1)