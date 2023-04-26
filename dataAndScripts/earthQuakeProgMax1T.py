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
diagEarthQuake10vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake10.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake10.vtu'])
diagEarthQuake10vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake10vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake10vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake0vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake0.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake0.vtu'])
diagEarthQuake0vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake0vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake0vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake7vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake7.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake7.vtu'])
diagEarthQuake7vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake7vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake7vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake2vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake2.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake2.vtu'])
diagEarthQuake2vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake2vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake2vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake9vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake9.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake9.vtu'])
diagEarthQuake9vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake9vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake9vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake8vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake8.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake8.vtu'])
diagEarthQuake8vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake8vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake8vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake3vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake3.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake3.vtu'])
diagEarthQuake3vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake3vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake3vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake6vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake6.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake6.vtu'])
diagEarthQuake6vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake6vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake6vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake11vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake11.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake11.vtu'])
diagEarthQuake11vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake11vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake11vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake5vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake5.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake5.vtu'])
diagEarthQuake5vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake5vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake5vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake4vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake4.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake4.vtu'])
diagEarthQuake4vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake4vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake4vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
diagEarthQuake1vtu = XMLUnstructuredGridReader(registrationName='DiagEarthQuake1.vtu', FileName=['wassersteinMergeTreesData/2006_earthquake_3D/DiagEarthQuake1.vtu'])
diagEarthQuake1vtu.CellArrayStatus = ['Birth', 'IsFinite','PairIdentifier', 'PairType', 'Persistence']
diagEarthQuake1vtu.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']
diagEarthQuake1vtu.TimeArray = 'None'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[diagEarthQuake0vtu, diagEarthQuake1vtu, diagEarthQuake2vtu, diagEarthQuake3vtu, diagEarthQuake4vtu, diagEarthQuake5vtu, diagEarthQuake6vtu, diagEarthQuake7vtu, diagEarthQuake8vtu, diagEarthQuake9vtu, diagEarthQuake10vtu, diagEarthQuake11vtu])

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
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 2.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.Stoppingcondition = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = a


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# set active source
# ----------------------------------------------------------------
# restore active source
SaveData('DictionaryEarthQuake.vtm' , OutputPort(tTKPersistenceDiagramDictEncoding1 , 0))
SaveData('WeightsEarthQuake.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 1), Precision = 8)
