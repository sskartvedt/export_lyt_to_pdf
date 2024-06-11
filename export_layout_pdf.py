import arcpy
#3.6.6

aprx = arcpy.mp.ArcGISProject(r"G:\!GIS_Drive\Projects\FY2021\Mori_Memorial\ArcPro\Mori_Memorial.aprx")
export_dir = r"G:\!GIS_Drive\Projects\FY2021\Mori_Memorial\Take_To_Field\pdfs"

'''
for m in aprx.listMaps():
    print("Map: " + m.name)
    for lyr in m.listLayers():
        print("  " + lyr.name)

print("Layouts:")
for lyt in aprx.listLayouts():
    print("  {0} ({1} x {2} {3})".format(lyt.name, lyt.pageHeight, lyt.pageWidth, lyt.pageUnits))
'''    

print ("done")

for lyt in aprx.listLayouts():
    lyt.exportToPDF(export_dir + "\\" + lyt.name + ".pdf", resolution = 150)
