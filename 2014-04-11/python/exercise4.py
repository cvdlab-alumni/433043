import urbanImport
from pyplasm import*

def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

#Creo le strade
strada1_vertici = [ [0,0], [150,0], [0,3], [150,3] ];
strada1_num_lati = [range(1,5)] 
strada1_25D = MKPOL([strada1_vertici, strada1_num_lati, None])
strada1 = PROD([strada1_25D, Q(0.5)])
strada1=T([2,3])([16,1])(strada1)

strada2=PROD([strada1_25D, Q(0.5)])
strada2=T([2,3])([38,1])(strada2)

strada3_vertici = [ [0,0], [3,0], [0,150], [3,150] ];
strada3_num_lati = [range(1,5)] 
strada3_25D = MKPOL([strada3_vertici, strada3_num_lati, None])
strada3 = PROD([strada3_25D, Q(0.5)])
strada3=T([1,3])([61,1])(strada3)

strada4=PROD([strada3_25D, Q(0.5)])
strada4=T([1,3])([87,1])(strada4)

strada5_vertici = [ [0,0], [3,0], [0,110], [3,110] ];
strada5_num_lati = [range(1,5)] 
strada5_25D = MKPOL([strada5_vertici, strada5_num_lati, None])
strada5 = PROD([strada5_25D, Q(0.5)])
strada5=T([1,3])([147,1])(strada5)

strada6_vertici = [ [0,0], [87,0], [0,3], [87,3] ];
strada6_num_lati = [range(1,5)] 
strada6_25D = MKPOL([strada6_vertici, strada6_num_lati, None])
strada6 = PROD([strada6_25D, Q(0.5)])
strada6=T([1,2,3])([61,57,1])(strada6)

strada7 = PROD([strada6_25D, Q(0.5)])
strada7=T([1,2,3])([61,85,1])(strada7)

strada8 = PROD([strada6_25D, Q(0.5)])
strada8=T([1,2,3])([61,107,1])(strada8)

strada9_vertici = [ [0,0], [3,0], [0,60], [3,60] ];
strada9_num_lati = [range(1,5)] 
strada9_25D = MKPOL([strada9_vertici, strada9_num_lati, None])
strada9 = PROD([strada9_25D, Q(0.5)])
strada9=T([1,3])([117,1])(strada9)

strada10_vertici = [ [0,0], [3,0], [0,40], [3,40] ];
strada10_num_lati = [range(1,5)] 
strada10_25D = MKPOL([strada10_vertici, strada10_num_lati, None])
strada10 = PROD([strada10_25D, Q(0.5)])
strada10=T([1,3])([33,1])(strada10)

strada11=PROD([strada10_25D, Q(0.5)])
strada11=T(3)(1)(strada11)

strade=STRUCT([strada1,strada2,strada3,strada4,strada5,strada6,strada7,strada8,strada9,strada10,strada11])
strade=COLOR(rgbToPlasmColor([47,47,47]))(strade)

#Creo gli alberi
tronco = CYLINDER([2, (10.0/12)*5])(50)
tronco = COLOR(rgbToPlasmColor([101, 67, 33]))(tronco)
foglie = SPHERE(4)([60,60])
foglie = COLOR(rgbToPlasmColor([85,104,50]))(foglie)

foglie = T(3)(5)(foglie)
albero = STRUCT([tronco,foglie])

T1=T(1)(10)
T2=T(2)(10)
alberi1=STRUCT(NN(5)([T1, STRUCT(NN(2)([T2, albero]))]))
alberi1=T([1,2,3])([90,83,1])(alberi1)

T3=T(1)(10)
alberi2=STRUCT(NN(6)([T3, albero]))
alberi2=T([1,2,3])([-5,45,1])(alberi2)

T4=T(2)(10)
alberi3=STRUCT(NN(10)([T4, albero]))
alberi3=T([1,2,3])([56,45,1])(alberi3)

#Creo un altra tipologia di alberi
tronco1 = CYLINDER([1, (10.0/12)*5])(50)
tronco1 = COLOR(rgbToPlasmColor([101, 67, 33]))(tronco1)
foglie1 = SPHERE(3)([60,60])
foglie1 = COLOR(rgbToPlasmColor([1,50,32]))(foglie1)

foglie1 = T(3)(4)(foglie1)
alberoP = STRUCT([tronco1,foglie1])

TA=T(1)(10)
alberi4=STRUCT(NN(3)([TA, alberoP]))
alberi4=T([1,2,3])([-2,5,1])(alberi4)

alberi5=STRUCT(NN(3)([TA, alberoP]))
alberi5=T([1,2,3])([29,5,1])(alberi5)

TB=T(1)(9)
alberi6=STRUCT(NN(3)([TB, alberoP]))
alberi6=T([1,2,3])([58,5,1])(alberi6)

alberi7=STRUCT(NN(3)([TA, alberoP]))
alberi7=T([1,2,3])([84,5,1])(alberi7)

alberi8=STRUCT(NN(3)([TA, alberoP]))
alberi8=T([1,2,3])([115,5,1])(alberi8)

TR=T(2)(8)
alberi9=STRUCT(NN(3)([TA, STRUCT(NN(2)([TR, alberoP]))]))
alberi9=T([1,2,3])([84,36,1])(alberi9)

tronco2 = CYLINDER([0.5, (10.0/12)*5])(50)
tronco2 = COLOR(rgbToPlasmColor([101, 67, 33]))(tronco2)
foglie2 = CONE([2, (10.0/12)*6])(100)
foglie2 = COLOR(rgbToPlasmColor([85,104,50]))(foglie2)

foglie2 = T(3)(4)(foglie2)
alberoQ = STRUCT([tronco2,foglie2])

TQ=T(2)(5)
alberi10=STRUCT(NN(3)([TA, STRUCT(NN(3)([TQ, alberoQ]))]))
alberi10=T([1,2,3])([115,38,1])(alberi10)

TZ=T(1)(5)
alberi11=STRUCT(NN(5)([TZ, STRUCT(NN(3)([TQ, alberoQ]))]))
alberi11=T([1,2,3])([60,38,1])(alberi11)

tronco3 = CYLINDER([1.5, (10.0/12)*10])(100)
tronco3 = COLOR(rgbToPlasmColor([101, 67, 33]))(tronco3)
foglie3 = SPHERE(5)([60,60])
foglie3 = COLOR(rgbToPlasmColor([128,128,0]))(foglie3)

foglie3 = T(3)(10)(foglie3)
alberoF = STRUCT([tronco3,foglie3])
alberoF=T([1,2,3])([76,96,1])(alberoF)

Tg=T(1)(4)
Th=T(2)(6)
alberi12=STRUCT(NN(2)([Tg, STRUCT(NN(3)([Th, albero]))]))
alberi12=T([1,2,3])([137,17,1])(alberi12)

#Unisco gli  alberi in un unica struttura
alberi=STRUCT([alberi1,alberi2,alberi3,alberi4,alberi5,alberi6,alberi7,alberi8,alberi9,alberi10,
	alberi11,alberoF,alberi12])

#Creo il lampione
palo1 = CYLINDER([0.3, (10.0/12)*6])(100)

palo2 = CYLINDER([0.3, (10.0/12)*4])(100)
palo2=ROTATE([1,3])(-PI/4)(palo2)
palo2=T(3)(4)(palo2)

palo3_vertici = [ [0,0], [2,0], [0,0.8], [2,0.8] ];
palo3_num_lati = [range(1,5)] 
palo3_25D = MKPOL([palo3_vertici, palo3_num_lati, None])
palo3 = PROD([palo3_25D, Q(0.5)])
palo3=T([1,2,3])([2,-0.4,6.1])(palo3)

palo=STRUCT([palo1,palo2,palo3])
palo = COLOR(rgbToPlasmColor([178,178,178]))(palo)

luce= CUBOID([0.5,0.5,0.2])
luce=T([1,2,3])([3.2,-0.2,6])(luce)
luce = COLOR(rgbToPlasmColor([255,255,0]))(luce)

lampione=STRUCT([palo,luce])

T5=T(2)(20)
lampioni1=STRUCT(NN(6)([T5, lampione]))
lampioni1=T([1,2,3])([60,25,1])(lampioni1)

lampione_temp1=ROTATE([1,2])(PI/4)(lampione)

T3=T(1)(16)
lampioni2=STRUCT(NN(9)([T3, lampione_temp1]))
lampioni2=T([1,2,3])([-11,15,1])(lampioni2)


lampione_temp2=ROTATE([1,2])(PI)(lampione)
lampioni3=STRUCT(NN(6)([T5, lampione_temp2]))
lampioni3=T([1,2,3])([90,25,1])(lampioni3)

T3=T(1)(15)
lampioni4=STRUCT(NN(4)([T3, lampione_temp1]))
lampioni4=T([1,2,3])([80,56,1])(lampioni4)

T3=T(1)(16)
lampioni5=STRUCT(NN(9)([T3, lampione_temp1]))
lampioni5=T([1,2,3])([-11,37,1])(lampioni5)

lampioni=STRUCT([lampioni1,lampioni2,lampioni3,lampioni4,lampioni5])

#Creo una fermata dell'autobus
piazzola=CUBOID([4,4,0.1])
piazzola = COLOR(rgbToPlasmColor([123,160,91]))(piazzola)

paloF = CYLINDER([0.2, (10.0/12)*3.5])(100)

paloF1_vertici = [ [0,0], [1,0], [0,0.1], [1,0.1] ];
paloF1_num_lati = [range(1,5)] 
paloF1_25D = MKPOL([paloF1_vertici,paloF1_num_lati, None])
paloF1 = PROD([paloF1_25D, Q(0.2)])
paloF1=T([3])([2.5])(paloF1)

paloF2_vertici = [ [0,0], [1,0], [0,0.1], [1,0.1] ];
paloF2_num_lati = [range(1,5)] 
paloF2_25D = MKPOL([paloF2_vertici,paloF2_num_lati, None])
paloF2 = PROD([paloF2_25D, Q(0.2)])
paloF2=T([3])([2])(paloF2)


tabellone_vertici = [ [0,0], [1.5,0], [0,0.1], [1.5,0.1] ];
tabellone_num_lati = [range(1,5)] 
tabellone_25D = MKPOL([tabellone_vertici,tabellone_num_lati, None])
tabellone = PROD([tabellone_25D, Q(1.8)])
tabellone=T([1,3])([0.5,1])(tabellone)

fermata_t=STRUCT([paloF,paloF1,paloF2,tabellone])
fermata_t = COLOR(rgbToPlasmColor([255,216,0]))(fermata_t)
fermata_t=T([1,2,3])([3,2,0.1])(fermata_t)
fermata=STRUCT([fermata_t,piazzola])

#Aggiungo una panchina
panchina1 = CUBOID([2,1,0.2])
panchina2= CUBOID([2,0.2,1])
panchina2=T(2)(1)(panchina2)
gamba = CYLINDER([0.1, (10.0/12)*0.5])(50)

Ta=T(1)(1.5)
Tb=T(2)(1)
gambe=STRUCT(NN(2)([Ta, STRUCT(NN(2)([Tb, gamba]))]))
gambe=T([1,2])([-1.25,-0.9])(gambe)

panchina_temp=STRUCT([panchina1,panchina2])
panchina_temp=T(3)(0.4)(panchina_temp)

panchina=STRUCT([panchina_temp,gambe])
panchina=ROTATE([1,2])(PI/2)(panchina)
panchina = COLOR(rgbToPlasmColor([145,129,81]))(panchina)
panchina=T([1,2])([1.5,1])(panchina)

fermata1=STRUCT([fermata_t,piazzola,panchina])
fermata1=T([1,2,3])([29,30,1])(fermata1)

fermata2=STRUCT([fermata_t,piazzola,panchina])
fermata2=T([1,2,3])([113,30,1])(fermata2)

fermata3=STRUCT([fermata_t,piazzola,panchina])
fermata3=T([1,2,3])([83,103,1])(fermata3)

fermate=STRUCT([fermata1,fermata2,fermata3])



#Creo la struttura di una macchina
car1=CUBOID([2,1,0.2])

car2_vertici = [ [1.5,0], [1.5,1.5], [2,0.3], [2,0.6] ];
car2_num_lati = [range(1,5)] 
car2_25D = MKPOL([car2_vertici, car2_num_lati, None])
car2 = PROD([car2_25D, Q(1)])
car2=ROTATE([1,3])(PI/2)(car2)
car2=ROTATE([1,2])(PI/2)(car2)
car2=T([1,2,3])([1.8,1,-1.3])(car2)

car_base=STRUCT([car1,car2])
Tcar1 = T(1)(1.6)
Tcar2 = T(2)(0.9)

ruota = CYLINDER([0.2, (10.0/12)*0.2])(50)
ruota=ROTATE([2,3])(PI/2)(ruota)
ruote=STRUCT(NN(2)([Tcar1, STRUCT(NN(2)([Tcar2, ruota]))]))
ruote=T([1,2,3])([-1.4,-0.78,-0.1])(ruote)

parab_vertici = [ [0,0], [0.3,0], [0,0.8], [0.3,0.8] ];
parab_num_lati = [range(1,5)] 
parab_25D = MKPOL([parab_vertici, parab_num_lati, None])
parab = PROD([parab_25D, Q(0.1)])
parab=ROTATE([1,3])(PI/6)(parab)
parab=T([1,2,3])([0.70,0.1,0.32])(parab)

antenna=CYLINDER([0.005, (10.0/12)*0.5])(100)
antenna=T([1,2,3])([1.9,0.2,0.1])(antenna)

finestrino_vertici = [ [0,0], [0.3,0.3], [0.3,0]];
finestrino_num_lati = [range(1,4)] 
finestrino_25D = MKPOL([finestrino_vertici, finestrino_num_lati, None])
finestrino = PROD([finestrino_25D, Q(0.1)])
finestrino=ROTATE([2,3])(PI/2)(finestrino)

T1 = T(2)(0.95)
finestrini=STRUCT(NN(2)([T1, finestrino]))
finestrini=T([1,2,3])([0.90,-0.88,0.32])(finestrini)

luceC = CYLINDER([0.1, (10.0/12)*0.1])(50)
Tluce = T(1)(0.5)
luciC=STRUCT(NN(2)([Tluce, luceC]))
luciC=ROTATE([2,3])(PI/2)(luciC)
luciC=ROTATE([1,2])(PI/2)(luciC)


luciC=T([1,2,3])([-0.01,-0.25,0.1])(luciC)

marmitta = CYLINDER([0.01, (10.0/12)*0.3])(50)
marmitta= ROTATE([1,3])(PI/2)(marmitta)
marmitta=T([1,2,3])([2.1,0.2,0.1])(marmitta)

#Coloro tutto
car_base = COLOR(rgbToPlasmColor([255,0,0]))(car_base)
ruote = COLOR(rgbToPlasmColor([0,0,0]))(ruote)
antenna = COLOR(rgbToPlasmColor([0,0,0]))(antenna)
parab = COLOR(rgbToPlasmColor([70,130,180]))(parab)
finestrini = COLOR(rgbToPlasmColor([70,130,180]))(finestrini)
luciC = COLOR(rgbToPlasmColor([255,255,102]))(luciC)
marmitta = COLOR(rgbToPlasmColor([0,0,0]))(marmitta)

#Creo un insieme di macchine
car=STRUCT([car_base,ruote,parab,antenna,finestrini,luciC,marmitta])
car=T([1,2,3])([80,115,3])(car)
car3=STRUCT([car_base,ruote,parab,antenna,finestrini,luciC,marmitta])
car3=T([1,2,3])([80,117,3])(car3)
car4=STRUCT([car_base,ruote,parab,antenna,finestrini,luciC,marmitta])
car4=T([1,2,3])([80,119,3])(car4)
car5=STRUCT([car_base,ruote,parab,antenna,finestrini,luciC,marmitta])
car5=T([1,2,3])([80,121,3])(car5)
car6=STRUCT([car_base,ruote,parab,antenna,finestrini,luciC,marmitta])
car6=T([1,2,3])([80,123,3])(car6)

#Le posiziono nel parcheggio delll'edificio
cars1=STRUCT([car,car3,car4,car5,car6])
Tcar3=T(1)(5)
cars2=STRUCT(NN(3)([Tcar3, cars1]))
cars2=T(1)(-16)(cars2)

#Creo un'altra tipologia di macchina
car7=CUBOID([2,1,0.2])
car8_vertici = [ [1.5,0], [1.5,1.5], [2,0.3], [2,0.6] ];
car8_num_lati = [range(1,5)] 
car8_25D = MKPOL([car8_vertici, car8_num_lati, None])
car8 = PROD([car8_25D, Q(1)])
car8=ROTATE([1,3])(PI/2)(car8)
car8=ROTATE([1,2])(PI/2)(car8)
car8=T([1,2,3])([1.8,1,-1.3])(car8)

#La duplico
car_base2=STRUCT([car7,car8])
car_base2 = COLOR(rgbToPlasmColor([255,216,0]))(car_base2)
car9=STRUCT([car_base2,ruote,parab,antenna,finestrini,luciC,marmitta])

Tcar4=T(2)(3)
cars3=STRUCT(NN(4)([Tcar4, car9]))
cars3=T([1,2,3])([57.2,20,1.5])(cars3)

#Creo un parcheggio
parcheggio=CUBOID([5,13,0.2])
parcheggio=T([1,2,3])([56.4,21,1])(parcheggio)

#Creo la struttura finale
urban=STRUCT([urbanImport.struttura,strade,alberi,lampioni,fermate,cars2,cars3,parcheggio])


VIEW(urban)