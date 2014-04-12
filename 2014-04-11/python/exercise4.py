import urbanImport
from pyplasm import*

def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

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

alberi=STRUCT([alberi1,alberi2,alberi3,alberi4,alberi5,alberi6,alberi7,alberi8,alberi9,alberi10,alberi11,alberoF])

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

urban=STRUCT([urbanImport.struttura,strade,alberi,lampioni1,lampioni2,lampioni3,lampioni4])


VIEW(urban)