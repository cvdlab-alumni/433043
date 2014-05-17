from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *
from splines import*
import exercise1Imp

DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([STRUCT,MKPOLS])

#Camera1
master = assemblyDiagramInit([4,3,2])([[.1,1.9,2,.1],[.1,3.5,.1],[.1,2.7]])
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
master =assemblyDiagramInit([4,3,2])([[.1,1.9,2,.1],[.1,2.5,.1],[.1,2.7]])
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


#Porta
toMerge = 3
diagram1 = assemblyDiagramInit([1,1,2])([[3],[.1],[2.2,.5]])
master = diagram2cell(diagram1,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [24,8,13,28]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
camera2=DRAW2(master)
camera2=T(2)(5.5)(camera2)


#Bagno
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
bagno=T(2)(3.6)(bagno)

#Scale
master = assemblyDiagramInit([5,3,2])([[.1,1,.1,2.3,.1],[.1,1.4,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toMerge = 7
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)



toRemove = [29,8,14,20]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
scale=DRAW2(master)
scale=T([1,2])([4.1,6.6])(scale)

#Garage1

master = assemblyDiagramInit([4,5,2])([[.1,2.5,3.2,.1],[.3,1,2.3,2,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)



toMerge = 3
diagram2 = assemblyDiagramInit([1,1,2])([[2],[.1],[2.2,.5]])
master = diagram2cell(diagram2,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)



toRemove = [39,12,22,14,24,16,26,36,34,32,30]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
garage1=DRAW2(master)
garage1=T([1,2])([7.6,4.8])(garage1)

#Garage2

master = assemblyDiagramInit([4,4,2])([[.1,4,4.4,.1],[.1,0.8,5.4,.1],[.1,2.7]])
V,CV= master
hpc1 = SKEL_1(STRUCT(MKPOLS(master)))
hpc1 = cellNumbering (master,hpc1)(range(len(CV)),CYAN,2)
hpc1=T([1,2])([13.3,4.1])(hpc1)


toRemove = [13,21,11,19,5]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
garage2=DRAW2(master)
garage2=T([1,2])([13.3,4.1])(garage2)



#Soggiorno2
master = assemblyDiagramInit([3,3,2])([[.1,3.3,.1],[.1,6.5,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

toRemove = [9,3,15,11]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno2=DRAW2(master)
soggiorno2=T([1])([4.1])(soggiorno2)


#Soggiorno3

master = assemblyDiagramInit([3,4,2])([[.1,5.5,.1],[.1,.4,4.8,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)



toRemove = [5,13,21,15,11,7,23,3,19]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno3=DRAW2(master)
soggiorno3=T([1])([7.6])(soggiorno3)





#Soggiorno4
master = assemblyDiagramInit([3,3,2])([[.1,4,.1],[.1,4,.1],[.1,2.7]])
V,CV= master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)


toRemove = [9,3,11,5]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno4=DRAW2(master)
soggiorno4=T([1])([13.2])(soggiorno4)


#Soggiorno5

master = assemblyDiagramInit([3,7,2])([[.1,5.5,.1],[.1,1.5,.3,2,0.6,.2,.1],[.1,2.7]])
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




toRemove = [23,21,19,17,15,40,38,42,45]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
soggiorno5=DRAW2(master)
soggiorno5=T([1,2])([7.6,0.1])(soggiorno5)

#Remove

master = assemblyDiagramInit([3,3,2])([[.1,2.1,.1],[.1,2.5,.1],[.1,2.7]])
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
#VIEW(hpc)

toRemove = [15,13,17,29]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
dispensa=DRAW2(master)
dispensa=T([1,2])([4,2.5])(dispensa)

#Inserimento di Curve nel progetto
controlpoints=[
   [[0,0,0],[0.3,0.3,0],[0.3,0.4,0]],
   [[0,0,0.5],[0.3,0.3,0.5],[0.3,0.4,0.5]],
   [[0,0,0.9],[0.3,0.3,0.9],[0.3,0.4,0.9]] ]
dom = larDomain([20])
dom2D = larExtrude1(dom, 20*[1./20])
mapping = larBiquadraticSurface(controlpoints)
patch = larMap(mapping)(dom2D)
curva1=STRUCT(MKPOLS(patch))
curva1=T([1,2])([7.7,9.2])(curva1)

controlpoints=[
   [[0,0,0],[0,0.3,0],[0.3,0,0],[0.3,0.3,0],[0.2,0.2,0]],
  [[0,0,0.5],[0,0.3,0.5],[0.3,0,0.5],[0.3,0.3,0.5],[0.2,0.2,0.5]],
   [[0,0,0.9],[0,0.3,0.9],[0.3,0,0.9],[0.3,0.3,0.9],[0.2,0.2,0.9]] ]
dom = larDomain([20])
dom2D = larExtrude1(dom, 20*[1./20])
mapping = larBiquadraticSurface(controlpoints)
patch = larMap(mapping)(dom2D)
curva2=STRUCT(MKPOLS(patch))

dom = larDomain([20])
dom2D = larExtrude1(dom, 20*[1./20])
mapping = larBiquadraticSurface(controlpoints)
patch = larMap(mapping)(dom2D)
curva3=STRUCT(MKPOLS(patch))
curva3=T([2])([-4])(curva3)
curva3=ROTATE([1,2])(PI/2)(curva3)

dom = larDomain([20])
dom2D = larExtrude1(dom, 20*[1./20])
mapping = larBiquadraticSurface(controlpoints)
patch = larMap(mapping)(dom2D)
curva4=STRUCT(MKPOLS(patch))
curva4=T([2])([-4])(curva4)
curva4=ROTATE([1,2])(PI)(curva4)

controlpoints=[
   [[0,0,0],[0.3,0.3,0],[0.3,0.4,0]],
   [[0,0,0.5],[0.3,0.3,0.5],[0.3,0.4,0.5]],
   [[0,0,0.9],[0.3,0.3,0.9],[0.3,0.4,0.9]] ]
dom = larDomain([20])
dom2D = larExtrude1(dom, 20*[1./20])
mapping = larBiquadraticSurface(controlpoints)
patch = larMap(mapping)(dom2D)
curva5=STRUCT(MKPOLS(patch))
curva5=T([1,2])([-13.2,5.3])(curva5)

plan2 = STRUCT([camera1,camera2,bagno,scale,garage1,garage2,soggiorno2,soggiorno3,soggiorno4,soggiorno5,
	remove,dispensa,curva1,curva2,curva3,curva4,curva5])

plan1=exercise1Imp.plan1
plan2=T([1,2])([17.3,0.1])(plan2)
planInf=STRUCT([plan1,plan2])
planSup=STRUCT([plan1,plan2])
planSup=T(3)(2.8)(planSup)
plan=STRUCT([planInf,planSup])
VIEW(plan)

