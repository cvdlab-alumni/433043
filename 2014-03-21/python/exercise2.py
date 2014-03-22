import exercise1
from pyplasm import*

#Creo una funzione per convertire colori RGB in Plasm
def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

#Creo le colonne anteriori
Colonna_ant1_vertici = [ [0,3], [0,11], [2,11],[2,3] ];
Colonna_ant1_lati = [range(1,5)] 
Colonna_ant1_2D = MKPOL([Colonna_ant1_vertici, Colonna_ant1_lati, None])
Colonna_ant1_2D= T(3)(4)(Colonna_ant1_2D)

Colonna_ant2_2D = MKPOL([Colonna_ant1_vertici, Colonna_ant1_lati, None])
Colonna_ant2_2D= T(3)(2)(Colonna_ant2_2D)

Colonna_ant3_2D = MKPOL([Colonna_ant1_vertici, Colonna_ant1_lati, None])
Colonna_ant3_2D= T(1)(2)(Colonna_ant3_2D)
Colonna_ant3_2D=ROTATE([1,3])(PI/2)(Colonna_ant3_2D)

Colonna_ant4_2D = MKPOL([Colonna_ant1_vertici, Colonna_ant1_lati, None])
Colonna_ant4_2D= T([1,3])([2,-2])(Colonna_ant4_2D)
Colonna_ant4_2D=ROTATE([1,3])(PI/2)(Colonna_ant4_2D)

colonna_ant_2D=STRUCT([Colonna_ant1_2D,Colonna_ant2_2D,Colonna_ant3_2D,Colonna_ant4_2D])



blocchetto_ant1_coords = [[-0.5,11], [-0.5,12], [2.5,12],[2.5,11]]
blocchetto_ant1_lati = [range(1,5)] 
blocchetto_ant1_2D = MKPOL([blocchetto_ant1_coords, blocchetto_ant1_lati, None])

blocchetto_ant2_2D = MKPOL([blocchetto_ant1_coords, blocchetto_ant1_lati, None])
blocchetto_ant2_2D= T(3)(3)(blocchetto_ant2_2D)

blocchetto_ant3_2D = MKPOL([blocchetto_ant1_coords, blocchetto_ant1_lati, None])
blocchetto_ant3_2D= T([1,3])([0.5,0.5])(blocchetto_ant3_2D)
blocchetto_ant3_2D=ROTATE([1,3])(PI/2)(blocchetto_ant3_2D)

blocchetto_ant4_2D = MKPOL([blocchetto_ant1_coords, blocchetto_ant1_lati, None])
blocchetto_ant4_2D= T([1,3])([0.5,-2.5])(blocchetto_ant4_2D)
blocchetto_ant4_2D=ROTATE([1,3])(PI/2)(blocchetto_ant4_2D)

blocchetto_facc1_coords = [[0,0], [0,3], [3,0],[3,3]]
blocchetto_facc1_lati = [range(1,5)] 

blocchetto_facc1_2D = MKPOL([blocchetto_facc1_coords, blocchetto_facc1_lati, None])
blocchetto_facc1_2D=ROTATE([2,3])(PI/2)(blocchetto_facc1_2D)
blocchetto_facc1_2D=T([1,2])([-0.5,11])(blocchetto_facc1_2D)


blocchetto_facc2_2D = MKPOL([blocchetto_facc1_coords, blocchetto_facc1_lati, None])
blocchetto_facc2_2D=ROTATE([2,3])(PI/2)(blocchetto_facc2_2D)
blocchetto_facc2_2D=T([1,2])([-0.5,12])(blocchetto_facc2_2D)

blocchetto_ant_2D=STRUCT([blocchetto_ant1_2D,blocchetto_ant2_2D,blocchetto_ant3_2D,blocchetto_ant4_2D,blocchetto_facc1_2D,blocchetto_facc2_2D])


blocchetto_ant_2D=T(3)(1.5)(blocchetto_ant_2D)

colonna_ant=STRUCT([colonna_ant_2D,blocchetto_ant_2D])

colonne_ant_temp=[T(1)(4.3),colonna_ant]
#Duplico
colonne_ant=STRUCT(NN(8)(colonne_ant_temp))
#Traslo su x
colonne_ant=T([1,3])([-3.8,-1.5])(colonne_ant)
#Coloro
colonne_ant= COLOR(rgbToPlasmColor([147,147,147]))(colonne_ant)



#Creo le colonne posteriori
sud=STRUCT(NN(8)(colonne_ant_temp))
#Traslo su x e z
sud=T([1,3])([-3.8,64.5])(sud)
#Coloro
sud= COLOR(rgbToPlasmColor([147,147,147]))(sud)




#Creo le colonne sx
colonne_sx_temp=[T(1)(4.8),colonna_ant]
est=STRUCT(NN(13)(colonne_sx_temp))


est=ROTATE([1,3])(PI/2)(est)
est=T(1)(4.5)(est)
est= COLOR(rgbToPlasmColor([147,147,147]))(est)


#Creo le colonne dx
ovest=STRUCT(NN(13)(colonne_sx_temp))
ovest=ROTATE([1,3])(PI/2)(ovest)
ovest=T(1)(34.5)(ovest)
ovest= COLOR(rgbToPlasmColor([147,147,147]))(ovest)


#Creo le colonne anteriori interne
Colonna_int1_vertici = [ [0,1], [0,11], [1,11],[1,1] ];
Colonna_int1_lati = [range(1,5)] 
Colonna_int1_2D = MKPOL([Colonna_int1_vertici, Colonna_int1_lati, None])
Colonna_int1_2D= T(3)(4)(Colonna_int1_2D)

Colonna_int2_2D = MKPOL([Colonna_int1_vertici, Colonna_int1_lati, None])
Colonna_int2_2D= T(3)(3)(Colonna_int2_2D)

Colonna_int3_2D = MKPOL([Colonna_int1_vertici, Colonna_int1_lati, None])
Colonna_int3_2D= T(1)(3)(Colonna_int3_2D)
Colonna_int3_2D=ROTATE([1,3])(PI/2)(Colonna_int3_2D)

col_temp=STRUCT([Colonna_int1_2D,Colonna_int2_2D,Colonna_int3_2D])
col_temp=T([1,3])([1,-1])(col_temp)

Colonna_int4_2D = MKPOL([Colonna_int1_vertici, Colonna_int1_lati, None])
Colonna_int4_2D= T([1,3])([2,-2])(Colonna_int4_2D)
Colonna_int4_2D=ROTATE([1,3])(PI/2)(Colonna_int4_2D)

colonna_int_2D=STRUCT([col_temp,Colonna_int4_2D])



blocchetto_int1_coords = [[-0.5,11], [-0.5,12], [2.5,12],[2.5,11]]
blocchetto_int1_lati = [range(1,5)] 
blocchetto_int1_2D = MKPOL([blocchetto_int1_coords, blocchetto_int1_lati, None])

blocchetto_int2_2D = MKPOL([blocchetto_int1_coords, blocchetto_int1_lati, None])
blocchetto_int2_2D= T(3)(3)(blocchetto_int2_2D)

blocchetto_int3_2D = MKPOL([blocchetto_int1_coords, blocchetto_int1_lati, None])
blocchetto_int3_2D= T([1,3])([0.5,0.5])(blocchetto_int3_2D)
blocchetto_int3_2D=ROTATE([1,3])(PI/2)(blocchetto_int3_2D)

blocchetto_int4_2D = MKPOL([blocchetto_int1_coords, blocchetto_int1_lati, None])
blocchetto_int4_2D= T([1,3])([0.5,-2.5])(blocchetto_int4_2D)
blocchetto_int4_2D=ROTATE([1,3])(PI/2)(blocchetto_int4_2D)

blocchetto_int_facc1_coords = [[0,0], [0,3], [3,0],[3,3]]
blocchetto_int_facc1_lati = [range(1,5)] 

blocchetto_int_facc1_2D = MKPOL([blocchetto_int_facc1_coords, blocchetto_int_facc1_lati, None])
blocchetto_int_facc1_2D=ROTATE([2,3])(PI/2)(blocchetto_int_facc1_2D)
blocchetto_int_facc1_2D=T([1,2])([-0.5,11])(blocchetto_int_facc1_2D)


blocchetto_int_facc2_2D = MKPOL([blocchetto_int_facc1_coords, blocchetto_int_facc1_lati, None])
blocchetto_int_facc2_2D=ROTATE([2,3])(PI/2)(blocchetto_int_facc2_2D)
blocchetto_int_facc2_2D=T([1,2])([-0.5,12])(blocchetto_int_facc2_2D)

blocchetto_int_2D=STRUCT([blocchetto_int1_2D,blocchetto_int2_2D,blocchetto_int3_2D,blocchetto_int4_2D,blocchetto_int_facc1_2D,blocchetto_int_facc2_2D])


blocchetto_int_2D=T([1,3])([0.5,1])(blocchetto_int_2D)


colonna_int=STRUCT([colonna_int_2D,blocchetto_int_2D])


colonne_int_temp=[T(1)(4.3),colonna_int]

colonne_int=STRUCT(NN(6)(colonne_int_temp))
colonne_int=T([3])([5])(colonne_int)
colonne_int = COLOR(rgbToPlasmColor([95,95,95]))(colonne_int)


#Creo colonne interne posteriori
colonne_post=STRUCT(NN(6)(colonne_int_temp))
colonne_post=T([3])([60])(colonne_post)
colonne_post = COLOR(rgbToPlasmColor([95,95,95]))(colonne_post)

north=STRUCT([colonne_ant,colonne_int,colonne_post])

VIEW(STRUCT([exercise1.two_and_half_model,north,sud,est,ovest]))