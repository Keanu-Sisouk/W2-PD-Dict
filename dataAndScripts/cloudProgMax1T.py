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
cloudDgm11vtu = XMLUnstructuredGridReader(registrationName='cloudDgm11.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm11.vtu'])
cloudDgm11vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm2vtu = XMLUnstructuredGridReader(registrationName='cloudDgm2.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm2.vtu'])
cloudDgm2vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm3vtu = XMLUnstructuredGridReader(registrationName='cloudDgm3.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm3.vtu'])
cloudDgm3vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm0vtu = XMLUnstructuredGridReader(registrationName='cloudDgm0.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm0.vtu'])
cloudDgm0vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm1vtu = XMLUnstructuredGridReader(registrationName='cloudDgm1.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm1.vtu'])
cloudDgm1vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm6vtu = XMLUnstructuredGridReader(registrationName='cloudDgm6.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm6.vtu'])
cloudDgm6vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm10vtu = XMLUnstructuredGridReader(registrationName='cloudDgm10.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm10.vtu'])
cloudDgm10vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm8vtu = XMLUnstructuredGridReader(registrationName='cloudDgm8.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm8.vtu'])
cloudDgm8vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm4vtu = XMLUnstructuredGridReader(registrationName='cloudDgm4.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm4.vtu'])
cloudDgm4vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm9vtu = XMLUnstructuredGridReader(registrationName='cloudDgm9.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm9.vtu'])
cloudDgm9vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm7vtu = XMLUnstructuredGridReader(registrationName='cloudDgm7.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm7.vtu'])
cloudDgm7vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'XML Unstructured Grid Reader'
cloudDgm5vtu = XMLUnstructuredGridReader(registrationName='cloudDgm5.vtu', FileName=['wassersteinMergeTreesData/cloud/cloudDgm5.vtu'])
cloudDgm5vtu.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
cloudDgm5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[cloudDgm0vtu, cloudDgm1vtu, cloudDgm2vtu, cloudDgm3vtu, cloudDgm4vtu, cloudDgm5vtu, cloudDgm6vtu, cloudDgm7vtu, cloudDgm8vtu, cloudDgm9vtu, cloudDgm10vtu, cloudDgm11vtu])

threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [0.0 , 3.0]
threshold1.LowerThreshold = 3.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.percentthreshold = 10
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 6.0
tTKPersistenceDiagramDictEncoding1.MaxEpoch = 1000
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1

# ----------------------------------------------------------------
# restore active source
UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# set active source
SetActiveSource(tTKPersistenceDiagramDictEncoding1)