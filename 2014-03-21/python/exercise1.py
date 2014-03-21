from pyplasm import*

#Creo una funzione per convertire colori RGB in Plasm
def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]


#Creazione della base. Approssimata 72x33
base1_vertici = [ [0,0], [0,72], [33,72], [33,0] ];
base1_num_lati = [range(1,5)] 
base1_2D = MKPOL([base1_vertici, base1_num_lati, None])

#Porto in 2,5D
floor1 = PROD([base1_2D, Q(1)])

#Coloro Grigio 20%
floor1 = COLOR(rgbToPlasmColor([210,210,210]))(floor1)


#Creo la seconda base.Approssimata 70x32
base2_vertici = [ [0,0], [0,71], [32,71], [32,0] ];
base2_num_lati = [range(1,5)] 
base2_2D = MKPOL([base2_vertici, base2_num_lati, None])

#Porto in 2,5D
floor2 = PROD([base2_2D, Q(1)])

#Coloro Grigio 40%
floor2 = COLOR(rgbToPlasmColor([147,147,147]))(floor2)


#Creo la terza base su cui poggeranno le colonne: 68x30
base3_vertici = [ [0,0], [0,70], [31,70], [31,0] ];
base3_num_lati = [range(1,5)] 
base3_2D = MKPOL([base3_vertici, base3_num_lati, None])

#Porto in 2,5D
floor3 = PROD([base3_2D, Q(1)])

#Coloro Grigio 60%
floor3 = COLOR(rgbToPlasmColor([95,95,95]))(floor3)


#Creo la la  base posizionata sotto il tetto
base4_vertici =  [ [0,0], [0,70], [31,70], [31,0] ]; 
base4_num_lati = [range(1,5)] 
base4_2D = MKPOL([base4_vertici, base4_num_lati, None])

#Porto in 2,5D
floor4 = PROD([base4_2D, Q(3)])

#Coloro Grigio 50%	
floor4 = COLOR(rgbToPlasmColor([128,128,128]))(floor4)


#Creo il tetto.Approssimato 70x32x5
from pyplasm import*
tetto_vertici = [ [0,0], [33,0], [16,5], ];
tetto_num_lati = [range(1,4)] 
tetto_2D = MKPOL([tetto_vertici, tetto_num_lati, None])

#Porto in 2,5D
floor5 = PROD([tetto_2D, Q(72)])


#Assemblo le 3 basi e il tetto
floor2=T([1,2,3])([0.5,0.5,1])(floor2)
floor3=T([1,2,3])([1,1,2])(floor3)
floor4=T([1,2,3])([1,1,15])(floor4)
building=STRUCT([floor1,floor2,floor3])


floor5=MAP([S1,S3,S2])(floor5)
floor5=T([3])([18])(floor5)

#Coloro il tetto dopo la traslazione.Grigio 80%
floor5 = COLOR(rgbToPlasmColor([47,47,47]))(floor5)

#Creo la struttura 2,5D
two_and_half_model=STRUCT([floor1,floor2,floor3,floor4,floor5])
VIEW(two_and_half_model)

