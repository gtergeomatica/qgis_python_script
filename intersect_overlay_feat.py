def unique(f_ov): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in f_ov: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list
#    for x in unique_list: 
#        print(x) 
      

lyr = iface.activeLayer()

#print(feat.id())
#i = 0
f_ov = []
f2_ov = []
f_res = []
f2_res = []
ii = []
for  f in lyr.getSelectedFeatures():
    ii.append(f.id())
    i = f.id()
    #break
#i = ii[0]
print(ii)
#print(i)
for f in lyr.getSelectedFeatures():
    f_ov.append(f["P_CAMPAGNA"])
    f_res.append(f["RISOLUZ_RA"])
    i = f.id()
#    if f.id() == i:
    for f2 in lyr.getSelectedFeatures():
        #f_ov.append(f["P_CAMPAGNA"]) #qui carico tutto le campagna che seleziono
        #f_res.append(f["RISOLUZ_RA"])
        if f2.id() > i:
            if f.geometry().intersects(f2.geometry()):
                intersection = f.geometry().intersection(f2.geometry())
                if intersection.area() > 0:
                    f2_ov.append(f["P_CAMPAGNA"]) #qui carico tutto le campagna che seleziono e che si sovrappongono fra loro
                    f2_ov.append(f2["P_CAMPAGNA"])
                    f2_res.append(f["RISOLUZ_RA"]) #qui carico tutto le campagna che seleziono e che si sovrappongono fra loro
                    #f2_res.append(f2["RISOLUZ_RA"])
                else:
                    print('sonoadiacenti')
    #i = i+1
#   else:

print(unique(f_ov))
print(f_res)
#print(f2_res)
#for i in unique(f_ov):
#    print(i)
print(len(unique(f_ov)))
if len(unique(f_ov)) == 1:
    print('fai tutto')
elif len(unique(f_ov)) > 1 and len(f2_ov) == 0:
    print('check la risoluzione')
elif len(unique(f_ov)) > 1 and len(f2_ov) > 1:
    print('comparirà il log')
#print(f_ov3)
print(max(f_res))
#print(unique(f_ov3))

for o in unique(f_ov):
    print(o)
    if o in f["P_CAMPAGNA"]:
        print('cè')
    else:
        print('non cè')
#        print(o)
#        print(f["RISOLUZ_RA"])
#        print(f["ANNO"])

#for i in unique(f_ov):
##    for r in unique(f_res):
#    print("CAMPAGNA: {}".format(i) + " - " + "CAMPAGNA: {}".format(f_res[i]))

#zip = zip(unique(f_ov), unique(f_res))
#for c in zip:
#    print(c)
#   for r in len(unique(f_res)):
#      print("CAMPAGNA: {}".format(c) + " - " + "RISOLUZIONE: {}".format(r))