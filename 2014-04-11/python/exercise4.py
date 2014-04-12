import urbanImport
from pyplasm import*

def rgbToPlasmColor(color):
	return [color[0]/255., color[1]/255., color[2]/255.]

strada1_vertici = [ [0,0], [150,0], [0,3], [150,3] ];
strada1_num_lati = [range(1,5)] 
strada1_25D = MKPOL([strada1_vertici, strada1_num_lati, None])
strada1 = PROD([strada1_25D, Q(0.5)])
strada1=T([2,3])([16,1])(strada1)

strada2=PROD([strada1_25D, Q(0.5)])
strada2=T([2,3])([38,1])(strada2)

strada3_vertici = [ [0,0], [3,0], [0,150], [3,150] ];
strada3_num_lati = [range(1,5)] 
strada3_25D = MKPOL([strada3_vertici, strada3_num_lati, None])
strada3 = PROD([strada3_25D, Q(0.5)])
strada3=T([1,3])([61,1])(strada3)

strada4=PROD([strada3_25D, Q(0.5)])
strada4=T([1,3])([87,1])(strada4)

strada5_vertici = [ [0,0], [3,0], [0,110], [3,110] ];
strada5_num_lati = [range(1,5)] 
strada5_25D = MKPOL([strada5_vertici, strada5_num_lati, None])
strada5 = PROD([strada5_25D, Q(0.5)])
strada5=T([1,3])([147,1])(strada5)

strada6_vertici = [ [0,0], [87,0], [0,3], [87,3] ];
strada6_num_lati = [range(1,5)] 
strada6_25D = MKPOL([strada6_vertici, strada6_num_lati, None])
strada6 = PROD([strada6_25D, Q(0.5)])
strada6=T([1,2,3])([61,57,1])(strada6)

strada7 = PROD([strada6_25D, Q(0.5)])
strada7=T([1,2,3])([61,85,1])(strada7)

strada8 = PROD([strada6_25D, Q(0.5)])
strada8=T([1,2,3])([61,107,1])(strada8)

strada9_vertici = [ [0,0], [3,0], [0,60], [3,60] ];
strada9_num_lati = [range(1,5)] 
strada9_25D = MKPOL([strada9_vertici, strada9_num_lati, None])
strada9 = PROD([strada9_25D, Q(0.5)])
strada9=T([1,3])([117,1])(strada9)

strada10_vertici = [ [0,0], [3,0], [0,40], [3,40] ];
strada10_num_lati = [range(1,5)] 
strada10_25D = MKPOL([strada10_vertici, strada10_num_lati, None])
strada10 = PROD([strada10_25D, Q(0.5)])
strada10=T([1,3])([33,1])(strada10)

strada11=PROD([strada10_25D, Q(0.5)])
strada11=T(3)(1)(strada11)

strade=STRUCT([strada1,strada2,strada3,strada4,strada5,strada6,strada7,strada8,strada9,strada10,strada11])
strade=COLOR(rgbToPlasmColor([47,47,47]))(strade)



#Creo gli alberi

tronco = CYLINDER([2, (10.0/12)*5])(50)
tronco = COLOR(rgbToPlasmColor([101, 67, 33]))(tronco)
foglie = SPHERE(4)([60,60])
foglie = COLOR(rgbToPlasmColor([85,104,50]))(foglie)

foglie = T(3)(5)(foglie)
albero = STRUCT([tronco,foglie])

T1=T(1)(10)
T2=T(2)(10)
alberi1=STRUCT(NN(5)([T1, STRUCT(NN(2)([T2, albero]))]))
alberi1=T([1,2,3])([90,83,1])(alberi1)

T3=T(1)(10)
alberi2=STRUCT(NN(6)([T3, albero]))
alberi2=T([1,2,3])([-5,45,1])(alberi2)

T4=T(2)(10)
alberi3=STRUCT(NN(10)([T4, albero]))
alberi3=T([1,2,3])([56,45,1])(alberi3)


urban=STRUCT([urbanImport.struttura,strade,alberi1,alberi2,alberi3])


VIEW(urban)