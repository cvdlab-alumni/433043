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
colonna_ant_2D= COLOR(rgbToPlasmColor([210,210,210]))(colonna_ant_2D)


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
blocchetto_ant_2D= COLOR(rgbToPlasmColor([255,255,255]))(blocchetto_ant_2D)

colonna_ant=STRUCT([colonna_ant_2D,blocchetto_ant_2D])

colonne_ant_temp=[T(1)(4.3),colonna_ant]
#Duplico
colonne_ant=STRUCT(NN(8)(colonne_ant_temp))
#Traslo su x
colonne_ant=T([1,3])([-3.8,-1.5])(colonne_ant)




#Creo le colonne posteriori
colonne_posteriori=STRUCT(NN(8)(colonne_ant_temp))
#Traslo su x e z
colonne_posteriori=T([1,3])([-3.8,64.5])(colonne_posteriori)
#Coloro
colonne_posteriori= COLOR(rgbToPlasmColor([64,64,64]))(colonne_posteriori)



#Creo le colonne dx
colonne_dx_temp=[T(1)(4.8),colonna_ant]
colonne_dx=STRUCT(NN(13)(colonne_dx_temp))


colonne_dx=ROTATE([1,3])(PI/2)(colonne_dx)
colonne_dx=T(1)(4.5)(colonne_dx)
colonne_dx= COLOR(rgbToPlasmColor([64,64,64]))(colonne_dx)


#Creo le colonne sx
colonne_sx=STRUCT(NN(13)(colonne_dx_temp))
colonne_sx=ROTATE([1,3])(PI/2)(colonne_sx)
colonne_sx=T(1)(34.5)(colonne_sx)
colonne_sx= COLOR(rgbToPlasmColor([64,64,64]))(colonne_sx)


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


#Creo i blocchetti delle colonne interne
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

#Essembo
colonna_int=STRUCT([colonna_int_2D,blocchetto_int_2D])

#Duplico
colonne_int_temp=[T(1)(4.3),colonna_int]

colonne_int=STRUCT(NN(6)(colonne_int_temp))
colonne_int=T([3])([5])(colonne_int)
colonne_int = COLOR(rgbToPlasmColor([95,95,95]))(colonne_int)


#Creo colonne interne posteriori
colonne_post=STRUCT(NN(6)(colonne_int_temp))
colonne_post=T([3])([60])(colonne_post)
colonne_post = COLOR(rgbToPlasmColor([95,95,95]))(colonne_post)






#Creo le pareti interne sx e dx

mura1_vertici = [ [0,0], [9,0], [9,40], [0,40] ];
mura1_num_lati = [range(1,5)] 
mura1 =MKPOL([mura1_vertici, mura1_num_lati, None])
mura1=ROTATE([1,3])(PI/2)(mura1)
mura1=COLOR(rgbToPlasmColor([95,95,95]))(mura1)

mura2= MKPOL([mura1_vertici, mura1_num_lati, None])
mura2=T(3)(1)(mura2)
mura2=ROTATE([1,3])(PI/2)(mura2)
mura2=COLOR(rgbToPlasmColor([95,95,95]))(mura2)


mura3_vertici = [ [0,0], [0,1], [9,1], [9,0] ];
mura3_num_lati = [range(1,5)] 
mura3 =MKPOL([mura3_vertici, mura3_num_lati, None])
mura3=ROTATE([1,3])(PI/2)(mura3)
mura3=ROTATE([1,2])(PI/2)(mura3)
mura3=COLOR(rgbToPlasmColor([95,95,95]))(mura3)


mura4= MKPOL([mura3_vertici, mura3_num_lati, None])
mura4=ROTATE([1,3])(PI/2)(mura4)
mura4=ROTATE([1,2])(PI/2)(mura4)
mura4=T(2)(40)(mura4)
mura4=COLOR(rgbToPlasmColor([95,95,95]))(mura4)

murasx=STRUCT([mura1,mura2,mura3,mura4])
murasx=ROTATE([2,3])(PI/2)(murasx)
murasx=T([1,2,3])([27,12,12])(murasx)
murasx=COLOR(rgbToPlasmColor([95,95,95]))(murasx)


ovest=STRUCT([colonne_sx,murasx])

muradx=STRUCT([mura1,mura2,mura3,mura4])
muradx=ROTATE([2,3])(PI/2)(muradx)
muradx=T([1,2,3])([7,12,12])(muradx)
muradx=COLOR(rgbToPlasmColor([95,95,95]))(muradx)

est=STRUCT([colonne_dx,muradx])

#Creo le pareti interne anteriori e posteriori

mura5_vertici = [ [0,0], [9,0], [9,20], [0,20] ];
mura5_num_lati = [range(1,5)] 
mura5 =MKPOL([mura5_vertici, mura5_num_lati, None])
mura5=ROTATE([1,3])(PI/2)(mura5)


mura6= MKPOL([mura5_vertici, mura5_num_lati, None])
mura6=T(3)(1)(mura6)
mura6=ROTATE([1,3])(PI/2)(mura6)


mura7_vertici = [ [0,0], [0,1], [9,1], [9,0] ];
mura7_num_lati = [range(1,5)] 
mura7 =MKPOL([mura7_vertici, mura7_num_lati, None])
mura7=ROTATE([1,3])(PI/2)(mura7)
mura7=ROTATE([1,2])(PI/2)(mura7)


mura8= MKPOL([mura7_vertici, mura7_num_lati, None])
mura8=ROTATE([1,3])(PI/2)(mura8)
mura8=ROTATE([1,2])(PI/2)(mura8)
mura8=T(2)(20)(mura8)

murapost=STRUCT([mura5,mura6,mura7,mura8])
murapost=ROTATE([1,3])(PI/2)(murapost)
murapost=ROTATE([1,2])(-PI/2)(murapost)
murapost=T([1,2,3])([7,3,45])(murapost)
murapost=COLOR(rgbToPlasmColor([95,95,95]))(murapost)

sud=STRUCT([colonne_posteriori,murapost])


#Creo le mura anteriori

murAnt1_vertici = [ [0,0], [9,0], [9,7], [0,7] ];
murAnt1_num_lati = [range(1,5)] 
murAnt1 =MKPOL([murAnt1_vertici, murAnt1_num_lati, None])
murAnt1=ROTATE([1,3])(PI/2)(murAnt1)
murAnt1=COLOR(rgbToPlasmColor([95,95,95]))(murAnt1)


murAnt2= MKPOL([murAnt1_vertici, murAnt1_num_lati, None])
murAnt2=T(3)(1)(murAnt2)
murAnt2=ROTATE([1,3])(PI/2)(murAnt2)
murAnt2=COLOR(rgbToPlasmColor([95,95,95]))(murAnt2)


murAnt3_vertici = [ [0,0], [0,1], [9,1], [9,0] ];
murAnt3_num_lati = [range(1,5)] 
murAnt3 =MKPOL([murAnt3_vertici, murAnt3_num_lati, None])
murAnt3=ROTATE([1,3])(PI/2)(murAnt3)
murAnt3=ROTATE([1,2])(PI/2)(murAnt3)
murAnt3=COLOR(rgbToPlasmColor([95,95,95]))(murAnt3)


murAnt4= MKPOL([murAnt3_vertici, murAnt3_num_lati, None])
murAnt4=ROTATE([1,3])(PI/2)(murAnt4)
murAnt4=ROTATE([1,2])(PI/2)(murAnt4)
murAnt4=T(2)(7)(murAnt4)
murAnt4=COLOR(rgbToPlasmColor([95,95,95]))(murAnt4)


#Creo la struttura e le posiziono
murAnt_1=STRUCT([murAnt1,murAnt2,murAnt3,murAnt4])


murAnt_2=STRUCT([murAnt1,murAnt2,murAnt3,murAnt4])
murAnt_2=COLOR(rgbToPlasmColor([95,95,95]))(murAnt_2)

murAnt_1=ROTATE([1,3])(PI/2)(murAnt_1)
murAnt_1=ROTATE([1,2])(-PI/2)(murAnt_1)
murAnt_1=T([1,2,3])([7,3,20])(murAnt_1)
murAnt_1=COLOR(rgbToPlasmColor([95,95,95]))(murAnt_1)

murAnt_1=COLOR(rgbToPlasmColor([95,95,95]))(murAnt_1)

murAnt_2=ROTATE([1,3])(PI/2)(murAnt_2)
murAnt_2=ROTATE([1,2])(-PI/2)(murAnt_2)
murAnt_2=T([1,2,3])([19,3,20])(murAnt_2)
murAnt_2=COLOR(rgbToPlasmColor([95,95,95]))(murAnt_2)




north=STRUCT([colonne_ant,colonne_int,colonne_post,murAnt_1,murAnt_2])


 
VIEW(STRUCT([exercise1.two_and_half_model,north,sud,est,ovest]))

