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
# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(registrationName='TTKCinemaReader1', DatabasePath='Isabel.cdb')

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=tTKCinemaReader1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=tTKCinemaProductReader1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'velocityMag']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'velocityMag']

# create a new 'TTK PersistenceDiagramDictEncoding'
tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=tTKPersistenceDiagram1,
    optionalinput=None)
tTKPersistenceDiagramDictEncoding1.percentthreshold = 1
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 5.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = a




UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# restore active source
SaveData('DictionaryIsabel.vtm' , OutputPort(tTKPersistenceDiagramDictEncoding1 , 0))
SaveData('WeightsIsabel.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 1), Precision = 8)
