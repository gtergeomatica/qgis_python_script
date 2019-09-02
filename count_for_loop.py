lyr = iface.activeLayer()

print(lyr.selectedFeatureCount())
#count = 0
#for f in lyr.getSelectedFeatures():
#    print('do something')
#    count += 1
#    print(count)

for id,f in enumerate(lyr.getSelectedFeatures()):
    print('do something')
    print(f["fid"])
#    count += 1
    print(id+1)