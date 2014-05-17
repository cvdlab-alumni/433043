from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([STRUCT,MKPOLS])

#Camera1
master = assemblyDiagramInit([4,3,2])([[.1,1.9,2,.1],[.1,3,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

#Porta
toMerge = 17
diagram0 = assemblyDiagramInit([3,1,2])([[3,3,3],[.1],[2.2,.5]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [9,15,25]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera1=DRAW2(master)


#Camera2
master =assemblyDiagramInit([4,3,2])([[.1,1.9,2,.1],[.1,3,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc=T(2)(5.1)(hpc)

#Porta
toMerge = 13
diagram1 = assemblyDiagramInit([3,1,2])([[3,3,3],[.1],[2.2,.5]])
master = diagram2cell(diagram1,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [9,14,25]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera2=DRAW2(master)
camera2=T(2)(5)(camera2)


#Bagno2
master = assemblyDiagramInit([3,5,2])([[.1,2.2,.1],[.1,.4,0.9,.4,.1],[.1,2.7]])
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
#VIEW(hpc)

toRemove = [15,13,17,29]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
bagno=DRAW2(master)
bagno=T(2)(3.1)(bagno)






#Stireria
master = assemblyDiagramInit([5,3,2])([[.1,1.4,1,.5,.1],[.1,2.1,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc=T([1,2])([9.1,8.2])(hpc)
#VIEW(hpc)


#Porta
toMerge = 13
diagram3 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram3,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [14,29,9,20]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW2(master)
stireria=DRAW2(master)
stireria=T([1,2])([10.2,8.2])(stireria)






#Cucina
master = assemblyDiagramInit([5,5,2])([[.1,1,1,2,.1],[.1,2.7,1,0.3,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc4=T([1,2])([13.2,4.1])(hpc4)

#Porta
toMerge = 21
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toMerge = 5
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toMerge = 43
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [21,12,31,14,23,33,16,25,35,51]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
cucina=DRAW2(master)
cucina=T([1,2])([13.2,4.1])(cucina)


 #Bagno2
master = assemblyDiagramInit([5,3,2])([[.1,1.4,1,.4,.1],[.1,1.2,.1],[.1,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#hpc=T([1,2])([10.6,5.3])(hpc)



toMerge = 17
diagram = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)




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


toMerge = 25
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [29,15,13,17]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
scale=DRAW2(master)
scale=T([1,2])([4,6.6])(scale)








#Remove
master = assemblyDiagramInit([3,3,2])([[.1,1.3,.1],[.1,1.4,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


toRemove = [5,11,17,3,9,15]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
remove=DRAW2(master)
remove=T([1,2])([7.6,6.6])(remove)


#Soggiorno2
master = assemblyDiagramInit([3,3,2])([[.1,3.4,.1],[.1,6.0,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

toRemove = [9,3,15,11]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno2=DRAW2(master)
soggiorno2=T([1,2])([4.1,0.5])(soggiorno2)




#Soggiorno3

master = assemblyDiagramInit([3,4,2])([[.1,5.5,.1],[.1,.4,4.8,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


toRemove = [5,13,21,15,11,7,23]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno3=DRAW2(master)
soggiorno3=T([1])([7.6])(soggiorno3)



#Sala pranzo
master = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,3.5,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


toRemove = [9,3,11,5]
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

master = assemblyDiagramInit([4,4,2])([[.1,2.5,3.1,.1],[.1,2.8,2.2,.1],[.1,2.7]])
V,CV= master
hpc1 = SKEL_1(STRUCT(MKPOLS(master)))
hpc1 = cellNumbering (master,hpc1)(range(len(CV)),CYAN,2)


toRemove = [29,27,9,17,3,13,21,11,19,1,25,31]
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


plan1 = STRUCT([camera1,camera2,bagno,stireria,scale,soggiorno2,soggiorno3,soggiorno4,camino,cucina
	,bagno2,remove,remove2,remove3])
VIEW(plan1)








