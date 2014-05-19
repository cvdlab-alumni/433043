from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *
from architectural import *
from splines import*
import exercise1

#Funzioni Utili
DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([STRUCT,MKPOLS])

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
garage2=T([1,2])([13.3,4.6])(garage2)


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

#Assemblamento secondo piano
plan2 = STRUCT([camera1,camera2,bagno,scale,garage1,garage2,soggiorno2,soggiorno3,soggiorno4,soggiorno5,
	remove,dispensa,camino,ext1,ext2])


#Richiamo il piano terra
plan1=exercise1.plan1
#Traslo il piano a fianco
plan1=T([2,3])([1,2.8])(plan1)
#Creo una struttura unica
#Creo primo e secondo piano
plan=STRUCT([plan1,plan2])
#Visualizzo
VIEW(plan)

