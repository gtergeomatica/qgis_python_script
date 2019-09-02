lyr = iface.activeLayer()
show_values = []
filter = 'MATTM'
yfilter = 2010
#values = [feat['P_CAMPAGNA'] for feat in lyr.getFeatures() if feat['ENTE'] == filter]
values = [feat['P_CAMPAGNA'] for feat in lyr.getFeatures() if feat['ENTE'] == filter if feat['ANNO'] == yfilter]

print(set(values))
list = set(values)
for i in list:
    if i != '':
        show_values.append(i)
        
print(show_values)
