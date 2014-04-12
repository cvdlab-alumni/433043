import partenoneImport 
from pyplasm import*

#Creo una funzione per convertire colori RGB in Plasm
def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

base_vertici = [ [5,0], [45,0], [0,10], [50,10] ];
base_num_lati = [range(1,5)] 
base_25D = MKPOL([base_vertici, base_num_lati, None])
base = PROD([base_25D, Q(90)])
base=ROTATE([2,3])(-PI/2)(base)
base=T(3)(11)(base)
base=COLOR(rgbToPlasmColor([3,192,60]))(base)
partenoneImport.solid_model_3D=T([1,2,3])([8,10,11])(partenoneImport.solid_model_3D)


prato_vertici = [ [0,0], [150,0], [0,150], [150,150] ];
prato_num_lati = [range(1,5)] 
prato_25D = MKPOL([prato_vertici, prato_num_lati, None])
prato = PROD([prato_25D, Q(1)])
prato=COLOR(rgbToPlasmColor([34,139,34]))(prato)
partenone=STRUCT([partenoneImport.solid_model_3D,base])
partenone=T([1,2])([1,53])(partenone)




#Creo un primo complesso di case

#Creo i vertici per le strutture 2D
base_vertici = [ [0,0], [0,4], [4,4], [4,0] ];
tetto_vertici = [ [-1,4], [5,4], [3,6] ];
base_num_lati = [range(1,5)] #genera da 1 a 4 (5 escluso)
tetto_num_lati = [range(1,4)]
base_2D = MKPOL([base_vertici, base_num_lati, None])
tetto = MKPOL([tetto_vertici, tetto_num_lati, None])

#Creo porte e finestre
porta_vertici = [ [1.5,0], [2.5,0], [1.5,2], [2.5,2] ]
porta_num_lati = [range(1,5)]
porta = MKPOL([porta_vertici, porta_num_lati, None])


finestra1 = CUBOID([0.75,0.5])
finestra1 = T([1,2])([0.5,2.5])(finestra1)
finestra2 = CUBOID([0.75,0.5])
finestra2 = T([1,2])([2.75,2.5])(finestra2)

#Renderizzo in 3D
base = PROD([base_2D, Q(4)])
tetto = PROD([tetto, Q(4)])

porta = PROD([porta,Q(0.5)])
finestra1 = PROD([finestra1,Q(0.5)])
finestra2 = PROD([finestra2,Q(0.5)])

#Svuoto l'interno
interno = CUBOID([3.5,3.5,3.5])
interno = T([1,2,3])([0.25,0.25,0.25])(interno)
base = DIFFERENCE([base,interno])

#Assemblo nella casa
base = DIFFERENCE([base,porta,finestra1,finestra2])

#Coloro
tetto = COLOR(rgbToPlasmColor([178,34,34]))(tetto)
base = COLOR(rgbToPlasmColor([255,229,180]))(base)

casa = STRUCT([base,tetto])

#Inserisco la porta (e sposto la casa)
casa = T(3)(1)(casa)
porta_aperta = CUBOID([0.1,2,1])
porta_aperta = T(1)(1.5)(porta_aperta)
porta_aperta = COLOR(rgbToPlasmColor([150, 75, 0]))(porta_aperta)
casa = STRUCT([casa,porta_aperta])

#Traslo la casa
casa = T([1,2,3])([9,0.1,5])(casa)
prato1 = CUBOID([15,0.1,15])
prato1= COLOR(rgbToPlasmColor([150,75,0]))(prato1)

#Creo gli alberi
#Creo 3 albero
tronco = CYLINDER([1, (10.0/12)*5])(50)
tronco = COLOR(rgbToPlasmColor([101, 67, 33]))(tronco)
foglie = SPHERE(2)([60,60])
foglie = COLOR(rgbToPlasmColor([85,104,50]))(foglie)

foglie = T(3)(3)(foglie)
albero = STRUCT([tronco,foglie])
albero2= STRUCT([tronco,foglie])
albero3= STRUCT([tronco,foglie])

#Posiziono gli alberi
albero = T([1,2])([4,-2])(albero)
albero = ROTATE([2,3])(-PI/2)(albero)

albero2 = T([1,2])([4,-7])(albero2)
albero2 = ROTATE([2,3])(-PI/2)(albero2)

albero3 = T([1,2])([4,-12])(albero3)
albero3 = ROTATE([2,3])(-PI/2)(albero3)

villa = STRUCT([casa,prato1,albero,albero2,albero3])
Tc = T(1)(13)
Tz = T(3)(10)
#Ripezione della casa. Complesso di case#
complesso=STRUCT(NN(2)([Tz, STRUCT(NN(4)([Tc, villa]))]))
complesso=ROTATE([2,3])(PI/2)(complesso)
complesso=ROTATE([1,2])(PI)(complesso)
complesso=T([1,2,3])([158,50,1])(complesso)


#Creo un secondo complesso

piano_vertici = [ [0,0], [60,0], [0,40], [60,40] ];
piano_num_lati = [range(1,5)] 
piano_25D = MKPOL([piano_vertici, piano_num_lati, None])
piano = PROD([piano_25D, Q(0.5)])
piano=T(1)(-20)(piano)

piano = COLOR(rgbToPlasmColor([192,192,192]))(piano)

base_vertici = [ [0,0], [10,0], [0,10], [10,10] ];
base_num_lati = [range(1,5)] 
base_25D = MKPOL([base_vertici, base_num_lati, None])
base = PROD([base_25D, Q(30)])
base = COLOR(rgbToPlasmColor([255,36,0]))(base)


porta_vertici = [ [1.5,0], [2.5,0], [1.5,2], [2.5,2] ]
porta_num_lati = [range(1,5)]
porta1 = MKPOL([porta_vertici, porta_num_lati, None])
porta2 = MKPOL([porta_vertici, porta_num_lati, None])
porta1 = COLOR(rgbToPlasmColor([70,130,180]))(porta1)
porta2 = COLOR(rgbToPlasmColor([70,130,180]))(porta2)
porta1=ROTATE([2,3])(PI/2)(porta1)
porta2=ROTATE([2,3])(PI/2)(porta2)
porta1=T(1)(1)(porta1)
porta2=T(1)(5)(porta2)

fin1 = CUBOID([2,0.5])
fin1 = T([1,2])([0.5,2.5])(fin1)
fin1=ROTATE([2,3])(PI/2)(fin1)

Tc = T(1)(3)
Tz = T(3)(5)

fin=STRUCT(NN(5)([Tz, STRUCT(NN(2)([Tc, fin1]))]))
fin=T(1)(-1)(fin)
fin= COLOR(rgbToPlasmColor([28,57,187]))(fin)


palazzo_temp=STRUCT([porta1,porta2,base,fin])
palazzo_temp=T([1,2,3])([2.5,2.5,0.5])(palazzo_temp)

T1=T(1)(20)
T2=T(2)(20)
complesso2_temp=STRUCT(NN(3)([T1, STRUCT(NN(2)([T2, palazzo_temp]))]))
complesso2_temp=T([1,2,3])([-37,-18,1])(complesso2_temp)
complesso2=STRUCT([complesso2_temp,piano])
complesso2=T([1,2,3])([110,110,1])(complesso2)

#Creo un complesso di ville


#Creo la pavimentazione
x_plinti1=QUOTE([2,-2]*4)
y_plinti1=QUOTE([2,-2]*4)
plinti1= INSR(PROD)([x_plinti1,y_plinti1,Q(0.2)])
plinti1 = COLOR(rgbToPlasmColor([255,99,71]))(plinti1)
x_plinti2=QUOTE([-2,2]*4)
y_plinti2=QUOTE([2,-2]*4)
plinti2= INSR(PROD)([x_plinti2,y_plinti2,Q(0.2)])
plinti2 = COLOR(rgbToPlasmColor([255,140,105]))(plinti2)
plintiT=STRUCT([plinti1,plinti2])
x_plinti3=QUOTE([-2,2]*4)
y_plinti3=QUOTE([-2,2]*4)
plinti3= INSR(PROD)([x_plinti3,y_plinti3,Q(0.2)])
plinti3 = COLOR(rgbToPlasmColor([255,99,71]))(plinti3)
x_plinti4=QUOTE([2,-2]*4)
y_plinti4=QUOTE([-2,2]*4)
plinti4= INSR(PROD)([x_plinti4,y_plinti4,Q(0.2)])
plinti4 = COLOR(rgbToPlasmColor([255,140,105]))(plinti4)

plinti5=STRUCT([plinti3,plinti4])

base=STRUCT([plintiT,plinti5])

#Creo la struttura base della casa
casa_vertici = [ [0,0], [10,0], [0,5], [10,5] ];
casa_num_lati = [range(1,5)]
casa_2D = MKPOL([casa_vertici, casa_num_lati, None])
casa = PROD([casa_2D, Q(3)])
casa=COLOR(rgbToPlasmColor([218,112,214]))(casa)



#Creo il tetto principale
tetto_vertici = [ [-1,-1], [11,-1], [5,3] ];
tetto_num_lati = [range(1,4)]
tetto_2D= MKPOL([tetto_vertici, tetto_num_lati, None])
tetto = PROD([tetto_2D, Q(5)])

#Lo posiziono sopra la casa
tetto=ROTATE([2,3])(PI/2)(tetto)
tetto=T([2,3])([5,4])(tetto)
tetto=COLOR(rgbToPlasmColor([255,0,0]))(tetto)

#Creo la struttura della prima casa
casa= STRUCT([casa,tetto])


#Creo la mansarda
mansarda_vertici = [ [0,0], [2,0], [0,2], [2,2] ];
mansarda_num_lati = [range(1,5)]
mansarda_2D = MKPOL([mansarda_vertici, mansarda_num_lati, None])
mansarda = PROD([mansarda_2D, Q(2)])
mansarda=COLOR(rgbToPlasmColor([218,112,214]))(mansarda)
#La posiziono sopra la prima casa
#mansarda=T([3])([10])(mansarda)


#Creo il tetto della mansarda
tettoM_vertici = [ [0,0], [3,0], [1.5,1] ];
tettoM_num_lati = [range(1,4)]
tettoM_2D= MKPOL([tettoM_vertici, tettoM_num_lati, None])
tettoM = PROD([tettoM_2D, Q(2)])

#Lo posiziono sopra la mansarda
tettoM=ROTATE([2,3])(PI/2)(tettoM)
tettoM=T([1,2,3])([-0.5,2,2])(tettoM)
#tettoM=T([3])([15])(tettoM)
tettoM=COLOR(rgbToPlasmColor([255,0,0]))(tettoM)

#Creo la struttura della mansarda
mansarda=STRUCT([mansarda,tettoM])
mansarda=T([1,2,3])([7,1.5,4.3])(mansarda)
#Creo la villa
villa=STRUCT([casa,mansarda])

#La sposto prima di metterla sul piastrellato
villa=T(2)(11)(villa)


#Creo le finestre
fin1 = CUBOID([1,1])
fin1=ROTATE([2,3])(PI/2)(fin1)
fin1 = T([1,2,3])([7.5,12.4,5])(fin1)
fin1=COLOR(rgbToPlasmColor([18,10,143]))(fin1)

T1 = T(1)(5)

fin2=STRUCT(NN(2)([T1, fin1]))
fin2= COLOR(rgbToPlasmColor([28,57,187]))(fin2)
fin2=T([1,2,3])([-10.5,-1.5,-3])(fin2)


#Creo la porta
#Creo le finestre
port1 = CUBOID([1,2])
port1=ROTATE([2,3])(PI/2)(port1)
port1 = T([1,2,3])([4.5,10.7,0.5])(port1)
port1=COLOR(rgbToPlasmColor([128,0,0]))(port1)

#La metto sul piastrellato
villa=STRUCT([villa,base,fin1,fin2,port1])



#sposto la villa completa sul giardiano in fondo
villa=T(3)(0.3)(villa)
villa=T(2)(18)(villa)

T3=T(1)(28)
complessoVille=STRUCT(NN(5)([T3, villa]))
complessoVille=T([1,2,3])([-19,2,1])(complessoVille)

#Creo un altro edificio
base2_vertici = [ [0,0], [20,0], [0,20], [20,20] ];
base2_num_lati = [range(1,5)] 
base2_25D = MKPOL([base2_vertici, base2_num_lati, None])
base2 = PROD([base2_25D, Q(15)])
base2 = COLOR(rgbToPlasmColor([65,105,225]))(base2)

porta_vertici = [ [1.5,0], [2.5,0], [1.5,2], [2.5,2] ]
porta_num_lati = [range(1,5)]
porta1 = MKPOL([porta_vertici, porta_num_lati, None])
porta1 = COLOR(rgbToPlasmColor([205,127,50]))(porta1)
porta1=ROTATE([2,3])(PI/2)(porta1)


T3=T(1)(4)
porta3=STRUCT(NN(3)([T3, porta1]))
porta3=T([1,2])([0.5,-0.1])(porta3)

fin2 = CUBOID([2,2])
fin2 = T([1,2])([-0.8,2.3])(fin2)
fin2=ROTATE([2,3])(PI/2)(fin2)

Tc = T(1)(3)
Tz = T(3)(5)

fin3=STRUCT(NN(2)([Tz, STRUCT(NN(6)([Tc, fin2]))]))
fin3=T(1)(-1)(fin3)
fin3= COLOR(rgbToPlasmColor([255,255,102]))(fin3)
fin3=T(2)(-0.1)(fin3)

piano2_vertici = [ [0,0], [22,0], [0,40], [22,40] ];
piano2_num_lati = [range(1,5)] 
piano2_25D = MKPOL([piano2_vertici, piano2_num_lati, None])
piano2 = PROD([piano2_25D, Q(1)])
piano2 = COLOR(rgbToPlasmColor([117,102,63]))(piano2)

edificio_temp=STRUCT([porta3,base2,fin3])
edificio_temp=T([1,2,3])([1,20,1])(edificio_temp)
edificio=STRUCT([edificio_temp,piano2])
edificio=T([1,2,3])([64.5,110,1])(edificio)



struttura=STRUCT([partenone,prato,complesso,complesso2,complessoVille,edificio])

VIEW(struttura)