from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *

#Funzioni Utili
DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([STRUCT,MKPOLS])

#Camera1
master = assemblyDiagramInit([5,3,2])([[.1,1.5,1,1.5,.1],[.1,3,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Porta
toMerge = 23
diagram0 = assemblyDiagramInit([3,1,2])([[1.5,2,1.5],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 13
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [30,35,9,14,20]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera1=DRAW2(master)

#Camera2
master = assemblyDiagramInit([5,3,2])([[.1,1.5,1,1.5,.1],[.1,3,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Porta
toMerge = 19
diagram0 = assemblyDiagramInit([3,1,2])([[1.5,2,1.5],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 17
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [30,35,9,15,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera2=DRAW2(master)
camera2=T(2)(5)(camera2)


#Bagno2
master = assemblyDiagramInit([3,5,2])([[.1,2.2,.1],[.1,.4,0.9,.4,.1],[.1,2.7]])
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
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)

#Rimozione
toRemove = [14,16,12,28,31]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
bagno=DRAW2(master)
bagno=T(2)(3.1)(bagno)

#Stireria
master = assemblyDiagramInit([5,3,2])([[.1,1.4,1,.5,.1],[.1,2.1,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Porta
toMerge = 13
diagram3 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram3,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 16
diagram0 = assemblyDiagramInit([3,1,3])([[3,3,3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [34,28,9,14,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW2(master)
stireria=DRAW2(master)
stireria=T([1,2])([10.8,8.2])(stireria)

#Cucina
master = assemblyDiagramInit([5,6,2])([[.1,1,1,2,.1],[.1,1.5,1,1.2,0.3,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc4=T([1,2])([13.2,4.1])(hpc4)


#Finestra
toMerge = 53
diagram = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 35
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 25
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 7
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [61,63,57,31,59,14,25,36,16,27,38,18,29,40,20,31,42]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
cucina=DRAW2(master)
cucina=T([1,2])([13.2,4.1])(cucina)



#Bagno2
master = assemblyDiagramInit([5,3,2])([[.1,1.4,1,.4,.1],[.1,1.2,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc=T([1,2])([10.6,5.3])(hpc)

#Porta
toMerge = 17
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [29,15,9,20]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
bagno2=DRAW2(master)
bagno2=T([1,2])([10.2,5.3])(bagno2)

#Scale
master = assemblyDiagramInit([3,5,2])([[.1,3.4,.1],[.1,.2,1,.2,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Porta
toMerge = 25
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 19
diagram0 = assemblyDiagramInit([3,1,3])([[3,3,3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [28,15,34,13,17,14]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
scale=DRAW2(master)
scale=T([1,2])([4,6.6])(scale)

#Remove
master = assemblyDiagramInit([3,3,2])([[.1,1.3,.1],[.1,1.4,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Remove
toRemove = [5,11,17,3,9,15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
remove=DRAW2(master)
remove=T([1,2])([7.6,6.6])(remove)

#Soggiorno2
master = assemblyDiagramInit([5,3,2])([[.15,0.8,1.6,0.8,.15],[.1,6.0,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Porta
toMerge = 13
diagram0 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [29,3,9,14,20,26,11,16,22]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno2=DRAW2(master)
soggiorno2=T([1,2])([4.1,0.5])(soggiorno2)



#Soggiorno3
master = assemblyDiagramInit([7,4,2])([[.4,1,1,0.9,1,1,.3],[.1,.4,4.8,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Porta
toMerge = 41
diagram0 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#Porta
toMerge = 33
diagram0 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#Porta
toMerge = 17
diagram0 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#Porta
toMerge = 9
diagram0 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [58,56,54,52,5,12,19,27,34,41,49,7,14,21,29,36,43,51,10,17,32,39]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno3=DRAW2(master)
soggiorno3=T([1])([7.6])(soggiorno3)



#Sala pranzo
master = assemblyDiagramInit([5,3,2])([[.1,1,2,1,.1],[.1,3.5,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)





#Finestra
toMerge = 13
diagram0 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)



#Rimozione
toRemove = [29,9,14,20,3,28,5,11,16,22,23]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno4=DRAW2(master)
soggiorno4=T([1,2])([13.2,0.5])(soggiorno4)


#Camino
master = assemblyDiagramInit([3,3,2])([[.1,1,.1],[.1,2,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


master = master[0], [cell for k,cell in enumerate(master[1]) ]
camino=DRAW2(master)
camino=T([1,2])([6.5,2])(camino)

#Remove2
master = assemblyDiagramInit([4,5,2])([[.1,3.6,2.6,.1],[.1,2.8,1.1,1.1,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Finestra
toMerge = 19
diagram0 = assemblyDiagramInit([3,1,3])([[3,3,3],[.1],[1,1.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Finestra
toMerge = 7
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

#Rimozione
toRemove = [47,42,12,21,14,23,16,25,3,10,1,19,31,29,33,35,37,27]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
remove2=DRAW2(master)
remove2=T([1,2])([7.5,5.3])(remove2)

#Remove3
master = assemblyDiagramInit([3,3,2])([[.1,2.1,.1],[.1,2,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

toRemove = [1,3,5,7,9,11,13,15,17]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
remove3=DRAW2(master)
remove3=T([1,2])([2.4,3.1])(remove3)



#Scale
gradino2_vertici = [ [0,0], [0,0.3], [1.3,0], [1.3,0.3] ];
gradino2_num_lati = [range(1,5)] 
gradino2_2D = MKPOL([gradino2_vertici, gradino2_num_lati, None])
gradino2 = PROD([gradino2_2D, Q(0.2)])

gradino3 = PROD([gradino2_2D, Q(0.2)])
gradino3=T([2,3])([0.2,0.2])(gradino3)

gradino4 = PROD([gradino2_2D, Q(0.2)])
gradino4=T([2,3])([0.4,0.4])(gradino4)

gradino5 = PROD([gradino2_2D, Q(0.2)])
gradino5=T([2,3])([0.6,0.6])(gradino5)

gradino6 = PROD([gradino2_2D, Q(0.2)])
gradino6=T([2,3])([0.8,0.8])(gradino6)

gradino7 = PROD([gradino2_2D, Q(0.2)])
gradino7=T([2,3])([1,1])(gradino7)

gradino8 = PROD([gradino2_2D, Q(0.2)])
gradino8=T([2,3])([1.2,1.2])(gradino8)

gradino9 = PROD([gradino2_2D, Q(0.2)])
gradino9=T([2,3])([1.4,1.4])(gradino9)

gradino10 = PROD([gradino2_2D, Q(0.2)])
gradino10=T([2,3])([1.6,1.6])(gradino10)

gradino11 = PROD([gradino2_2D, Q(0.2)])
gradino11=T([2,3])([1.8,1.8])(gradino11)

gradino12 = PROD([gradino2_2D, Q(0.2)])
gradino12=T([2,3])([2,2])(gradino12)

gradino13 = PROD([gradino2_2D, Q(0.2)])
gradino13=T([2,3])([2.2,2.2])(gradino13)

gradino14 = PROD([gradino2_2D, Q(0.2)])
gradino14=T([2,3])([2.4,2.4])(gradino14)

gradino15 = PROD([gradino2_2D, Q(0.2)])
gradino15=T([2,3])([2.6,2.6])(gradino15)

#Assemblo la scalinata
scalinata=STRUCT([gradino2,gradino3,gradino4,gradino5,gradino6,gradino7,gradino8,gradino9,gradino10,
	gradino11,gradino12,gradino13,gradino14,gradino15])

scalinata=ROTATE([1,2])(PI/2)(scalinata)

#La traslo sui 3 assi al centro della parte frontale
scalinata=T([1,2])([7.3,5.3])(scalinata)

#Faccio la seconda scala
scalinata2=scalinata

#Traslo la seconda scala
scalinata2=T([1,2,3])([-11.9,-13.4,-2.7])(scalinata2)
scalinata2=ROTATE([1,2])(-PI)(scalinata2)


#Esterno
est1= CUBOID([4.2,6,0.1])
est1=T([1,2])([13.2,-5.5])(est1)

est2= CUBOID([13.2,3,0.1])
est2=T([2])([-2.5])(est2)



colonna1=CUBOID([0.5,0.5,2.8])
colonna1=T([1,2])([3,-1])(colonna1)
colonna2=CUBOID([0.5,0.5,2.8])
colonna2=T([1,2])([7,-1])(colonna2)
colonna3=CUBOID([0.5,0.5,2.8])
colonna3=T([1,2])([10.5,-1])(colonna3)
colonna4=CUBOID([0.5,0.5,2.8])
colonna4=T([1,2])([14,-1])(colonna4)
colonne=STRUCT([colonna1,colonna2,colonna3,colonna4])

ext4_vertici = [ [0,0], [0,2], [0.5,0], [0.5,2] ];
ext4_num_lati = [range(1,5)] 
ext4_2D = MKPOL([ext4_vertici, ext4_num_lati, None])
ext4 = PROD([ext4_2D, Q(2.8)])
ext4=T(2)(-2)(ext4)

ext5_vertici = [ [0,0], [0,6], [2.8,0],[2.8,2.5],[0.3,6] ];
ext5_num_lati = [range(1,6)] 
ext5_2D = MKPOL([ext5_vertici, ext5_num_lati, None])
ext5 = PROD([ext5_2D, Q(0.5)])
ext5=ROTATE([1,3])(PI/2)(ext5)
ext5=ROTATE([1,2])(PI)(ext5)
ext5=T([1,2])([16.9,0.5])(ext5)

esterno=STRUCT([est1,est2,ext4,ext5,colonne])

#ParteSuperiore
parteSup=CUBOID([17.4,10.3,0.7])
parteSup=T([2,3])([-2,2.8])(parteSup)
#Tetto

tetto_vertici = [ [0,0], [10.3,0], [5.15,2], ];
tetto_num_lati = [range(1,4)] 
tetto_2D = MKPOL([tetto_vertici, tetto_num_lati, None])
#Porto in 2,5D
tetto = PROD([tetto_2D, Q(17.4)])
tetto=ROTATE([2,3])(PI/2)(tetto)
tetto=ROTATE([1,2])(PI/2)(tetto)
tetto=T([2,3])([-2,3.5])(tetto)


#Creo La mansarda

#Camera1
master = assemblyDiagramInit([7,6,2])([[.1,0.5,1.1,2,1,1,.1],[.1,0.5,1.3,2,1.3,.2],[.1,2.3]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


#Finestra
toMerge = 49
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.2]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Porta
toMerge = 35
diagram0 = assemblyDiagramInit([1,1,2])([[3],[.1],[2.2,.2]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toMerge = 25
diagram0 = assemblyDiagramInit([1,1,2])([[3],[.1],[2.2,.2]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)



toMerge = 9
diagram0 = assemblyDiagramInit([1,1,2])([[3],[.1],[2.2,.2]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toMerge = 5
diagram0 = assemblyDiagramInit([1,1,2])([[3],[.1],[2.2,.2]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [80,88,84,86,24,26,28,30,35,37,39,41,46,48,50,52,58,60,62,64,13,15,17,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
cameraMan=DRAW2(master)
cameraMan=T([1])([4.2])(cameraMan)

#bagnoMan
master = assemblyDiagramInit([5,5,2])([[.1,0.5,1.5,2,.1],[.1,0.5,1.3,1.5,.1],[.1,2.5]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)



toMerge = 21
diagram0 = assemblyDiagramInit([1,1,3])([[3],[.1],[1,1.2,.3]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [50,17,26,36,46,15,24,34,44,13,22,32,42]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
bagnoMan=DRAW2(master)


#Balcone

master = assemblyDiagramInit([3,3,3])([[.1,9.8,.1],[.1,1.3,.1],[.1,1.5,.1]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Rimozione
toRemove = [13,16,17,14]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
balcone=DRAW2(master)
balcone=T(2)(-1.5)(balcone)

#muro
muro=CUBOID([0.1,1.8,2.8])
muro=T(2)(3.5)(muro)

#muro2
muro2=CUBOID([4.5,0.1,2.8])
muro2=T(2)(5.3)(muro2)


#ParteSupTettoMansarda
ParteSupTettoMansarda=CUBOID([10,9.7,0.3])
ParteSupTettoMansarda=T(3)(2.4)(ParteSupTettoMansarda)

#TettoMansarda
tettoM_vertici = [ [0,0], [9.7,0], [4.85,1.5], ];
tettoM_num_lati = [range(1,4)] 
tettoM_2D = MKPOL([tettoM_vertici, tettoM_num_lati, None])
#Porto in 2,5D
tettoM = PROD([tettoM_2D, Q(10)])
tettoM=ROTATE([2,3])(PI/2)(tettoM)
tettoM=ROTATE([1,2])(PI/2)(tettoM)
tettoM=T(3)(2.7)(tettoM)


Mansarda=STRUCT([cameraMan,bagnoMan,balcone,muro,muro2,ParteSupTettoMansarda,tettoM])

Mansarda=T([1,2,3])([3.9,1.5,3])(Mansarda)

#Rimozione
rimozione=CUBOID([10,7,4])
rimozione=T([1,3])([4,3])(rimozione)
tetto=DIFFERENCE([tetto,rimozione])

#Muri Stireria
muroStir=CUBOID([6.4,3.6,3])
muroStir=T([1,2,3])([7.5,6.9,2.8])(muroStir)
#Assemblo
plan1 = STRUCT([camera1,camera2,bagno,stireria,scale,soggiorno2,soggiorno3,soggiorno4,camino,cucina
	,bagno2,remove,remove2,remove3,scalinata,scalinata2,esterno,parteSup,tetto,Mansarda,muroStir])


#Visualizzo
#VIEW(plan1)








