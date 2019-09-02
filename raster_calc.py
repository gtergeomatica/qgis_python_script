#r1 = QgsProject.instance().mapLayersByName('D46521204_0101_DSMFirst.asc')[0]
#r2 = QgsProject.instance().mapLayersByName('D46521204_0101_DTM.asc')[0]

#r1 = QgsRasterLayer('C:/Users/roberta\Documents\DSM_CORTINA_2010_CONTRATTO_140_20190503T094658Z_001\DSM_CORTINA_2010_CONTRATTO_140', 'D46521204_0101_DSMFirst.asc')
#r2 = QgsRasterLayer('C:/Users/roberta\Documents\DTM_CORTINA_2010_CONTRATTO_140', 'D46521204_0101_DTM.asc')

#print(str(r1.name()))
#print(str(r2.name()))

r1 = 'C:/Users/roberta\Documents\DSM_CORTINA_2010_CONTRATTO_140_20190503T094658Z_001\DSM_CORTINA_2010_CONTRATTO_140\D46521204_0101_DSMFirst.asc'

entries = []

ras1 = QgsRasterCalculatorEntry()
ras1.ref = 'D46521204_0101_DSMFirst.asc@1'
ras1.raster = r1
ras1.bandNumber = 1
entries.append(ras1)
print(ras1)
#ras2 = QgsRasterCalculatorEntry()
#ras2.ref = 'D46521204_0101_DTM.asc@1'
#ras2.raster = r2
#ras2.bandNumber = 1
#entries.append(ras2)
#
calc = QgsRasterCalculator('D46521204_0101_DSMFirst.asc@1 > 2000', 'C:/Users/roberta/Desktop/testchm2.tif', 'GTiff', r1.extent(), r1.width(), r1.height(), entries)
calc.processCalculation()

print(calc)

print('fatto!')