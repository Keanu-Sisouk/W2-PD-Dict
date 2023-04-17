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
a020_run06_120vtu = XMLUnstructuredGridReader(registrationName='0.20_run06_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.20_run06_120.vtu'])
a020_run06_120vtu.PointArrayStatus = ['SplatterValues']
a020_run06_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram5 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram5', Input=a020_run06_120vtu)
tTKPersistenceDiagram5.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram5.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram5.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram5.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a030_run03_120vtu = XMLUnstructuredGridReader(registrationName='0.30_run03_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.30_run03_120.vtu'])
a030_run03_120vtu.PointArrayStatus = ['SplatterValues']
a030_run03_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram8 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram8', Input=a030_run03_120vtu)
tTKPersistenceDiagram8.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram8.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram8.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram8.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a044_run02_120vtu = XMLUnstructuredGridReader(registrationName='0.44_run02_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.44_run02_120.vtu'])
a044_run02_120vtu.PointArrayStatus = ['SplatterValues']
a044_run02_120vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
a044_run03_120vtu = XMLUnstructuredGridReader(registrationName='0.44_run03_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.44_run03_120.vtu'])
a044_run03_120vtu.PointArrayStatus = ['SplatterValues']
a044_run03_120vtu.TimeArray = 'None'

# create a new 'XML Unstructured Grid Reader'
a044_run01_120vtu = XMLUnstructuredGridReader(registrationName='0.44_run01_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.44_run01_120.vtu'])
a044_run01_120vtu.PointArrayStatus = ['SplatterValues']
a044_run01_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram11 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram11', Input=a044_run01_120vtu)
tTKPersistenceDiagram11.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram11.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram11.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram11.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a030_run04_120vtu = XMLUnstructuredGridReader(registrationName='0.30_run04_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.30_run04_120.vtu'])
a030_run04_120vtu.PointArrayStatus = ['SplatterValues']
a030_run04_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram9 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram9', Input=a030_run04_120vtu)
tTKPersistenceDiagram9.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram9.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram9.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram9.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram13 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram13', Input=a044_run03_120vtu)
tTKPersistenceDiagram13.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram13.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram13.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram13.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a044_run04_120vtu = XMLUnstructuredGridReader(registrationName='0.44_run04_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.44_run04_120.vtu'])
a044_run04_120vtu.PointArrayStatus = ['SplatterValues']
a044_run04_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram14 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram14', Input=a044_run04_120vtu)
tTKPersistenceDiagram14.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram14.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram14.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram14.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a044_run05_120vtu = XMLUnstructuredGridReader(registrationName='0.44_run05_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.44_run05_120.vtu'])
a044_run05_120vtu.PointArrayStatus = ['SplatterValues']
a044_run05_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram15 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram15', Input=a044_run05_120vtu)
tTKPersistenceDiagram15.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram15.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram15.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram15.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a030_run01_120vtu = XMLUnstructuredGridReader(registrationName='0.30_run01_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.30_run01_120.vtu'])
a030_run01_120vtu.PointArrayStatus = ['SplatterValues']
a030_run01_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram6 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram6', Input=a030_run01_120vtu)
tTKPersistenceDiagram6.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram6.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram6.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram6.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a030_run05_120vtu = XMLUnstructuredGridReader(registrationName='0.30_run05_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.30_run05_120.vtu'])
a030_run05_120vtu.PointArrayStatus = ['SplatterValues']
a030_run05_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram10 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram10', Input=a030_run05_120vtu)
tTKPersistenceDiagram10.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram10.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram10.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram10.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a020_run01_120vtu = XMLUnstructuredGridReader(registrationName='0.20_run01_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.20_run01_120.vtu'])
a020_run01_120vtu.PointArrayStatus = ['SplatterValues']
a020_run01_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=a020_run01_120vtu)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram1.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram1.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a020_run05_120vtu = XMLUnstructuredGridReader(registrationName='0.20_run05_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.20_run05_120.vtu'])
a020_run05_120vtu.PointArrayStatus = ['SplatterValues']
a020_run05_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram4 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram4', Input=a020_run05_120vtu)
tTKPersistenceDiagram4.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram4.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram4.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram4.Saddlesaddlediagramdimension1slowest = 0

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram12 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram12', Input=a044_run02_120vtu)
tTKPersistenceDiagram12.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram12.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram12.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram12.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a020_run03_120vtu = XMLUnstructuredGridReader(registrationName='0.20_run03_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.20_run03_120.vtu'])
a020_run03_120vtu.PointArrayStatus = ['SplatterValues']
a020_run03_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram2 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram2', Input=a020_run03_120vtu)
tTKPersistenceDiagram2.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram2.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram2.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram2.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a020_run04_120vtu = XMLUnstructuredGridReader(registrationName='0.20_run04_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.20_run04_120.vtu'])
a020_run04_120vtu.PointArrayStatus = ['SplatterValues']
a020_run04_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram3 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram3', Input=a020_run04_120vtu)
tTKPersistenceDiagram3.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram3.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram3.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram3.Saddlesaddlediagramdimension1slowest = 0

# create a new 'XML Unstructured Grid Reader'
a030_run02_120vtu = XMLUnstructuredGridReader(registrationName='0.30_run02_120.vtu', FileName=['/home/keanu/ttk-data/wassersteinMergeTreesData/2016_viscous_fingering_3D/0.30_run02_120.vtu'])
a030_run02_120vtu.PointArrayStatus = ['SplatterValues']
a030_run02_120vtu.TimeArray = 'None'

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram7 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram7', Input=a030_run02_120vtu)
tTKPersistenceDiagram7.ScalarField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram7.InputOffsetField = ['POINTS', 'SplatterValues']
tTKPersistenceDiagram7.Dimensions = 'Selected Dimensions (no infinite pairs)'
tTKPersistenceDiagram7.Saddlesaddlediagramdimension1slowest = 0

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[tTKPersistenceDiagram1, tTKPersistenceDiagram2, tTKPersistenceDiagram3, tTKPersistenceDiagram4, tTKPersistenceDiagram5, tTKPersistenceDiagram6, tTKPersistenceDiagram7, tTKPersistenceDiagram8, tTKPersistenceDiagram9, tTKPersistenceDiagram10, tTKPersistenceDiagram11, tTKPersistenceDiagram12, tTKPersistenceDiagram13, tTKPersistenceDiagram14, tTKPersistenceDiagram15])
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
tTKPersistenceDiagramDictEncoding1.Progressiveapproach = 1
tTKPersistenceDiagramDictEncoding1.UseAllCores = 0
tTKPersistenceDiagramDictEncoding1.ThreadNumber = 1


SaveData('TimersViscousFing5PercProgMaxTest1T.csv', OutputPort(tTKPersistenceDiagramDictEncoding1, 5))
