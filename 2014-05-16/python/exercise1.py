from architectural import *
from pyplasm import *
from scipy import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

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
master = assemblyDiagramInit([5,3,2])([[.1,1.4,1,.4,.1],[.1,2,.1],[.1,2.7]])
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
stireria=T([1,2])([9.1,8.2])(stireria)






#Cucina
master4 = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,4,.1],[.1,2.7]])
V4,CV4 = master4
hpc4 = SKEL_1(STRUCT(MKPOLS(master4)))
hpc4 = cellNumbering (master4,hpc4)(range(len(CV4)),CYAN,2)
hpc4=T([1,2])([13.2,4.1])(hpc4)



 #Bagno2
master5 = assemblyDiagramInit([3,3,2])([[.1,2.5,.1],[.1,1.2,.1],[.1,2.7]])
V5,CV5 = master5
hpc5 = SKEL_1(STRUCT(MKPOLS(master5)))
hpc5 = cellNumbering (master5,hpc5)(range(len(CV4)),CYAN,2)
hpc5=T([1,2])([10.6,5.3])(hpc5)


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
master7 = assemblyDiagramInit([3,3,2])([[.1,1.4,.1],[.1,1.5,.1],[.1,2.7]])
V7,CV7= master7
hpc7 = SKEL_1(STRUCT(MKPOLS(master7)))
hpc7 = cellNumbering (master7,hpc7)(range(len(CV7)),CYAN,2)
hpc7=T([1,2])([7.6,6.6])(hpc7)


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
VIEW(hpc)

toRemove = [5,13,21,15,11,7,23]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno3=DRAW2(master)
soggiorno3=T([1])([7.6])(soggiorno3)


plan = STRUCT([camera1,camera2,bagno,stireria,scale,soggiorno2,soggiorno3])
VIEW(plan)
#Sala pranzo

master10 = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,3.5,.1],[.1,2.7]])
V10,CV10= master10
hpc10 = SKEL_1(STRUCT(MKPOLS(master10)))
hpc10 = cellNumbering (master10,hpc10)(range(len(CV10)),CYAN,2)
hpc10=T([1,2])([13.2,0.5])(hpc10)



#Camino

master11 = assemblyDiagramInit([3,3,2])([[.1,1,.1],[.1,2,.1],[.1,2.7]])
V11,CV11= master11
hpc11 = SKEL_1(STRUCT(MKPOLS(master11)))
hpc11 = cellNumbering (master11,hpc11)(range(len(CV11)),CYAN,2)
hpc11=T([1,2])([6.5,2])(hpc11)
#VIEW(STRUCT([hpc0,hpc1,hpc2,hpc3,hpc4,hpc5,hpc6,hpc7,hpc8,hpc9,hpc10,hpc11]))


Porte




toRemove = [9]
master = V0,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)




