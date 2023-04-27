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

# create a new 'XML MultiBlock Data Reader'
volcanoDgmvtm = XMLMultiBlockDataReader(registrationName='VolcanoDgm.vtm', FileName=['wassersteinMergeTreesData/2014_volcanic_eruptions_2D/VolcanoDgm.vtm'])
volcanoDgmvtm.CellArrayStatus = ['PairIdentifier', 'PairType', 'Persistence', 'Birth', 'IsFinite']
volcanoDgmvtm.PointArrayStatus = ['ttkVertexScalarField', 'CriticalType', 'Coordinates']

# Properties modified on volcanoDgmvtm
volcanoDgmvtm.TimeArray = 'None'

UpdatePipeline(time=0.0, proxy=volcanoDgmvtm)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=volcanoDgmvtm)
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
tTKPersistenceDiagramDictEncoding1.ThreadNumber = a

# ----------------------------------------------------------------
# restore active source

UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# restore active source
SaveData('Outputs/DictionaryVolcanicEruption.vtm' , OutputPort(tTKPersistenceDiagramDictEncoding1 , 0))
SaveData('Outputs/WeightsVolcanicEruption.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 1), Precision = 8)
