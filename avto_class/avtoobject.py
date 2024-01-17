from avto import Avto,Avtosalon

avto1 = Avto("Cobalt","Oq","avtomat",10000,2021)
avto2 = Avto("Gentra","Qora","mexanik",9000,2018)
avto3 = Avto("Malibu","Oq","avtomat",20000,2022)
avto4 = Avto("Kaptiva","Qora","avtomat",19000,2022)
avto5 = Avto("Damas","Oq","mexanik",7000,2020)


avtosalon = Avtosalon("Shox","Urganch shahri")

print(avtosalon.get_info())

avtosalon(avto1,avto2,avto3,avto4,avto5)
print(avtosalon.get_info())

print(avtosalon[2])

avtosalon[1] = 'Tracker'
print(avtosalon.get_info())

