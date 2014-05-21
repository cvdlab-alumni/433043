from pyplasm import *
import os,sys
sys.path.insert(0, 'lib/py/')
from lar2psm import *
from larcc import *
from sysml import *


#Funzione per la numerazione di celle
def NumberCell(master,hpc):
    hpc = cellNumbering(master,hpc)(range(len(master[1])),CYAN,2)
    return hpc


#Prende in input una lista di Diagram da inserire, il master e la lista di celle
#in cui inserire i vari Diagram. Come ulteriore parametro gli si da in input
#la lista di celle da rimuovere

def InserisciEliminaDiagram(diagram,master,toMerge,toRemove):
 master = master[0],[cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
 ToMerge=list.sort(toMerge)
 ToMerge=list.reverse(toMerge)	
 cont=0
 for k in toMerge:
    master = diagram2cell(diagram[cont],master,k)
    cont=cont+1;
 hpc = SKEL_1(STRUCT(MKPOLS(master)))
 hpc = NumberCell(master, hpc)


 return hpc

#Esempio di utilizzo
master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = NumberCell(master,hpc)


VIEW(hpc)




diagram1 = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
diagram2 = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
diagram3 = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
diagram4 = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])

ToRemove=[13,33,37,17]
ToMerge=([11,29,17,35])

hpc=InserisciEliminaDiagram([diagram1,diagram2,diagram3,diagram4],master,ToMerge,ToRemove)
VIEW(hpc)



