import exercise1
from pyplasm import*

#Creo una funzione per convertire colori RGB in Plasm
def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

#Creo le colonne anteriori
Colonna_ant_vertici = [ [0,3], [0.5,11], [1.5,11],[2,3] ];
Colonna_ant_lati = [range(1,5)] 
Colonna_ant_2D = MKPOL([Colonna_ant_vertici, Colonna_ant_lati, None])

blocchetto_ant_coords = [[-0.5,11], [-0.5,12], [2.5,12],[2.5,11]]
blocchetto_ant_lati = [range(1,5)] 
blocchetto_ant_2D = MKPOL([blocchetto_ant_coords, blocchetto_ant_lati, None])

colonna_ant=STRUCT([Colonna_ant_2D,blocchetto_ant_2D])

colonne_ant_temp=[T(1)(4.3),colonna_ant]
#Duplico
north=STRUCT(NN(8)(colonne_ant_temp))
#Traslo su x
north=T(1)(-3.8)(north)
#Coloro
north= COLOR(rgbToPlasmColor([95,95,95]))(north)




#Creo le colonne posteriori
Colonna_post_2D = MKPOL([Colonna_ant_vertici, Colonna_ant_lati, None])

blocchetto_post_2D = MKPOL([blocchetto_ant_coords, blocchetto_ant_lati, None])

colonna_post=STRUCT([Colonna_post_2D,blocchetto_post_2D])

colonne_post_temp=[T(1)(4.3),colonna_ant]
#Duplico
sud=STRUCT(NN(8)(colonne_post_temp))
#Traslo su x e z
sud=T([1,3])([-3.8,69])(sud)
#Coloro
sud= COLOR(rgbToPlasmColor([95,95,95]))(sud)


#Creo le colonne sx
Colonna_sx_vertici = [ [0,3], [0.5,11], [1.5,11],[2,3] ];
Colonna_sx_lati = [range(1,5)] 
Colonna_sx_2D = MKPOL([Colonna_sx_vertici, Colonna_sx_lati, None])

blocchetto_sx_coords = [[-0.5,11], [-0.5,12], [2.5,12],[2.5,11]]
blocchetto_sx_lati = [range(1,5)] 
blocchetto_sx_2D = MKPOL([blocchetto_sx_coords, blocchetto_sx_lati, None])

colonna_sx=STRUCT([Colonna_sx_2D,blocchetto_sx_2D])
colonne_sx_temp=[T(1)(4.7),colonna_sx]
est=STRUCT(NN(15)(colonne_sx_temp))


est=ROTATE([1,3])(PI/2)(est)
est=T(3)(-4.3)(est)
est= COLOR(rgbToPlasmColor([95,95,95]))(est)

#Creo le colonne dx
Colonna_dx_2D = MKPOL([Colonna_sx_vertici, Colonna_sx_lati, None])

blocchetto_dx_2D = MKPOL([blocchetto_sx_coords, blocchetto_sx_lati, None])

colonna_dx=STRUCT([Colonna_dx_2D,blocchetto_dx_2D])
colonne_dx_temp=[T(1)(4.7),colonna_dx]
ovest=STRUCT(NN(15)(colonne_dx_temp))


ovest=ROTATE([1,3])(PI/2)(ovest)
ovest=T([1,3])([33,-4.3])(ovest)
ovest= COLOR(rgbToPlasmColor([95,95,95]))(ovest)
VIEW(STRUCT([exercise1.two_and_half_model,north,sud,est,ovest]))