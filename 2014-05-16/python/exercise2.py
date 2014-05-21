from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *
from architectural import *
from splines import*
import exercise1Imp

#Funzioni Utili
DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([STRUCT,MKPOLS])

def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

#Camera1
master = assemblyDiagramInit([4,5,2])([[.1,1.9,2,.1],[.1,1,2,1,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)



#Porta
toMerge = 29
diagram0 = assemblyDiagramInit([3,1,2])([[3,3,3],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 5
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [45,40,16,26,14,24,12,22]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera1=DRAW2(master)



#Camera2
master =assemblyDiagramInit([4,5,2])([[.1,1.9,2,.1],[.1,1,1,1,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Porta
toMerge = 21
diagram1 = assemblyDiagramInit([3,1,2])([[3,3,3],[.1],[2.2,.5]])
master = diagram2cell(diagram1,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 5
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [40,45,16,25,14,23,12,21]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera2=DRAW2(master)
camera2=T(2)(6)(camera2)



#Bagno
master = assemblyDiagramInit([3,5,2])([[.1,2.2,.1],[.1,.4,1,.4,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)




#Porta
toMerge = 25
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 5
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [28,31,14,12,16]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
bagno=DRAW2(master)
bagno=T(2)(4.1)(bagno)


#Scale
master = assemblyDiagramInit([5,3,2])([[.1,1,.1,2.3,.1],[.1,1.4,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 7
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 22
diagram0 = assemblyDiagramInit([3,1,3])([[3,3,3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [28,8,14,20]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
scale=DRAW2(master)
scale=T([1,2])([4.1,7.6])(scale)



#Garage1
master = assemblyDiagramInit([4,5,2])([[.1,2.5,3.2,.1],[.3,1,3,2.8,.1],[.1,2.7]])
V,CV= master
hpc1 = SKEL_1(STRUCT(MKPOLS(master)))
hpc1 = cellNumbering (master,hpc1)(range(len(CV)),CYAN,2)

#Porta
toMerge = 3
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [39,12,22,14,24,16,26,36,34,32,30]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
garage1=DRAW2(master)
garage1=COLOR(rgbToPlasmColor([255	,204,153]))(garage1)
garage1=T([1,2])([7.6,5.3])(garage1)


#Garage2
master = assemblyDiagramInit([5,4,2])([[.1,3.5,2,2.9,.1],[.1,1,6.7,.1],[.1,2.7]])
V,CV= master
hpc2 = SKEL_1(STRUCT(MKPOLS(master)))
hpc2 = cellNumbering (master,hpc2)(range(len(CV)),CYAN,2)




#Porta
toMerge = 25
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [5,13,21,28,11,26,39,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
garage2=DRAW2(master)
garage2=COLOR(rgbToPlasmColor([255	,204,153]))(garage2)
garage2=T([1,2])([13.3,4.6])(garage2)

#pianoGarage
pianoGarage=CUBOID([4.6,4.6,0.1])
pianoGarage=T([1])([17.3])(pianoGarage)

#SalitaGarage

salita_vertici = [ [0,0], [0,1.2], [6,0],[6,0.1] ];
salita_num_lati = [range(1,5)] 
salita_2D = MKPOL([salita_vertici, salita_num_lati, None])
#Porto in 2,5D
salita = PROD([salita_2D, Q(4.6)])
salita=ROTATE([2,3])(PI/2)(salita)
salita=ROTATE([1,2])(PI/2)(salita)
salita=T([1,2])([17.3,-6])(salita)

#MuroGarage
muroGarage=CUBOID([0.4,18.5,2.9])
muroGarage=T([1,2])([21.9,-6])(muroGarage)

#MuroGarage2
muroGarage2=CUBOID([0.4,10.9,0.5])
muroGarage2=T([1,2,3])([21.9,-5.8,2.9])(muroGarage2)


#MuroGarage3
muroGarage3=CUBOID([4.9,0.4,0.5])
muroGarage3=T([1,2,3])([17.4,4.6,2.9])(muroGarage3)

#Assemblo


garage=STRUCT([garage1,garage2])
garage=COLOR(rgbToPlasmColor([255	,204,153]))(garage)

#Soggiorno2
master = assemblyDiagramInit([3,3,2])([[.1,3.3,.1],[.1,7.5,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Rimozione
toRemove = [9,3,15,11]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno2=DRAW2(master)
soggiorno2=T([1])([4.1])(soggiorno2)


#Soggiorno3
master = assemblyDiagramInit([3,4,2])([[.1,5.5,.1],[.1,.4,5.3,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Rimozione
toRemove = [5,13,21,15,11,7,23,3,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno3=DRAW2(master)
soggiorno3=T([1])([7.6])(soggiorno3)


#Soggiorno4
master = assemblyDiagramInit([3,5,2])([[.1,4,.1],[.1,1.,2,1.3,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)



#Finestra
toMerge = 25
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#VIEW(hpc)

#Rimozione
toRemove = [30,15,13,17,3,5,7,9,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno4=DRAW2(master)
soggiorno4=T([1])([13.2])(soggiorno4)


#Soggiorno5
master = assemblyDiagramInit([3,7,2])([[.1,5.5,.1],[.1,1.5,.3,2.5,0.6,.2,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Porta
toMerge = 9
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 3
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 29
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Apertura
toMerge = 32
diagram2 = assemblyDiagramInit([1,1,3])([[2],[.1],[1,1.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [23,21,19,17,15,40,38,42,45]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno5=DRAW2(master)
soggiorno5=T([1,2])([7.6,0.1])(soggiorno5)


#Remove
master = assemblyDiagramInit([3,3,2])([[.1,2.1,.1],[.1,3,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

toRemove = [1,3,5,7,9,11,13,15,17]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
remove=DRAW2(master)
remove=T([1,2])([2.4,3.1])(remove)


#Dispensa
master = assemblyDiagramInit([3,5,2])([[.1,2,.1],[.1,.4,0.7,.4,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc=T(2)(3.1)(hpc)
#VIEW(hpc)

#Porta
toMerge = 25
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toRemove = [15,13,17,29]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
dispensa=DRAW2(master)
dispensa=T([1,2])([4,2.5])(dispensa)

#Camino
camino=CUBOID([1,1,8.5])
camino=T([1])([17.3])(camino)

#Esterni
ext1=CUBOID([14.3,7.3,0.1])
ext1=T([1,2,3])([7.6,5.2,2.8])(ext1)

ext2=CUBOID([8.7,1,0.1])
ext2=T([1,2,3])([13.2,4.6,2.8])(ext2)

#Vialetto

domain1D = larDomain([32])
domain2D = larIntervals([32,48],'simplex')([1,1])
b1 = BEZIER(S1)([[-3.8,5], [0.5,-10.4], [10,-9]])
b2=BEZIER(S1)([[-0.6,5], [1.5,-5.5], [9.5,-6]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
vialetto1 = PROD([path, Q(1.2)])
vialetto1=T([1,2,3])([-1,-11])(vialetto1)


b1 = BEZIER(S1)([[8.5,-9], [17.5,-10.4], [21.9,5]])
b2=BEZIER(S1)([[8.5,-6], [16.5,-5.7], [17.3,5]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
vialetto2 = PROD([path, Q(1.2)])
vialetto2=T([2,3])([-11])(vialetto2)
vialetto=STRUCT([vialetto1,vialetto2,garage])

#Scale vialetto

b1 = BEZIER(S1)([[-1.5,-5.5],[6.5,-16.5], [14,-5.5]])
b2=BEZIER(S1)([[0.2,-5.5],[6.5,-9], [11,-5.5]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
grad1 = PROD([path, Q(0.2)])
grad1=T([1,2,3])([2,-8,1])(grad1)

b1 = BEZIER(S1)([[1.5,-5.5],[6.5,-9], [10.9,-5.5]])
b2=BEZIER(S1)([[1.5,-5.5],[6.5,-6], [10.9,-5.5]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
grad2 = PROD([path, Q(0.2)])
grad2=T([1,2,3])([2,-8.3,1.2])(grad2)

b1 = BEZIER(S1)([[2.5,-5.5],[6.5,-8], [9.9,-5.5]])
b2=BEZIER(S1)([[2.5,-5.5],[6.5,-6], [9.9,-5.5]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
grad3 = PROD([path, Q(0.2)])
grad3=T([1,2,3])([2,-8.2,1.4])(grad3)

b1 = BEZIER(S1)([[2.5,-5.5],[6.5,-8], [9.9,-5.5]])
b2=BEZIER(S1)([[2.5,-5.5],[6.5,-6], [9.9,-5.5]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
grad4 = PROD([path, Q(0.2)])
grad4=T([1,2,3])([2,-7.8,1.6])(grad4)

grad5=CUBOID([7.4,1,0.15])
grad5=T([1,2,3])([4.5,-13.6,1.8])(grad5)

grad6=CUBOID([7.4,0.6,0.15])
grad6=T([1,2,3])([4.5,-13.2,1.95])(grad6)

grad7=CUBOID([7.4,0.6,0.15])
grad7=T([1,2,3])([4.5,-12.8,2.10])(grad7)

grad8=CUBOID([7.4,0.6,0.15])
grad8=T([1,2,3])([4.5,-12.4,2.25])(grad8)

grad9=CUBOID([7.4,0.6,0.15])
grad9=T([1,2,3])([4.5,-12,2.40])(grad9)

grad10=CUBOID([7.4,3,0.16])
grad10=T([1,2,3])([4.5,-11.6,2.55])(grad10)



scaleEXT=STRUCT([grad1,grad2,grad3,grad4,grad5,grad6,grad7,grad8,grad9,grad10])

#GiardinoPosteriore

giardinoPost=CUBOID([14.3,4,2.9])
giardinoPost=T([1,2])([7.6,12.5])(giardinoPost)

#giardinoPost2
giardinoPost2=CUBOID([3.5,4,2.9])
giardinoPost2=T([1,2])([21.9,12.5])(giardinoPost2)

stradaPost=CUBOID([12.4,7.3,2.9])
stradaPost=T([1,2])([-4.7,9.2])(stradaPost)

stradaPost2=CUBOID([3.3,10,1.2])
stradaPost2=T([1,2])([-4.7,-6.10])(stradaPost2)

#StradaDX
StradaDX=CUBOID([3.1,18.5,2.9])
StradaDX=T([1,2])([22.3,-6])(StradaDX)





#Salita Posteriore
SalitaPos_vertici = [ [0,0], [0,1.2], [7.3,0],[7.3,2.9] ];
SalitaPos_num_lati = [range(1,5)] 
SalitaPos_2D = MKPOL([SalitaPos_vertici, SalitaPos_num_lati, None])
#Porto in 2,5D
SalitaPos = PROD([SalitaPos_2D, Q(3.3)])
SalitaPos=ROTATE([2,3])(PI/2)(SalitaPos)
SalitaPos=ROTATE([1,2])(PI/2)(SalitaPos)
SalitaPos=T([1,2])([-4.75,2])(SalitaPos)

#Muretto
muretto=CUBOID([0.2,9.2,2.8])
muretto=T([1])([-1.5])(muretto)

#baseMuretto
baseMuretto=CUBOID([1.7,9.2,0.1])
baseMuretto=T([1])([-1.5])(baseMuretto)

#Siepe Posteriore
pianta= CUBOID([0.5,0.5,1.5])
Tp=T(1)(0.6)
siepe1=STRUCT(NN(50)([Tp, pianta]))
siepe1=T([1,2,3])([-5.3,16,2.9])(siepe1)
siepe1=COLOR(rgbToPlasmColor([85,104	,5]))(siepe1)

#Siepe sx
pianta= CUBOID([0.5,0.5,1.5])
Tp=T(2)(-0.6)
siepe2=STRUCT(NN(11)([Tp, pianta]))
siepe2=T([1,2,3])([-5.3,15.8,2.9])(siepe2)
siepe2=COLOR(rgbToPlasmColor([85,104	,5]))(siepe2)


siepe3=STRUCT(NN(14)([Tp, pianta]))
siepe3=T([1,2,3])([-5.3,3,1.2])(siepe3)
siepe3=COLOR(rgbToPlasmColor([85,104	,5]))(siepe3)

pianta1=T([1,2,3])([-5.3,3,1.4])(pianta)
pianta2=T([1,2,3])([-5.3,3.8,1.6])(pianta)
pianta3=T([1,2,3])([-5.3,4.4,1.8])(pianta)
pianta4=T([1,2,3])([-5.3,5,1.9])(pianta)
pianta5=T([1,2,3])([-5.3,5.6,2.1])(pianta)
pianta6=T([1,2,3])([-5.3,6.2,2.2])(pianta)
pianta7=T([1,2,3])([-5.3,6.8,2.3])(pianta)
pianta8=T([1,2,3])([-5.3,7.4,2.4])(pianta)
pianta9=T([1,2,3])([-5.3,8,2.6])(pianta)
pianta10=T([1,2,3])([-5.3,8.6,2.8])(pianta)

siepe4=STRUCT([pianta1,pianta2,pianta3,pianta4,pianta5,pianta6,pianta7,pianta8,pianta9,pianta10])
siepe4=COLOR(rgbToPlasmColor([85,104	,5]))(siepe4)

siepe5=STRUCT(NN(36)([Tp, pianta]))
siepe5=T([1,2,3])([25,16,2.9])(siepe5)
siepe5=COLOR(rgbToPlasmColor([85,104	,5]))(siepe5)



principale=STRUCT([camera1,camera2,bagno,scale,garage,soggiorno2,soggiorno3,soggiorno4,soggiorno5,
	remove,dispensa,camino,muretto,baseMuretto,muroGarage,muroGarage2,muroGarage3])

principale = COLOR(rgbToPlasmColor([255	,204,153]))(principale)

esterno=STRUCT([stradaPost,stradaPost2,SalitaPos,vialetto,scaleEXT
	,pianoGarage,salita])

esterno=COLOR(rgbToPlasmColor([128,128,128]))(esterno)
giardinoPost=COLOR(rgbToPlasmColor([34,139,34	]))(giardinoPost)
giardinoPost2=COLOR(rgbToPlasmColor([34,139,34	]))(giardinoPost2)
ext1=COLOR(rgbToPlasmColor([255	,204,153]))(ext1)
ext2=COLOR(rgbToPlasmColor([255	,204,153]))(ext2)
StradaDX=COLOR(rgbToPlasmColor([150,75,0]))(StradaDX)



siepe=STRUCT([siepe1,siepe2,siepe3,siepe4,siepe5])

#Assemblamento secondo piano
plan2 = STRUCT([principale,esterno,ext1,ext2,giardinoPost,giardinoPost2,siepe,StradaDX])



#Richiamo il piano terra
plan1=exercise1Imp.plan1
#Traslo il piano a fianco
plan1=T([2,3])([1,2.8])(plan1)
#Creo una struttura unica
#Creo primo e secondo piano
plan=STRUCT([plan1,plan2])
#Visualizzo
VIEW(plan)

