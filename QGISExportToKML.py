#ExportToKML.py
from qgis.utils import iface
import os, string

print "***\nExport to KML\nSusan Jones\n***"

#your code here
sf = r"D:\TMP\SCATS GPS Coordinate\SCATS GPS Coordinate\Arterials GPS.shp"
path = r"D:\TMP\SCATS GPS Coordinate\SCATS GPS Coordinate"

#export To KML File
files = os.listdir(path)
for f in files:
    if f.find(".shp") > -1 and f.find(".xml")  == -1:

        #KML file Management
        kml = path + os.path.sep  + f.replace(".shp", ".kml")
        if os.path.exists(kml):
            os.remove(kml)
        sf = path + os.path.sep + f

#        add Layer to Map
        layer = iface.addVectorLayer(sf, f, "ogr")
        
        #convert to kml
        writerToKML = QgsVectorFileWriter.writeAsVectorFormat(layer , kml,  "utf-8",  None,  "KML")
        layer = iface.addVectorLayer(kml, f.replace(".shp", ".kml"), "ogr")

#t.refresh() #refrsh the lMap

print "\nLoop through layers"
t = iface.mapCanvas()
layerList = []
layers = iface.legendInterface().layers()
print str(len(layers)) + " layers"
for layer in layers:
    if layer.type() == QgsMapLayer.VectorLayer and string.find(layer.name(),"shp") > -1:
        layerList.append(layer.id())

#remove All Map Layers from MapLayerRegistry
#QgsMapLayerRegistry.instance().removeAllMapLayers()
QgsMapLayerRegistry.instance().removeMapLayers(layerList)

#refresh The Map
t.refresh() #refrsh the lMap
  
#all Done
print "\ncompleted\n***"