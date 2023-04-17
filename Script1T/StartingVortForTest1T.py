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

# create a new 'XML Image Data Reader'
startingVortexGoodEnsemblevti = XMLImageDataReader(registrationName='startingVortexGoodEnsemble.vti', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/data/startingVortexGoodEnsemble.vti'])
startingVortexGoodEnsemblevti.PointArrayStatus = ['vorticity_angle_02', 'vorticity_angle_03', 'vorticity_angle_04', 'vorticity_angle_05', 'vorticity_angle_06', 'vorticity_angle_08', 'vorticity_angle_38', 'vorticity_angle_39', 'vorticity_angle_40', 'vorticity_angle_41', 'vorticity_angle_42', 'vorticity_angle_43']
startingVortexGoodEnsemblevti.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram12 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram12', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram12.ScalarField = ['POINTS', 'vorticity_angle_43']
tTKPersistenceDiagram12.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram6 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram6', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram6.ScalarField = ['POINTS', 'vorticity_angle_08']
tTKPersistenceDiagram6.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram5', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram5.ScalarField = ['POINTS', 'vorticity_angle_06']
tTKPersistenceDiagram5.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram3', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram3.ScalarField = ['POINTS', 'vorticity_angle_04']
tTKPersistenceDiagram3.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram8 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram8', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram8.ScalarField = ['POINTS', 'vorticity_angle_39']
tTKPersistenceDiagram8.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram4', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram4.ScalarField = ['POINTS', 'vorticity_angle_05']
tTKPersistenceDiagram4.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'vorticity_angle_02']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram11 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram11', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram11.ScalarField = ['POINTS', 'vorticity_angle_42']
tTKPersistenceDiagram11.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram2', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram2.ScalarField = ['POINTS', 'vorticity_angle_03']
tTKPersistenceDiagram2.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram9 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram9', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram9.ScalarField = ['POINTS', 'vorticity_angle_40']
tTKPersistenceDiagram9.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram7 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram7', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram7.ScalarField = ['POINTS', 'vorticity_angle_38']
tTKPersistenceDiagram7.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram10 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram10', Input=startingVortexGoodEnsemblevti)
tTKPersistenceDiagram10.ScalarField = ['POINTS', 'vorticity_angle_41']
tTKPersistenceDiagram10.InputOffsetField = ['POINTS', 'vorticity_angle_02']



# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[tTKPersistenceDiagram1, tTKPersistenceDiagram2, tTKPersistenceDiagram3, tTKPersistenceDiagram4, tTKPersistenceDiagram5, tTKPersistenceDiagram6, tTKPersistenceDiagram7, tTKPersistenceDiagram8, tTKPersistenceDiagram9, tTKPersistenceDiagram10, tTKPersistenceDiagram11, tTKPersistenceDiagram12])

tTKPersistenceDiagramDictEncoding1 = TTKPersistenceDiagramDictEncoding(registrationName='TTKPersistenceDiagramDictEncoding1', Input=groupDatasets1,
    optionalinput=None)

tTKPersistenceDiagramDictEncoding1.NumberofAtoms = 2
tTKPersistenceDiagramDictEncoding1.percentthreshold = 0.25
tTKPersistenceDiagramDictEncoding1.Compressionfactor = 2.
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


SaveData('TimersStartVort1percProgMaxMinTest1T.csv', OutputPort(tTKPersistenceDiagramDictEncoding1, 5))
