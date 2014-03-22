#Creazione Struttura solid_model_3D


from pyplasm import*

#Creo una funzione per convertire colori RGB in Plasm
def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]


#Creazione della base. Approssimata 69x33
base1_vertici = [ [0,0], [0,69], [33,69], [33,0] ];
base1_num_lati = [range(1,5)] 
base1_2D = MKPOL([base1_vertici, base1_num_lati, None])

#Porto in 2,5D
floor1 = PROD([base1_2D, Q(1)])

#Coloro 
floor1 = COLOR(rgbToPlasmColor([255,255,255]))(floor1)


#Creo la seconda base.Approssimata 68x32
base2_vertici = [ [0,0], [0,68], [32,68], [32,0] ];
base2_num_lati = [range(1,5)] 
base2_2D = MKPOL([base2_vertici, base2_num_lati, None])

#Porto in 2,5D
floor2 = PROD([base2_2D, Q(1)])

#Coloro 
floor2 = COLOR(rgbToPlasmColor([147,147,147]))(floor2)


#Creo la terza base su cui poggeranno le colonne: 68x30
base3_vertici = [ [0,0], [0,67], [31,67], [31,0] ];
base3_num_lati = [range(1,5)] 
base3_2D = MKPOL([base3_vertici, base3_num_lati, None])

#Porto in 2,5D
floor3 = PROD([base3_2D, Q(1)])

#Coloro 
floor3 = COLOR(rgbToPlasmColor([95,95,95]))(floor3)


#Creo la la  base posizionata sotto il tetto
base4_vertici =  [ [0,0], [0,67], [31,67], [31,0] ]; 
base4_num_lati = [range(1,5)] 
base4_2D = MKPOL([base4_vertici, base4_num_lati, None])

#Porto in 2,5D
floor4 = PROD([base4_2D, Q(3)])

#Coloro 
floor4 = COLOR(rgbToPlasmColor([128,128,128]))(floor4)


#Creo il tetto.Approssimato 69x33x5
from pyplasm import*
tetto_vertici = [ [0,0], [33,0], [16,5], ];
tetto_num_lati = [range(1,4)] 
tetto_2D = MKPOL([tetto_vertici, tetto_num_lati, None])

#Porto in 2,5D
floor5 = PROD([tetto_2D, Q(69)])


#Assemblo le 3 basi e il tetto
floor2=T([1,2,3])([0.5,0.5,1])(floor2)
floor3=T([1,2,3])([1,1,2])(floor3)
floor4=T([1,2,3])([1,1,15])(floor4)


floor5=MAP([S1,S3,S2])(floor5)
floor5=T([3])([18])(floor5)

#Coloro il tetto dopo la traslazione.
floor5 = COLOR(rgbToPlasmColor([147,147,147]))(floor5)

#Creo la struttura 2,5D
Orizontal_model=STRUCT([floor1,floor2,floor3,floor4,floor5])

#Creo una funzione per la circonferenza delle colonne esterne
def base(p): 
 u,v = p
 return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(2*PI)(20), INTERVALS(1)(3)])

#Creo una funzione per la circonferenza delle colonne interne
def base2(p): 
 u,v = p
 return [(v/2)*COS(u), (v/2)*SIN(u)]

 #Creo una colonna esterna
base_colonna1=MAP(base)(domain2D) 
base_colonna=PROD([base_colonna1,Q(11)])

#Creo una colonna interna
base_colonnina1=MAP(base2)(domain2D)
base_colonnina=PROD([base_colonnina1,Q(11.5)])

#Creo il blocchetto da mettere sopra la colonna esterna
blocchetto_coords = [ [0,0], [0,2.5], [2.5,2.5], [2.5,0] ];
blocchetto_num_lati = [range(1,5)] 
blocchetto_2D = MKPOL([blocchetto_coords, blocchetto_num_lati, None])
blocchetto = PROD([blocchetto_2D, Q(1)])

#Posiziono il blocchetto della colonna esterna
blocchetto=T([1,2,3])([-1.25,-1.25,11])(blocchetto)

#Creo la struttura con colonna e blocchetto
colonna=STRUCT([blocchetto,base_colonna])

#Creo il blocchetto della colonna interna
blocchetto2_coords = [ [0,0], [0,1.5], [1.5,1.5], [1.5,0] ];
blocchetto2_num_lati = [range(1,5)] 
blocchetto2_2D = MKPOL([blocchetto2_coords, blocchetto2_num_lati, None])
blocchetto2 = PROD([blocchetto2_2D, Q(0.5)])

#Posiziono il blocchetto sulla colonna interna
blocchetto2=T([1,2,3])([-0.80,-0.80,11.5])(blocchetto2)

#Creo la struttura con colonna interna e blocchetto
colonna_int=STRUCT([blocchetto2,base_colonnina])

#Traslo la colonna
colonna=T([1,2,3])([2.2,2.2,3])(colonna)

#Traslo la colonna interna
colonna_int=T([1,2,3])([8.2,8.2,3])(colonna_int)

#Creo le colonne frontali e le posiziono
colonne_temp=[T(1)(4),colonna]
colonne_frontali=STRUCT(NN(8)(colonne_temp))
colonne_frontali=T(1)(-3.80)(colonne_frontali)
#Coloro
colonne_frontali = COLOR(rgbToPlasmColor([95,95,95]))(colonne_frontali)

#Creo le colonne interne frontali
colonne_int_temp=[T(1)(4),colonna_int]
colonne_int_frontali=STRUCT(NN(6)(colonne_int_temp))
colonne_int_frontali=T(1)(-5.80)(colonne_int_frontali)
#Coloro
colonne_int_frontali = COLOR(rgbToPlasmColor([255,255,255]))(colonne_int_frontali)


#Creo le mura interne frontali
mura4_vertici = [ [0,0], [1,0], [0,5], [1,5] ];
mura4_num_lati = [range(1,5)] 
mura4_2D = MKPOL([mura4_vertici, mura4_num_lati, None])
mura4 = PROD([mura4_2D, Q(12)])

mura4=T([1,2,3])([20,-26.5,3])(mura4)
mura4=ROTATE([1,2])(PI/2)(mura4)
mura4 = COLOR(rgbToPlasmColor([178,178,178]))(mura4)

mura5_vertici = [ [1,1], [2,1], [1,6], [2,6] ];
mura5_num_lati = [range(1,5)] 
mura5_2D = MKPOL([mura5_vertici, mura5_num_lati, None])
mura5 = PROD([mura5_2D, Q(12)])

mura5=T([1,2,3])([19,-12.5,3])(mura5)
mura5=ROTATE([1,2])(PI/2)(mura5)
mura5 = COLOR(rgbToPlasmColor([178,178,178]))(mura5)

mura_frontali=STRUCT([mura4,mura5])

#Creo la struttua frontale
north=STRUCT([colonne_frontali,colonne_int_frontali,mura_frontali])

#Creo le colonne posteriori e le posiziono
colonne_posteriori=T(2)(64)(colonne_frontali)
#Coloro
colonne_posteriori = COLOR(rgbToPlasmColor([95,95,95]))(colonne_posteriori)

#Creo le colonne interne posteriori
colonne_int_posteriori=T(2)(52)(colonne_int_frontali)

#Creo le mura interne posteriori
mura3_vertici = [ [0,0], [1,0], [0,20], [1,20] ];
mura3_num_lati = [range(1,5)] 
mura3_2D = MKPOL([mura3_vertici, mura3_num_lati, None])
mura3 = PROD([mura3_2D, Q(12)])

mura3=T([1,2,3])([50,-26.5,3])(mura3)
mura3=ROTATE([1,2])(PI/2)(mura3)
mura3 = COLOR(rgbToPlasmColor([178,178,178]))(mura3)

#Creo la struttura posteriore
sud=STRUCT([colonne_posteriori,colonne_int_posteriori,mura3])

#Creo le colonne esterne sx e le posiziono
colonne_sx=STRUCT(NN(15)(colonne_temp))
colonne_sx=ROTATE([1,2])(PI/2)(colonne_sx)
colonne_sx=T(1)(4.3)(colonne_sx)
#Coloro
colonne_sx = COLOR(rgbToPlasmColor([95,95,95]))(colonne_sx)

#Creo le mura sx e le posiziono
mura1_vertici = [ [0,0], [1,0], [0,45], [1,45] ];
mura1_num_lati = [range(1,5)] 
mura1_2D = MKPOL([mura1_vertici, mura1_num_lati, None])
mura1 = PROD([mura1_2D, Q(12)])
mura1=T([1,2,3])([6.2,11.2,3])(mura1)

#Coloro
mura1 = COLOR(rgbToPlasmColor([178,178,178]))(mura1)

#Creo la struttura sx
ovest=STRUCT([colonne_sx,mura1])

#Creo le colonne esterne dx e le posiziono
colonne_dx=STRUCT(NN(15)(colonne_temp))
colonne_dx=ROTATE([1,2])(PI/2)(colonne_dx)
colonne_dx=T(1)(32.8)(colonne_dx)
#Coloro
colonne_dx = COLOR(rgbToPlasmColor([95,95,95]))(colonne_dx)

#Creo le mura dx e le posiziono
mura2_vertici = [ [5,0], [6,0], [5,45], [6,45] ];
mura2_num_lati = [range(1,5)] 
mura2_2D = MKPOL([mura2_vertici, mura2_num_lati, None])
mura2 = PROD([mura2_2D, Q(12)])

mura2=T([1,2,3])([21,11.2,3])(mura2)
#Coloro
mura2 = COLOR(rgbToPlasmColor([178,178,178]))(mura2)

#Creo la struttura sx
est=STRUCT([colonne_dx,mura2])


#Creo la struttura finale solida 3D
Vertical_model=STRUCT([north,sud,ovest,est])
solid_model_3D=STRUCT([Orizontal_model,Vertical_model])
VIEW(solid_model_3D)

