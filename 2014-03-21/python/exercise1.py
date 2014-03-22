from pyplasm import*

#Creo una funzione per convertire colori RGB in Plasm
def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]


#CREAZIONE PARTE ANTERIORE
#Creazione della base frontale
base1_vertici = [ [0,0], [33,0], [0,1], [33,1] ];
base1_num_lati = [range(1,5)] 
base1_2D = MKPOL([base1_vertici, base1_num_lati, None])


#Coloro 
base1_2D = COLOR(rgbToPlasmColor([210,210,210]))(base1_2D)


#Creo la seconda base frontale
base2_vertici = [ [0,1], [33,1], [0,2], [33,2] ];
base2_num_lati = [range(1,5)] 
base2_2D = MKPOL([base2_vertici, base2_num_lati, None])


#Coloro 
base2_2D = COLOR(rgbToPlasmColor([147,147,147]))(base2_2D)


#Creo la terza base su cui poggeranno le colonne
base3_vertici = [ [0,2], [33,2], [0,3], [33,3] ];
base3_num_lati = [range(1,5)] 
base3_2D = MKPOL([base3_vertici, base3_num_lati, None])


#Coloro 
base3_2D = COLOR(rgbToPlasmColor([95,95,95]))(base3_2D)


#Creo la la  base posizionata sotto il tetto frontale
base4_vertici =  [ [0,12], [33,12], [0,13], [33,13] ]; 
base4_num_lati = [range(1,5)] 
base4_2D = MKPOL([base4_vertici, base4_num_lati, None])

#Coloro %	
base4_2D = COLOR(rgbToPlasmColor([128,128,128]))(base4_2D)


#Creo il tetto frontale
tetto1_vertici = [ [0,13], [33,13], [16.5,22.7], ];
tetto1_num_lati = [range(1,4)] 
tetto1_2D = MKPOL([tetto1_vertici, tetto1_num_lati, None])

#Coloro
tetto1_2D = COLOR(rgbToPlasmColor([147,147,147]))(tetto1_2D)

#Creo la struttura 
floor1=STRUCT([base1_2D,base2_2D,base3_2D,base4_2D,tetto1_2D])



#CREAZIONE PARTE POSTERIORE

#Creazione della base posteriore
base5_2D = MKPOL([base1_vertici, base1_num_lati, None])


#Coloro 
base5_2D = COLOR(rgbToPlasmColor([210,210,210]))(base5_2D)


#Creo la seconda base posteriore
base6_2D = MKPOL([base2_vertici, base2_num_lati, None])


#Coloro 
base6_2D = COLOR(rgbToPlasmColor([147,147,147]))(base6_2D)


#Creo la terza base su cui poggeranno le colonne posteriori
base7_2D = MKPOL([base3_vertici, base3_num_lati, None])


#Coloro 
base7_2D = COLOR(rgbToPlasmColor([95,95,95]))(base7_2D)


#Creo la la  base posizionata sotto il tetto posteriore 
base8_2D = MKPOL([base4_vertici, base4_num_lati, None])

#Coloro 
base8_2D = COLOR(rgbToPlasmColor([128,128,128]))(base8_2D)


#Creo il tetto posteriore
tetto2_2D = MKPOL([tetto1_vertici, tetto1_num_lati, None])

#Coloro
tetto2_2D = COLOR(rgbToPlasmColor([147,147,147]))(tetto2_2D)


#Creo la struttura posteriore
floor2=STRUCT([base5_2D,base6_2D,base7_2D,base8_2D,tetto2_2D])


#CREO LA PARTE SX

#Creo la prima base sx
base1sx_vertici = [ [0,0], [69,0], [69,1], [0,1] ];
base1sx_num_lati = [range(1,5)] 
base1sx_2D = MKPOL([base1sx_vertici, base1sx_num_lati, None])


#Coloro Grigio 
base1sx_2D = COLOR(rgbToPlasmColor([210,210,210]))(base1sx_2D)


#Creo la seconda base sx
base2sx_vertici = [ [0,1], [69,1], [69,2], [0,2] ];
base2sx_num_lati = [range(1,5)] 
base2sx_2D = MKPOL([base2sx_vertici, base2sx_num_lati, None])


#Coloro 
base2sx_2D = COLOR(rgbToPlasmColor([147,147,147]))(base2sx_2D)


#Creo la terza base su cui poggeranno le colonne di 
base3sx_vertici = [ [0,2], [69,2], [69,3], [0,3] ];
base3sx_num_lati = [range(1,5)] 
base3sx_2D = MKPOL([base3sx_vertici, base3sx_num_lati, None])


#Coloro 
base3sx_2D = COLOR(rgbToPlasmColor([95,95,95]))(base3sx_2D)


#Creo la la  base posizionata sotto il tetto sx
base4sx_vertici =  [ [0,12], [69,12], [69,13], [0,13] ]; 
base4sx_num_lati = [range(1,5)] 
base4sx_2D = MKPOL([base4sx_vertici, base4sx_num_lati, None])

#Coloro 
base4sx_2D = COLOR(rgbToPlasmColor([128,128,128]))(base4sx_2D)


#Creo il tetto sx
tetto1sx_vertici = [ [0,13], [0,32.3], [69,32.3],[69,13] ];
tetto1sx_num_lati = [range(1,5)] 
tetto1sx_2D = MKPOL([tetto1sx_vertici, tetto1sx_num_lati, None])
tetto1sx_2D = ROTATE([2,3])(-PI/3)(tetto1sx_2D)
tetto1sx_2D=T([2,3])([6.5,11.5])(tetto1sx_2D)

#Coloro
tetto1sx_2D = COLOR(rgbToPlasmColor([147,147,147]))(tetto1sx_2D)

#Creo la struttura SX
floor3=STRUCT([base1sx_2D,base2sx_2D,base3sx_2D,base4sx_2D,tetto1sx_2D])



#CREO LA PARTE DX

#Creo la base dx
base1dx_2D = MKPOL([base1sx_vertici, base1sx_num_lati, None])


#Coloro Grigio 20%
base1dx_2D = COLOR(rgbToPlasmColor([210,210,210]))(base1dx_2D)


#Creo la seconda base dx
base2dx_2D = MKPOL([base2sx_vertici, base2sx_num_lati, None])


#Coloro 
base2dx_2D = COLOR(rgbToPlasmColor([147,147,147]))(base2dx_2D)


#Creo la terza base su cui poggeranno le colonne dx
base3dx_2D = MKPOL([base3sx_vertici, base3sx_num_lati, None])


#Coloro 
base3dx_2D = COLOR(rgbToPlasmColor([147,147,147]))(base3dx_2D)


#Creo la la  base posizionata sotto il tetto dx
base4dx_2D = MKPOL([base4sx_vertici, base4sx_num_lati, None])

#Coloro 	
base4dx_2D = COLOR(rgbToPlasmColor([128,128,128]))(base4dx_2D)


#Creo il tetto della parte DX
tetto1dx_2D = MKPOL([tetto1sx_vertici, tetto1sx_num_lati, None])
tetto1dx_2D = ROTATE([2,3])(PI/3)(tetto1dx_2D)
tetto1dx_2D=T([2,3])([6.5,-11.5])(tetto1dx_2D)
tetto1dx_2D = COLOR(rgbToPlasmColor([147,147,147]))(tetto1dx_2D)

#Creo la struttura dx
floor4=STRUCT([base1dx_2D,base2dx_2D,base3dx_2D,base4dx_2D,tetto1dx_2D])

#Creo il piano dove poggiano le colonne
base5_vertici = [ [0,0], [0,69], [33,69], [33,0] ];
base5_num_lati = [range(1,5)] 
floor5 = MKPOL([base5_vertici, base5_num_lati, None])
floor5 = COLOR(rgbToPlasmColor([255,255,255]))(floor5)



#Creo il piano superiore del tetto
floor6= MKPOL([base5_vertici, base5_num_lati, None])

#Creo il piamo inferiore
floor7= MKPOL([base5_vertici, base5_num_lati, None])


#CREO LA TRUTTURA 2.5D
floor2=T([3])(69)(floor2)

floor3=ROTATE([1,3])(PI/2)(floor3)

floor4=ROTATE([1,3])(PI/2)(floor4)
floor4=T([1,3])(33)(floor4)

floor5=ROTATE([2,3])(PI/2)(floor5)
floor5=T(2)(3)(floor5)

floor6=ROTATE([2,3])(PI/2)(floor6)
floor6=T(2)(12)(floor6)

floor7=ROTATE([2,3])(PI/2)(floor7)

#Struttura finale
two_and_half_model=STRUCT([floor1,floor2,floor3,floor4,floor5,floor6,floor7])
