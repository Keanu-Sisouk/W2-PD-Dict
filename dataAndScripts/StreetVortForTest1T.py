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


# create a new 'XML Image Data Reader'
vortexStreetGoodEnsemble2vti = XMLImageDataReader(registrationName='vortexStreetGoodEnsemble2.vti', FileName=['wassersteinMergeTreesData/data/vortexStreetGoodEnsemble2.vti'])
vortexStreetGoodEnsemble2vti.CellArrayStatus = ['vtkGhostType']
vortexStreetGoodEnsemble2vti.PointArrayStatus = ['100.0', '100.1', '100.2', '100.3', '100.4', '100.5', '100.6', '100.7', '100.9', '160.0', '160.1', '160.2', '160.3', '160.4', '160.5', '160.6', '160.7', '160.8', '200.0', '200.1', '200.2', '200.3', '200.4', '200.5', '200.6', '200.7', '200.8', '50.0', '50.1', '50.2', '50.3', '50.5', '50.6', '50.7', '50.8', '50.9', '60.1', '60.2', '60.3', '60.4', '60.5', '60.6', '60.7', '60.8', '60.9']
vortexStreetGoodEnsemble2vti.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram27 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram27', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram27.ScalarField = ['POINTS', '200.8']
tTKPersistenceDiagram27.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram27.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram43 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram43', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram43.ScalarField = ['POINTS', '60.7']
tTKPersistenceDiagram43.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram43.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram24 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram24', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram24.ScalarField = ['POINTS', '200.5']
tTKPersistenceDiagram24.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram24.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram42 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram42', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram42.ScalarField = ['POINTS', '60.6']
tTKPersistenceDiagram42.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram42.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram31 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram31', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram31.ScalarField = ['POINTS', '50.3']
tTKPersistenceDiagram31.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram31.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram28 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram28', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram28.ScalarField = ['POINTS', '50.0']
tTKPersistenceDiagram28.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram28.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram41 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram41', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram41.ScalarField = ['POINTS', '60.5']
tTKPersistenceDiagram41.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram41.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram40 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram40', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram40.ScalarField = ['POINTS', '60.4']
tTKPersistenceDiagram40.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram40.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram25 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram25', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram25.ScalarField = ['POINTS', '200.6']
tTKPersistenceDiagram25.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram25.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram4', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram4.ScalarField = ['POINTS', '100.3']
tTKPersistenceDiagram4.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram4.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram39 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram39', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram39.ScalarField = ['POINTS', '60.3']
tTKPersistenceDiagram39.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram39.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram38 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram38', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram38.ScalarField = ['POINTS', '60.2']
tTKPersistenceDiagram38.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram38.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram29 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram29', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram29.ScalarField = ['POINTS', '50.1']
tTKPersistenceDiagram29.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram29.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram37 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram37', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram37.ScalarField = ['POINTS', '60.1']
tTKPersistenceDiagram37.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram37.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram16 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram16', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram16.ScalarField = ['POINTS', '160.6']
tTKPersistenceDiagram16.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram16.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram36 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram36', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram36.ScalarField = ['POINTS', '50.9']
tTKPersistenceDiagram36.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram36.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram15 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram15', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram15.ScalarField = ['POINTS', '160.5']
tTKPersistenceDiagram15.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram15.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram35 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram35', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram35.ScalarField = ['POINTS', '50.8']
tTKPersistenceDiagram35.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram35.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram30 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram30', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram30.ScalarField = ['POINTS', '50.2']
tTKPersistenceDiagram30.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram30.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram21 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram21', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram21.ScalarField = ['POINTS', '200.2']
tTKPersistenceDiagram21.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram21.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram1.ScalarField = ['POINTS', '100.0']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram1.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram11 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram11', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram11.ScalarField = ['POINTS', '160.1']
tTKPersistenceDiagram11.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram11.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram32 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram32', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram32.ScalarField = ['POINTS', '50.5']
tTKPersistenceDiagram32.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram32.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram12 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram12', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram12.ScalarField = ['POINTS', '160.2']
tTKPersistenceDiagram12.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram12.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram3', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram3.ScalarField = ['POINTS', '100.2']
tTKPersistenceDiagram3.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram3.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram33 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram33', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram33.ScalarField = ['POINTS', '50.6']
tTKPersistenceDiagram33.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram33.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram14 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram14', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram14.ScalarField = ['POINTS', '160.4']
tTKPersistenceDiagram14.InputOffsetField = ['POINTS', '100.0']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram9 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram9', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram9.ScalarField = ['POINTS', '100.9']
tTKPersistenceDiagram9.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram9.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram23 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram23', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram23.ScalarField = ['POINTS', '200.4']
tTKPersistenceDiagram23.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram23.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram13 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram13', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram13.ScalarField = ['POINTS', '160.3']
tTKPersistenceDiagram13.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram13.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram22 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram22', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram22.ScalarField = ['POINTS', '200.3']
tTKPersistenceDiagram22.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram22.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram10 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram10', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram10.ScalarField = ['POINTS', '160.0']
tTKPersistenceDiagram10.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram10.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram34 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram34', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram34.ScalarField = ['POINTS', '50.7']
tTKPersistenceDiagram34.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram34.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram17 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram17', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram17.ScalarField = ['POINTS', '160.7']
tTKPersistenceDiagram17.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram17.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram19 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram19', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram19.ScalarField = ['POINTS', '200.0']
tTKPersistenceDiagram19.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram19.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram20 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram20', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram20.ScalarField = ['POINTS', '200.1']
tTKPersistenceDiagram20.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram20.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram8 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram8', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram8.ScalarField = ['POINTS', '100.7']
tTKPersistenceDiagram8.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram8.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram2', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram2.ScalarField = ['POINTS', '100.1']
tTKPersistenceDiagram2.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram2.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram7 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram7', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram7.ScalarField = ['POINTS', '100.6']
tTKPersistenceDiagram7.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram7.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram18 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram18', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram18.ScalarField = ['POINTS', '160.8']
tTKPersistenceDiagram18.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram18.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram6 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram6', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram6.ScalarField = ['POINTS', '100.5']
tTKPersistenceDiagram6.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram6.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram5', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram5.ScalarField = ['POINTS', '100.4']
tTKPersistenceDiagram5.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram5.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram26 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram26', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram26.ScalarField = ['POINTS', '200.7']
tTKPersistenceDiagram26.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram26.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram45 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram45', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram45.ScalarField = ['POINTS', '60.9']
tTKPersistenceDiagram45.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram45.UseAllCores = 1

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram44 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram44', Input=vortexStreetGoodEnsemble2vti)
tTKPersistenceDiagram44.ScalarField = ['POINTS', '60.8']
tTKPersistenceDiagram44.InputOffsetField = ['POINTS', '100.0']
tTKPersistenceDiagram44.UseAllCores = 1

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[tTKPersistenceDiagram1, tTKPersistenceDiagram2, tTKPersistenceDiagram3, tTKPersistenceDiagram4, tTKPersistenceDiagram5, tTKPersistenceDiagram6, tTKPersistenceDiagram7, tTKPersistenceDiagram8, tTKPersistenceDiagram9, tTKPersistenceDiagram10, tTKPersistenceDiagram11, tTKPersistenceDiagram12, tTKPersistenceDiagram13, tTKPersistenceDiagram14, tTKPersistenceDiagram15, tTKPersistenceDiagram16, tTKPersistenceDiagram17, tTKPersistenceDiagram18, tTKPersistenceDiagram19, tTKPersistenceDiagram20, tTKPersistenceDiagram21, tTKPersistenceDiagram22, tTKPersistenceDiagram23, tTKPersistenceDiagram24, tTKPersistenceDiagram25, tTKPersistenceDiagram26, tTKPersistenceDiagram27, tTKPersistenceDiagram28, tTKPersistenceDiagram29, tTKPersistenceDiagram30, tTKPersistenceDiagram31, tTKPersistenceDiagram32, tTKPersistenceDiagram33, tTKPersistenceDiagram34, tTKPersistenceDiagram35, tTKPersistenceDiagram36, tTKPersistenceDiagram37, tTKPersistenceDiagram38, tTKPersistenceDiagram39, tTKPersistenceDiagram40, tTKPersistenceDiagram41, tTKPersistenceDiagram42, tTKPersistenceDiagram43, tTKPersistenceDiagram44, tTKPersistenceDiagram45])
# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=groupDatasets1)
threshold1.Scalars = ['POINTS', 'CriticalType']
# threshold1.ThresholdRange = [3.0 , 3.0]
threshold1.LowerThreshold = 3.0
threshold1.UpperThreshold = 3.0
threshold1.AllScalars = 0

tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=threshold1,
    optionalinput=None)


tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 5
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 5.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = a


UpdatePipeline(time=0.0, proxy=tTKPersistenceDiagramDictEncoding1)

# restore active source
SaveData('DictionaryStreetVortex.vtm' , OutputPort(tTKPersistenceDiagramDictEncoding1 , 0))
SaveData('WeightsStreetVortex.csv', OutputPort(tTKPersistenceDiagramDictEncoding1 , 1), Precision = 8)
