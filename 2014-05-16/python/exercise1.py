from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *

#Funzioni Utili
DRAW = COMP([VIEW,STRUCT,MKPOLS])
DRAW2 = COMP([STRUCT,MKPOLS])

def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

def creaFinestre(x,z):
 finestra0=CUBOID([x,0.1,z])
 anta1=CUBOID([0.1,0.1,z-0.1])
 anta1=T([2,3])([-0.1,0.1])(anta1)
 anta2=CUBOID([0.1,0.1,z-0.1])
 anta2=T([1,2,3])([x-0.1,-0.1,0.1])(anta2)
 anta3=CUBOID([x,0.1,0.1])
 anta3=T(2)(-0.1)(anta3)
 anta4=CUBOID([x,0.1,0.1])
 anta4=T([2,3])([-0.1,z-0.1])(anta4)
 anta5=CUBOID([0.1,0.1,z-0.1])
 anta5=T([1,2,3])([(x-0.1)/2,-0.1,0.1])(anta5)
 ante=STRUCT([anta1,anta2,anta3,anta4,anta5])
 ante=COLOR(rgbToPlasmColor([153,51,0]))(ante)
 finestra0=COLOR(rgbToPlasmColor([153,203,255]))(finestra0)
 finestra=STRUCT([finestra0,ante])
 return finestra

def creaPorta(x,z):
 porta0=CUBOID([x,0.1,z])
 porta0=COLOR(rgbToPlasmColor([192,64,0]))(porta0)
 cilind_T = CYLINDER([0.025, (10.0/12)*0.1])(50)
 cilind_T=ROTATE([2,3])(PI/2)(cilind_T)
 cilind_T=T([1,3])([x-0.1,z/2])(cilind_T)
 cilind_T=COLOR(rgbToPlasmColor([205,133,63]))(cilind_T)
 porta=STRUCT([porta0,cilind_T])
 
 return porta


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
camera=DRAW2(master)


camera=COLOR(rgbToPlasmColor([255	,204,153]))(camera)
finestra1=creaFinestre(1,1.2)
finestra1=T([1,3])([1.6,1.1])(finestra1)

porta0=creaPorta(0.6,2.2)
porta0=ROTATE([1,2])(PI)(porta0)
porta0=T([1,2,3])([3.65,3.2,0.1])(porta0)

camera1=STRUCT([camera,finestra1,porta0])


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
camera2Temp=DRAW2(master)
camera2Temp=COLOR(rgbToPlasmColor([255	,204,153]))(camera2Temp)

finestra0=creaFinestre(1.2,1.2)
finestra0=ROTATE([1,2])(PI)(finestra0)
finestra0=T([1,2,3])([2.6,3.2,1.1])(finestra0)

porta0=creaPorta(0.6,2.2)

porta0=T([1,3])([3.05,0.1])(porta0)
camera2=STRUCT([camera2Temp,finestra0,porta0])
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
bagnoTemp=DRAW2(master)


bagnoTemp=COLOR(rgbToPlasmColor([255	,204,153]))(bagnoTemp)

finestra0=creaFinestre(1,1.2)
finestra0=ROTATE([1,2])(-PI/2)(finestra0)
finestra0=T([2,3])([1.5,1.1])(finestra0)

porta0=creaPorta(0.9,2.2)
porta0=ROTATE([1,2])(PI/2)(porta0)
porta0=T([1,2,3])([2.4,0.5,0.1])(porta0)

bagno=STRUCT([bagnoTemp,finestra0,porta0])

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
toRemove = [34,28,9,14,19,31,37]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW2(master)
stireriaTemp=DRAW2(master)
stireriaTemp=COLOR(rgbToPlasmColor([255	,204,153]))(stireriaTemp)

finestra0=creaFinestre(1,1.2)
finestra0=ROTATE([1,2])(-PI)(finestra0)
finestra0=T([1,2,3])([2.5,2.3,1.1])(finestra0)

porta0=creaPorta(1,2.2)
porta0=T([1,3])([1.5,0.1])(porta0)

stireria=STRUCT([stireriaTemp,finestra0,porta0])
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
cucinaTemp=DRAW2(master)
cucinaTemp=COLOR(rgbToPlasmColor([255	,204,153]))(cucinaTemp)

finestra0=creaFinestre(1,1.2)
finestra0=ROTATE([1,2])(PI/2)(finestra0)
finestra0=T([1,2,3])([4.2,1.6,1.1])(finestra0)

porta0=creaPorta(1,2.2)
porta0=ROTATE([1,2])(PI)(porta0)
porta0=T([1,2,3])([2.1,4.2,0.1])(porta0)


porta1=creaPorta(1,2.2)
porta1=T([1,3])([1.1,0.1])(porta1)


porta2=creaPorta(1.2,2.2)
porta2=ROTATE([1,2])(-PI/2)(porta2)
porta2=T([2,3])([3.8,0.1])(porta2)


cucina=STRUCT([cucinaTemp,finestra0,porta0,porta1,porta2])
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
bagnoTemp2=DRAW2(master)
bagnoTemp2=COLOR(rgbToPlasmColor([255	,204,153]))(bagnoTemp2)

porta0=creaPorta(1,2.2)
porta0=ROTATE([1,2])(PI)(porta0)
porta0=T([1,2,3])([2.5,1.4,0.1])(porta0)

bagno2=STRUCT([porta0,bagnoTemp2])
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
scaleTemp=DRAW2(master)
scaleTemp=COLOR(rgbToPlasmColor([255	,204,153]))(scaleTemp)

finestra0=creaFinestre(1.2,1.2)
finestra0=ROTATE([1,2])(PI)(finestra0)
finestra0=T([1,2,3])([2.4,1.6,1.1])(finestra0)

porta0=creaPorta(1,2.2)
porta0=ROTATE([1,2])(PI/2)(porta0)
porta0=T([1,2,3])([3.6,0.3,0.1])(porta0)

scale=STRUCT([scaleTemp,finestra0,porta0])


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
remove=COLOR(rgbToPlasmColor([255	,204,153]))(remove)

finestra0=creaFinestre(1.2,1.2)
finestra0=ROTATE([1,2])(PI)(finestra0)
finestra0=T([1,2,3])([2.4,1.6,1.1])(finestra0)

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
soggiornoTemp2=DRAW2(master)

soggiornoTemp2=COLOR(rgbToPlasmColor([255	,204,153]))(soggiornoTemp2)

finestra0=creaFinestre(1.6,2.3)
finestra0=T([1])(0.95)(finestra0)
soggiorno2=STRUCT([soggiornoTemp2,finestra0])
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
soggiornoTemp3=DRAW2(master)
soggiornoTemp3=COLOR(rgbToPlasmColor([255	,204,153]))(soggiornoTemp3)
finestra0=creaFinestre(2,2.3)
finestra0=T(1)(0.4)(finestra0)

finestra1=creaFinestre(2,2.3)
finestra1=T(1)(3.3)(finestra1)

soggiorno3=STRUCT([soggiornoTemp3,finestra0,finestra1])

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
soggiornoTemp4=DRAW2(master)
soggiornoTemp4=COLOR(rgbToPlasmColor([255	,204,153]))(soggiornoTemp4)



finestra0=creaFinestre(2,2.3)
finestra0=T(1)(1.1)(finestra0)


soggiorno4=STRUCT([soggiornoTemp4,finestra0])


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
remove2Temp=DRAW2(master)

remove2Temp=COLOR(rgbToPlasmColor([255	,204,153]))(remove2Temp)

porta0=creaPorta(1.1,2.2)
porta0=ROTATE([1,2])(-PI/2)(porta0)
porta0=T([2,3])([5.1,0.1])(porta0)

finestra0=creaFinestre(1.2,1.2)
finestra0=ROTATE([1,2])(PI)(finestra0)
finestra0=T([1,2,3])([2.5,5.2,1.1])(finestra0)

remove2=STRUCT([remove2Temp,finestra0,porta0])
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
est1= CUBOID([4,6,0.2])
est1=T([1,2,3])([13.2,-5.5,-0.1])(est1)

est2= CUBOID([14.7,2.8,0.2])
est2=T([1,2,3])([-1.5,-2.3,-0.1])(est2)

est3=CUBOID([14.5,0.2,0.2])
est3=T([1,2,3])([-1.5,-2.5,-0.1])(est3)
est3=COLOR(rgbToPlasmColor([147,147,147]))(est3)

est4=CUBOID([0.2,3.2,0.2])
est4=T([1,2,3])([13,-5.5,-0.1])(est4)
est4=COLOR(rgbToPlasmColor([147,147,147]))(est4)

est5=CUBOID([4,0.2,0.2])
est5=T([1,2,3])([13,-5.7,-0.1])(est5)
est5=COLOR(rgbToPlasmColor([147,147,147]))(est5)

est6=CUBOID([0.5,1.7,0.5])
est6=T([1,2,3])([16.9,-7,-0.1])(est6)
est6=COLOR(rgbToPlasmColor([255	,204,153]))(est6)



colonna1=CUBOID([0.5,0.5,2.8])
colonna1=T([1,2])([3,-1])(colonna1)
colonna2=CUBOID([0.5,0.5,2.8])
colonna2=T([1,2])([7,-1])(colonna2)
colonna3=CUBOID([0.5,0.5,2.8])
colonna3=T([1,2])([10.5,-1])(colonna3)
colonna4=CUBOID([0.5,0.5,2.8])
colonna4=T([1,2])([14,-1])(colonna4)
colonna5=CUBOID([0.5,0.5,2.8])
colonna5=T([1,2])([3.9,10])(colonna5)
colonne=STRUCT([colonna1,colonna2,colonna3,colonna4,colonna5])


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

baseEsterno=STRUCT([est1,est2])
esterno=STRUCT([ext4,ext5,colonne])


#ParteSuperiore
parteSup=CUBOID([17.4,10.3,0.7])
parteSup=T([2,3])([-2,2.8])(parteSup)
#Tetto

tetto_vertici = [ [0,0], [10.3,0], [5.15,1.5], ];
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
toRemove = [80,88,84,86,24,26,28,30,35,37,39,41,46,48,50,52,58,60,62,64,13,15,17,19,82]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
cameraManTemp=DRAW2(master)



cameraManTemp=COLOR(rgbToPlasmColor([255	,204,153]))(cameraManTemp)

finestra0=creaFinestre(1,1.2)
finestra0=T([1,3])([3.7,1])(finestra0)

porta0=creaPorta(1.1,2.1)
porta0=T([1,3])([0.6,0.1])(porta0)

porta1=creaPorta(1.1,2.1)
porta1=ROTATE([1,2])(PI)(porta1)
porta1=T([1,2,3])([1.7,5.3,0.1])(porta1)

porta2=creaPorta(1.3,2.1)
porta2=ROTATE([1,2])(-PI/2)(porta2)
porta2=T([2,3])([1.9,0.1])(porta2)

porta3=creaPorta(1.3,2.1)
porta3=ROTATE([1,2])(-PI/2)(porta3)
porta3=T([2,3])([5.2,0.1])(porta3)

cameraMan=STRUCT([cameraManTemp,finestra0,porta0,porta1,porta2,porta3])


cameraMan=T([1])([4.1])(cameraMan)


#bagnoMan
master = assemblyDiagramInit([5,5,2])([[.1,0.5,1.5,2,.1],[.1,0.5,1.3,1.5,.1],[.1,2.3]])
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
bagnoManTemp=DRAW2(master)

bagnoManTemp=COLOR(rgbToPlasmColor([255	,204,153]))(bagnoManTemp)

finestra0=creaFinestre(1.6,1.2)
finestra0=T([1,3])([0.5,1])(finestra0)

bagnoMan=STRUCT([bagnoManTemp,finestra0])




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
muro=CUBOID([0.1,1.8,2.4])
muro=T(2)(3.5)(muro)

#muro2
muro2=CUBOID([4.5,0.1,2.4])
muro2=T(2)(5.3)(muro2)


#ParteSupTettoMansarda
ParteSupTettoMansarda=CUBOID([10,9.7,0.3])
ParteSupTettoMansarda=T([2,3])([-0.7,2.4])(ParteSupTettoMansarda)

#TettoMansarda
tettoM_vertici = [ [0,0], [9.7,0], [4.85,1.5], ];
tettoM_num_lati = [range(1,4)] 
tettoM_2D = MKPOL([tettoM_vertici, tettoM_num_lati, None])
#Porto in 2,5D
tettoM = PROD([tettoM_2D, Q(10)])
tettoM=ROTATE([2,3])(PI/2)(tettoM)
tettoM=ROTATE([1,2])(PI/2)(tettoM)
tettoM=T([2,3])([-0.7,2.7])(tettoM)



#Sottotetto
master = assemblyDiagramInit([5,5,2])([[.1,3,.1,6.7,.1],[.1,1,1,1.4,.1],[.1,2.3]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc= cellNumbering (master,hpc)(range(len(CV)),CYAN,2)

toMerge = 25
diagram0 = assemblyDiagramInit([1,1,2])([[3],[.1],[2.2,.2]])
master = diagram2cell(diagram0,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


#Rimozione
toRemove = [11,21,30,49,13,15,17,36,34,32]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
sottotetto=DRAW2(master)
sottotetto=T([2])(5.4)(sottotetto)



tettoM=COLOR(rgbToPlasmColor([206,48,24]))(tettoM)
ParteSupTettoMansarda=COLOR(rgbToPlasmColor([123,27	,2	]))(ParteSupTettoMansarda)
balcone=COLOR(rgbToPlasmColor([255	,204,153]))(balcone)
muro=COLOR(rgbToPlasmColor([255	,204,153]))(muro)
muro2=COLOR(rgbToPlasmColor([255	,204,153]))(muro2)



tettoM=COLOR(rgbToPlasmColor([206,48,24]))(tettoM)
ParteSupTettoMansarda=COLOR(rgbToPlasmColor([123,27	,2	]))(ParteSupTettoMansarda)
cameraMan=COLOR(rgbToPlasmColor([255	,204,153]))(cameraMan)
sottotetto=COLOR(rgbToPlasmColor([255	,204,153]))(sottotetto)
bagnoMan=COLOR(rgbToPlasmColor([255	,204,153]))(bagnoMan)
balcone=COLOR(rgbToPlasmColor([255	,204,153]))(balcone)
muro=COLOR(rgbToPlasmColor([255	,204,153]))(muro)
muro2=COLOR(rgbToPlasmColor([255	,204,153]))(muro2)

Mansarda=STRUCT([cameraMan,bagnoMan,balcone,muro,muro2,sottotetto,ParteSupTettoMansarda,tettoM])
#ParteSupTettoMansarda,tettoM

Mansarda=T([1,2,3])([3.9,1.5,2.8])(Mansarda)


#Rimozione
rimozione=CUBOID([10.1,14,3.8])
rimozione=T([1,3])([3.9,2.8])(rimozione)
tetto=DIFFERENCE([tetto,rimozione])
parteSup=DIFFERENCE([parteSup,rimozione])



#Giardino
domain1D = larDomain([32])
domain2D = larIntervals([32,48],'simplex')([1,1])
b1 = BEZIER(S1)([[-1.5,4], [0.5,-7], [6.5,-7], [7.5,0]])
b2=BEZIER(S1)([[-1.5,4], [0.5,5], [6.5,5], [7.5,0]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
giardino1 = PROD([path, Q(2.8)])
giardino1=T([2,3])([-14.3,-2.9])(giardino1)


b1 = BEZIER(S1)([[9.5,0], [10.5,-7], [16.5,-7], [17.3,4]])
b2=BEZIER(S1)([[9.5,0], [9.5,5], [16.5,5], [17.3,4]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
giardino2 = PROD([path, Q(2.8)])
giardino2=T([2,3])([-14.3,-2.9])(giardino2)



giardino3=CUBOID([18.8,6,2.8])
giardino3=T([1,2,3])([-1.5,-10.4,-2.9])(giardino3)


giardino4=CUBOID([13,6,2.8])
giardino4=T([1,2,3])([2,-14,-2.9])(giardino4)

#Assemblo
giardino=STRUCT([giardino1,giardino2,
	giardino4])
giardino=T([2])(3.4)(giardino)
giardino3=T([2])(3.4)(giardino3)

#GiardinoREMOVE
domain1D = larDomain([32])
domain2D = larIntervals([32,48],'simplex')([1,1])
b1 = BEZIER(S1)([[-1.3,4], [0.7,-7], [6.3,-7], [7.3,0]])
b2=BEZIER(S1)([[-1.3,4], [0.7,5], [6.3,5], [7.3,0]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
giardinoR1 = PROD([path, Q(0.1)])
giardinoR1=T([2,3])([-14.3,0.1])(giardinoR1)



b1 = BEZIER(S1)([[9.7,0], [10.7,-7], [16.3,-7], [17.1,4]])
b2=BEZIER(S1)([[9.7,0], [9.7,5], [16.3,5], [17.1,4]])
controls = [b1,b2]
mapping = BEZIER(S2)(controls)
path = STRUCT(MKPOLS(larMap(mapping)(domain2D)))
giardinoR2 = PROD([path, Q(0.1)])
giardinoR2=T([2,3])([-14.3,0.1])(giardinoR2)



giardinoR3=CUBOID([18.4,4.5,0.1])
giardinoR3=T([1,2,3])([-1.3,-10.5,0.1])(giardinoR3)


giardinoR4=CUBOID([12.8,6,0.1])
giardinoR4=T([1,2,3])([2.1,-14,0.1])(giardinoR4)

#Assemblo
giardinoR=STRUCT([giardinoR1,giardinoR2,
        giardinoR4])
giardinoR=T([2])(3.4)(giardinoR)
giardinoR3=T([2])(3.4)(giardinoR3)
giardinoRemove=STRUCT([giardinoR,giardinoR3])
giardinoRemove=T(3)(-0.2)(giardinoRemove)
giardinoRemove=COLOR(rgbToPlasmColor([34,139,34	]))(giardinoRemove)



#Assemblo

principale=STRUCT([camera1,camera2,bagno,stireria,scale,soggiorno2,soggiorno3,soggiorno4,cucina
	,bagno2,remove,remove2,remove3])

#Coloro

camino=COLOR(rgbToPlasmColor([240,248,255]))(camino)
scalinata=COLOR(rgbToPlasmColor([153,51,0]))(scalinata)
scalinata2=COLOR(rgbToPlasmColor([229,228,226]))(scalinata2)
parteSup=COLOR(rgbToPlasmColor([123	,27	,2	]))(parteSup)
esterno=COLOR(rgbToPlasmColor([255	,204,153]))(esterno)
baseEsterno=COLOR(rgbToPlasmColor([255	,204,153]))(baseEsterno)
tetto=COLOR(rgbToPlasmColor([206,48,24]))(tetto)
giardino=COLOR(rgbToPlasmColor([184	,115	,51]))(giardino)
giardino3= COLOR(rgbToPlasmColor([255	,204,153]))(giardino3)
est3=COLOR(rgbToPlasmColor([147,147,147]))(est3)

#Creo la siepe
pianta= CUBOID([0.5,0.5,0.8])
Tp=T(2)(0.6)
piante1=STRUCT(NN(8)([Tp, pianta]))
piante1=T([1,2])([-1.3,-8.2])(piante1)

pianta2=T([1,2])([-1.1,-8.2])(pianta)
pianta3=T([1,2])([-1.0,-8.8])(pianta)
pianta4=T([1,2])([-0.8,-9.4])(pianta)
pianta5=T([1,2])([-0.6,-10])(pianta)
pianta6=T([1,2])([-0.4,-10.6])(pianta)
pianta7=T([1,2])([-0.2,-11.2])(pianta)
pianta8=T([1,2])([0,-11.8])(pianta)
pianta9=T([1,2])([0.2,-12.4])(pianta)
pianta10=T([1,2])([0.6,-13])(pianta)
pianta11=T([1,2])([0.9,-13.6])(pianta)
pianta12=T([1,2])([1.3,-14.2])(pianta)
pianta13=T([1,2])([1.7,-14.8])(pianta)
pianta14=T([1,2])([2.3,-15.4])(pianta)
pianta15=T([1,2])([2.8,-15.6])(pianta)
pianta16=T([1,2])([3.4,-15.8])(pianta)
pianta17=T([1,2])([4.0,-15.8])(pianta)
pianta18=T([1,2])([4.6,-15.6])(pianta)
pianta19=T([1,2])([5.1,-15.4])(pianta)
pianta20=T([1,2])([5.4,-14.9])(pianta)
pianta21=T([1,2])([5.8,-14.4])(pianta)
pianta22=T([1,2])([6.2,-13.8])(pianta)
pianta23=T([1,2])([6.4,-13.2])(pianta)
pianta24=T([1,2])([6.6,-12.6])(pianta)
pianta25=T([1,2])([6.8,-12])(pianta)
pianta26=T([1,2])([7,-11.4])(pianta)
pianta27=T([1,2])([7,-10.6])(pianta)
pianta28=T([1,2])([9.3,-10.6])(pianta)



siepe1=STRUCT([pianta18,pianta19,pianta20,pianta21,pianta22,pianta23,pianta24,pianta25])
siepe2=STRUCT([pianta18,pianta19,pianta20,pianta21,pianta22,pianta23,pianta24,pianta25])
siepe2=T(1)(9)(siepe2)
siepe3=STRUCT([pianta7,pianta8,pianta9,pianta10,pianta11,pianta12,pianta13,pianta14,pianta15,pianta16,pianta17])
siepe4=STRUCT([pianta7,pianta8,pianta9,pianta10,pianta11,pianta12,pianta13,pianta14,pianta15,pianta16,pianta17])
siepe4=T(1)(9.5)(siepe4)
siepe5=STRUCT([pianta5,pianta6,pianta7,pianta8,pianta9])
siepe6=STRUCT([pianta5,pianta6,pianta7,pianta8,pianta9])
siepe6=ROTATE([1,3])(PI)(siepe6)
siepe6=T([1,2,3])([16.6,1,0.8])(siepe6)
siepe7=STRUCT([pianta2,pianta3,pianta4])
siepe8=STRUCT([pianta2,pianta3])
siepe8=ROTATE([1,3])(PI)(siepe8)
siepe8=T([1,2,3])([16.2,0.5,0.8])(siepe8)




siepe=STRUCT([siepe1,siepe2,siepe3,siepe4,siepe5,siepe6,siepe7,siepe8,piante1,
        pianta26,pianta27,pianta28])
siepe=COLOR(rgbToPlasmColor([128 ,128,0]))(siepe)

plan1 = STRUCT([principale,scalinata,scalinata2,esterno,baseEsterno,parteSup,giardino,camino,
	Mansarda,tetto,giardino3,giardinoRemove,siepe,est3,est4,est5,est6])
#tetto,Mansarda

#Visualizzo
VIEW(plan1)








