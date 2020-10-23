#sim stat of lights
#sim presence of # cars on road
#sim exit points
#generalize to real map
#direction 0 is up for all
#direction 0 is right for all
# . --A-- . --B-- . --C-- . 
# |:::::::|:::::::|:::::::|
# D:::::::E:::::::F:::::::G
# |:::::::|:::::::|:::::::|
# . --H-- . --I-- . --J-- . 
# |:::::::|:::::::|:::::::|
# K:::::::L:::::::M:::::::N
# |:::::::|:::::::|:::::::|
# . --O-- . --P-- . --Q-- . 

#arg1 = frames arg2 = cars

import warnings
warnings.filterwarnings("ignore")
import random
import networkx as nx

import numpy as np
import matplotlib.pyplot as plt
import seaborn.apionly as sns
import matplotlib.animation
import sys



if len(sys.argv) != 3:
	print("Incorrect Usage, Expected:\npython3 road3.py <number_of_frames> <number_of_cars>")
	exit()

gr = nx.Graph()
gr.add_nodes_from([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47])

edge_list = [(1,2),(3,4),(5,6),(9,10),(11,12),(13,14),(8,16),(9,17),(10,18),(11,19),(12,20),(13,21),(14,22),(15,23),(17,18),(19,20),(21,22),(25,26),(27,28),(29,30),(24,32),(25,33),(26,34),(27,35),(28,36),(29,37),(30,38),(31,39),(33,34),(35,36),(37,38),(41,42),(43,44),(45,46)]
#edge_list = [(1,2),(3,4),(5,6),(0,8),(1,9),(2,10),(3,11),(4,12),(5,13),(6,14),(7,15),(9,10),(11,12),(13,14),(8,16),(9,17),(10,18),(11,19),(12,20),(13,21),(14,22),(15,23),(17,18),(19,20),(21,22)]
#pos = {0:[0,1],1:[0.1,1],2:[0.333,1],3:[0.433,1],4:[0.666,1],5:[0.766,1],6:[1,1],7:[1.1,1],8:[0,0.666],9:[0.1,0.666],10:[0.333,0.666],11:[0.433,0.666],12:[0.666,0.666],13:[0.766,0.66],14:[1,0.666],15:[1.1,0.666],16:[0,0.333],17:[0.1,0.333],18:[0.333,0.333],19:[0.433,0.333],20:[0.666,0.333],21:[0.766,0.333],22:[1,0.333],23:[1.1,0.333]}
pos = {0:[0,1],1:[0.1,1],2:[0.333,1],3:[0.433,1],4:[0.666,1],5:[0.766,1],6:[1,1],7:[1.1,1],8:[0,0.9],9:[0.1,0.9],10:[0.333,0.9],11:[0.433,0.9],12:[0.666,0.9],13:[0.766,0.9],14:[1,0.9],15:[1.1,0.9],16:[0,0.666],17:[0.1,0.666],18:[0.333,0.666],19:[0.433,0.666],20:[0.666,0.666],21:[0.766,0.666],22:[1,0.666],23:[1.1,0.666],24:[0,0.566],25:[0.1,0.566],26:[0.333,0.566],27:[0.433,0.566],28:[0.666,0.566],29:[0.766,0.566],30:[1,0.566],31:[1.1,0.566],32:[0,0.333],33:[0.1,0.333],34:[0.333,0.333],35:[0.433,0.333],36:[0.666,0.333],37:[0.766,0.333],38:[1,0.333],39:[1.1,0.333],40:[0,0.233],41:[0.1,0.233],42:[0.333,0.233],43:[0.433,0.233],44:[0.666,0.233],45:[0.766,0.233],46:[1,0.233],47:[1.1,0.233]}
fig, ax = plt.subplots(figsize=(6,4))
zA,oA,zB,oB,zC,oC,zD,oD,zE,oE,zF,oF,zG,oG,zH,oH,zI,oI,zJ,oJ,zK,oK,zL,oL,zM,oM,zN,oN,zO,oO,zP,oP,zQ,oQ = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q = [zA,oA],[zB,oB],[zC,oC],[zD,oD],[zE,oE],[zF,oF],[zG,oG],[zH,oH],[zI,oI],[zJ,oJ],[zK,oK],[zL,oL],[zM,oM],[zN,oN],[zO,oO],[zP,oP],[zQ,oQ]

cars = int(sys.argv[2])
print("#######{}".format(cars))
carcap = 20
direction =[0]*cars

roads = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q]
roadnames = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"]

#for later
onroad = []
offroad = []

def start():	
	#A.clear();B.clear();C.clear();D.clear();E.clear();F.clear();G.clear();H.clear();I.clear();
	#J.clear();K.clear();L.clear();M.clear();N.clear();O.clear();P.clear();Q.clear();
	for i in range(cars): #produce cars
		num = random.randint(0,len(roadnames)-1)
		dir = random.randint(0,1)
		direction[i] = dir
		roads[num][dir].append(i)

	print("******Initial Arrangement******")
	for i in range(len(roadnames)):
		print("L{}: {}\nR{}: {}".format(roadnames[i],roads[i][0],roadnames[i],roads[i][0]))
#we need to have left and rigt lane go one at a ttime at the same time

file = open("carstats.txt",'w')

def update(num):
	ax.clear()
	#@@@@A@@@@
	#at A, can only go forward to B or turn right to E :0
	#at A, can only turn left onto D :1
	print("A")
	if len(A[0]) > 0:
		curr = A[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("AAction: {}".format(act))
		if act == 0:
			if len(zB) != carcap:
				print("acar: {}".format(curr))
				zB.append(curr)
				zA.remove(curr)
		else:
			if len(oE) != carcap:
				print("acar: {}".format(curr))
				direction[curr] = 1
				oE.append(curr)
				zA.remove(curr)

	if len(A[1]) > 0:
		if len(oD) != carcap:
				
			curr = A[1][0]
			print("Direction: {}".format(direction[curr]))
			print("1 action available")
			oD.append(curr)
			oA.remove(curr)
	#@@@B@@@
	#at B, can only go forward to C or turn right to F :0
	#at B, can only go forward to A or turn left to E :1
	print("\nB")
	if len(B[0]) > 0:
		curr = B[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("BAction: {}".format(act))
		if act == 0: #go forward
			if len(zC) != carcap:	
				print("bcar: {}".format(curr))
				zC.append(curr)
				zB.remove(curr)
		else:
			if len(oF) != carcap:			
				print("bcar: {}".format(curr))
				direction[curr] = 1
				oF.append(curr)
				zB.remove(curr)
				
	if len(B[1]) > 0:
		curr = B[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("BAction: {}".format(act))
		if act == 0: #go forward
			if len(oA) != carcap:
				print("bcar: {}".format(curr))
				oA.append(curr)
				oB.remove(curr)
		else:
			if len(oE) != carcap:
				print("bcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oE.append(curr)
				oB.remove(curr)
				
	#@@@C@@@
	#at C, can only turn right to G :0
	#at C, can only go forward to B or turn left to F :1
	print("\nC")
	if len(C[0]) > 0:
		if len(oG) != carcap:	
			curr = C[0][0]
			print("Direction: {}".format(direction[curr]))
			print("1 action available")
			direction[curr] = 1
			oG.append(curr)
			zC.remove(curr)

	if len(C[1]) > 0:
		curr = C[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("CAction: {}".format(act))
		if act == 0: #go forward
			if len(oB) != carcap:
				print("ccar: {}".format(curr))
				oB.append(curr)
				oC.remove(curr)
		else:
			if len(oF) != carcap:
				print("ccar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oF.append(curr)
				oC.remove(curr)
	#@@@D@@@
	#at D, can only turn right to A :0
	#at D, can only go forward to K or turn left to H :1
	print("\nD")
	if len(D[0]) > 0:
		if len(zA) != carcap:
			print("Direction: {}".format(direction[D[0][0]]))
			print("1 action available")
			direction[D[0][0]] = 0 #redundancy
			zA.append(D[0][0])
			zD.remove(D[0][0])

	if len(D[1]) > 0:
		act = random.randint(0,1)
		print("Direction: {}".format(direction[D[1][0]]))
		print("DAction: {}".format(act))
		if act == 0: #go forward
			if len(oK) != carcap:
				print("dcar: {}".format(D[1][0]))
				oK.append(D[1][0])
				oD.remove(D[1][0])
		else:
			if len(zH) != carcap:
				print("dcar: {}".format(D[1][0]))
				direction[D[1][0]] = 0
				zH.append(D[1][0])
				oD.remove(D[1][0])
	#@@@E@@@
	#at E, can only turn right to B or left to A :0
	#at E, can only go forward to L or turn left to I or left to A :1
	print("\nE")
	if len(E[0]) > 0:
		act = random.randint(0,1)
		print("Direction: {}".format(direction[E[0][0]]))
		print("EAction: {}".format(act))
		if act == 0: #right
			if len(zB) != carcap:
				print("ecar: {}".format(E[0][0]))
				direction[E[0][0]] = 0 #redundancy
				zB.append(E[0][0])
				zE.remove(E[0][0])
		else:# left
			if len(oA) != carcap:
				print("ecar: {}".format(E[0][0]))
				direction[E[0][0]] = 1
				oA.append(E[0][0])
				zE.remove(E[0][0])

	if len(E[1]) > 0:
		act = random.randint(0,2)
		print("Direction: {}".format(direction[E[1][0]]))
		print("EAction: {}".format(act))
		if act == 0: #forward
			if len(oL) != carcap:
				print("ecar: {}".format(E[1][0]))
				direction[E[1][0]] = 1 #redundancy
				oL.append(E[1][0])
				oE.remove(E[1][0])
		elif act == 1: # right
			if len(oE) != carcap:
				print("ecar: {}".format(E[1][0]))
				direction[E[1][0]] = 0
				zI.append(E[1][0])
				oE.remove(E[1][0])
		else:
			if len(oH) != carcap:
				print("ecar: {}".format(E[1][0]))
				direction[E[1][0]] = 1 #redundancy
				oH.append(E[1][0])
				oE.remove(E[1][0])
	#@@@F@@@
	#at F, can only turn right to C or left to B :0
	#at F, can only go forward to M or go right to I or go left to J :1
	print("\nF")
	if len(F[0]) > 0:
		act = random.randint(0,1)
		print("Direction: {}".format(direction[F[0][0]]))
		print("FAction: {}".format(act))
		if act == 0:
			if len(zC) != carcap:
				print("fcar: {}".format(F[0][0]))
				direction[F[0][0]] = 0 #redundancy
				zC.append(F[0][0])
				zF.remove(F[0][0])
		else:
			if len(oB) != carcap:
				direction[F[0][0]] = 1
				oB.append(F[0][0])
				zF.remove(F[0][0])
	if len(F[1]) > 0:
		act = random.randint(0,2)
		print("Direction: {}".format(direction[F[1][0]]))
		print("FAction: {}".format(act))
		if act == 0: #forward
			if len(oM) != carcap:
				print("fcar: {}".format(F[1][0]))
				direction[F[1][0]] = 1 #redundancy 
				oM.append(F[1][0])
				oF.remove(F[1][0])
		elif act == 1: #right
			if len(oD) != carcap:
				print("fcar: {}".format(F[1][0]))
				direction[F[1][0]] = 1 #redundancy
				oD.append(F[1][0])
				oF.remove(F[1][0])
		else:
			if len(zJ) != carcap:
				print("fcar: {}".format(F[1][0]))
				direction[F[1][0]] = 0
				zJ.append(F[1][0])
				oF.remove(F[1][0])
	#@@@G@@@
	#at G, can only turn left to C  :0
	#at G, can only go forward to N or turn right to J :1
	print("\nG")
	if len(G[0]) > 0:
		if len(oC) != carcap:
			print("1 action available")
			direction[G[0][0]] = 1
			oC.append(G[0][0])
			zG.remove(G[0][0])

	if len(G[1]) > 0:
		act = random.randint(0,1)
		print("Direction: {}".format(direction[G[1][0]]))
		print("GAction: {}".format(act))
		if act == 0: #forward
			if len(oN) != carcap:
				print("gcar: {}".format(G[1][0]))
				direction[G[1][0]] = 1 #redundancy
				oN.append(G[1][0])
				oG.remove(G[1][0])
		else: #right
			if len(oJ) != carcap:
				print("gcar: {}".format(G[1][0]))
				direction[G[1][0]] = 1 #redundancy
				oJ.append(G[1][0])
				oG.remove(G[1][0])
	#@@@H@@@
	#at H, can only go forward to I, or right to L or left to E :0
	#at H, can only go right to D or left to K :1
	print("\nH")
	if len(H[0]) > 0:
		curr = H[0][0]
		act = random.randint(0,2)
		print("Direction: {}".format(direction[curr]))
		print("HAction: {}".format(act))
		if act == 0: #forward
			if len(zI) != carcap:
				print("hcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zI.append(curr)
				zH.remove(curr)
		elif act == 1: #right
			if len(oL) != carcap:
				print("hcar: {}".format(curr))
				direction[curr] = 1
				oL.append(curr)
				zH.remove(curr)
		else:
			if len(zE) != carcap:
				print("hcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zE.append(curr)
				zH.remove(curr)
	if len(H[1]) > 0:
		curr  = H[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("HAction: {}".format(act))
		if act == 0: #forward
			if len(zD) != carcap:
				print("hcar: {}".format(curr))
				direction[curr] = 0
				zD.append(curr)
				oH.remove(curr)
		else: #right
			if len(oK) != carcap:
				print("hcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oK.append(curr)
				oH.remove(curr)
	#@@@I@@@
	#at I, can only go forward to J, right to M, or left to F :0
	#at I, can only go forward to H, right to E, or left to L :1
	print("\nI")
	if len(I[0]) > 0:
		curr = I[0][0]
		act = random.randint(0,2)
		print("Direction: {}".format(direction[curr]))
		print("IAction: {}".format(act))
		if act == 0: #forward
			if len(zJ) != carcap:
				print("icar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zJ.append(curr)
				zI.remove(curr)
		elif act == 1: #right
			if len(oM) != carcap:
				print("icar: {}".format(curr))
				direction[curr] = 1
				oM.append(curr)
				zI.remove(curr)
		else:
			if len(zF) != carcap:
				print("icar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zF.append(curr)
				zI.remove(curr)

	if len(I[1]) > 0:
		curr = I[1][0]
		act = random.randint(0,2)
		print("Direction: {}".format(direction[curr]))
		print("IAction: {}".format(act))
		if act == 0: #forward
			if len(oH) != carcap:
				print("icar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oH.append(curr)
				oI.remove(curr)
		elif act ==1 : #right
			if len(zE) != carcap:
				print("icar: {}".format(curr))
				direction[curr] = 0
				zE.append(curr)
				oI.remove(curr)
		else: #left
			if len(oL) != carcap:
				print("icar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oL.append(curr)
				oI.remove(curr)
	#@@@J@@@
	#at J, can only turn right to N or left to G :0
	#at J, can only go forward to I or turn right to F or left to M :1
	print("\nJ")
	if len(J[0]) > 0:
		curr = J[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("JAction: {}".format(act))
		if act == 0: #right
			if len(oN) != carcap:
				print("jcar: {}".format(curr))
				direction[curr] = 1
				oN.append(curr)
				zJ.remove(curr)
		else: #left
			if len(zG) != carcap:
				print("jcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zG.append(curr)
				zJ.remove(curr)

	if len(J[1]) > 0:
		curr = J[1][0]
		act = random.randint(0,2)
		print("Direction: {}".format(direction[curr]))
		print("JAction: {}".format(act))
		if act == 0: #forward
			if len(oI) != carcap:
				print("jcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oI.append(curr)
				oJ.remove(curr)
		elif act ==1 : #right
			if len(zF) != carcap:
				print("jcar: {}".format(curr))
				direction[curr] = 0
				zF.append(curr)
				oJ.remove(curr)
		else: #left
			if len(oM) != carcap:
				print("jcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oM.append(curr)
				oJ.remove(curr)
	#@@@K@@@
	#at K, can only go forward to D or go right to H :0
	#at K, can only turn left to O :1
	print("\nK")
	if len(K[0]) > 0:
		curr = K[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("KAction: {}".format(act))
		if act == 0: #forward
			if len(zD) != carcap:
				print("kcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zD.append(curr)
				zK.remove(curr)
		else: #right
			if len(zH) != carcap:
				print("kcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zH.append(curr)
				zK.remove(curr)
	if len(K[1]) > 0:
		if len(zO) != carcap:
			curr = K[1][0]
			print("1 action available")
			direction[curr] = 0
			zO.append(curr)
			oK.remove(curr)
	#@@@L@@@
	#at L, can go forward to E or right to I or left to H :0
	#at L, can turn right to O or left to P :1
	print("\nL")
	if len(L[0]) > 0:
		curr = L[0][0]
		act = random.randint(0,2)
		print("Direction: {}".format(direction[curr]))
		print("LAction: {}".format(act))
		if act == 0: #forward
			if len(zE) != carcap:
				print("lcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zE.append(curr)
				zL.remove(curr)
		elif act == 1: #right
			if len(zI) != carcap:
				print("lcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zI.append(curr)
				zL.remove(curr)
		else:
			if len(oH) != carcap:
				print("lcar: {}".format(curr))
				direction[curr] = 1
				oH.append(curr)
				zL.remove(curr)
	if len(L[1]) > 0:
		curr = L[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("LAction: {}".format(act))
		if act == 0: #right
			if len(oO) != carcap:
				print("lcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oO.append(curr)
				oL.remove(curr)
		else: #left
			if len(zP) != carcap:
				print("lcar: {}".format(curr))
				direction[curr] = 0
				zP.append(curr)
				oL.remove(curr)
	#@@@M@@@
	#at M, can go forward to F or right to J or left to I :0
	#at M, can go right to P or left to Q :1
	print("\nM")
	if len(M[0]) > 0:
		curr = M[0][0]
		act = random.randint(0,2)
		print("Direction: {}".format(direction[curr]))
		print("MAction: {}".format(act))
		if act == 0: #forward
			if len(zF) != carcap:
				print("mcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zF.append(curr)
				zM.remove(curr)
		elif act == 1: #right
			if len(zJ) != carcap:
				print("mcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zJ.append(curr)
				zM.remove(curr)
		else: #left
			if len(oI) != carcap:
				print("mcar: {}".format(curr))
				direction[curr] = 1
				oI.append(curr)
				zM.remove(curr)
	if len(M[1]) > 0:
		curr = M[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("MAction: {}".format(act))
		if act == 0: #right
			if len(oP) != carcap:
				print("mcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oP.append(curr)
				oM.remove(curr)
		else: #left
			if len(zQ) != carcap:
				print("mcar: {}".format(curr))
				direction[curr] = 0
				zQ.append(curr)
				oM.remove(curr)
	#@@@N@@@
	#at N, can go forward to G or turn left to J :0
	#at N, can turn right to Q :1
	print("\nN")
	if len(N[0]) > 0:
		curr = N[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("NAction: {}".format(act))
		if act == 0: #forward
			if len(zG) != carcap:
				print("ncar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zG.append(curr)
				zN.remove(curr)
		else: #left
			if len(oJ) != carcap:
				print("ncar: {}".format(curr))
				direction[curr] = 1
				oJ.append(curr)
				zN.remove(curr)
	if len(N[1]) > 0:
		if len(oQ) != carcap:
			curr = N[1][0]
			print("1 action available")
			direction[curr] = 1 #redundancy
			oQ.append(curr)
			oN.remove(curr)
	#@@@O@@@
	#at O, can go forward to P or turn left to L :0
	#at O, can turn right to K :1
	print("\nO")
	if len(O[0]) > 0:
		curr = O[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("OAction: {}".format(act))
		if act == 0: #forward
			if len(zP) != carcap:
				print("ocar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zP.append(curr)
				zO.remove(curr)
		else: #left
			if len(zL) != carcap:
				print("ocar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zL.append(curr)
				zO.remove(curr)
	if len(O[1]) > 0: #right
		if len(zK) != carcap:
			curr = O[1][0]
			print("1 action available")
			direction[curr] = 0
			zK.append(curr)
			oO.remove(curr)
	#@@@P@@@
	#at P, can go forward to Q or turn left to M :0
	#at P, can go forward to O or turn right to L :1
	print("\nP")
	if len(P[0]) > 0:
		curr = P[0][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("PAction: {}".format(act))
		if act == 0: #forward
			if len(zQ) != carcap:
				print("pcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zQ.append(curr)
				zP.remove(curr)
		else: #left
			if len(zM) != carcap:
				print("pcar: {}".format(curr))
				direction[curr] = 0 #redundancy
				zM.append(curr)
				zP.remove(curr)
	if len(P[1]) > 0:
		curr = P[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("PAction: {}".format(act))
		if act == 0: #forward
			if len(oO) != carcap:
				print("pcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oO.append(curr)
				oP.remove(curr)
		else: #left
			if len(zL) != carcap:
				print("pcar: {}".format(curr))
				direction[curr] = 0
				zL.append(curr)
				oP.remove(curr)
	#@@@Q@@@
	#at Q, can turn left to N :0
	#at Q, can go forward to P or turn right to M :1
	print("\nQ")
	if len(Q[0]) > 0:
		if len(zN) != carcap:
			curr = Q[0][0]
			print("1 action available")
			direction[curr] = 0 #redundancy
			zN.append(curr)
			zQ.remove(curr)
	if len(Q[1]) > 0:
		curr = Q[1][0]
		act = random.randint(0,1)
		print("Direction: {}".format(direction[curr]))
		print("QAction: {}".format(act))
		if act == 0: #forward
			if len(oP) != carcap:
				print("qcar: {}".format(curr))
				direction[curr] = 1 #redundancy
				oP.append(curr)
				oQ.remove(curr)
		else: #left
			if len(zM) != carcap:
				print("qcar: {}".format(curr))
				direction[curr] = 0
				zM.append(curr)
				oQ.remove(curr)

	print("******Arrangement*******")
	for i in range(len(roadnames)):
		print("L{}: {}\nR{}: {}".format(roadnames[i],roads[i][0],roadnames[i],roads[i][1]))
		file.write("{} {} {}\n".format(roadnames[i],len(roads[i][0]),len(roads[i][1])))
	file.write("****************\n")

	greenlist = []#0-4
	bluelist = []#5-9
	yellowlist = []#10-14
	orangelist = []#15-19
	redlist = []#20 --> 
	for i in range(17):
		l= len(roads[i][0])
		if l < 5:
			greenlist.append(edge_list[2*i])
		elif 5 <= l < 10:
			bluelist.append(edge_list[2*i])
		elif 10 <= l < 15:
			yellowlist.append(edge_list[2*i])
		elif 15 <= l < 20:
			orangelist.append(edge_list[2*i])
		else:
			redlist.append(edge_list[2*i])

	for i in range(17):
		l= len(roads[i][1])
		if l < 5:
			greenlist.append(edge_list[2*i+1])
		elif 5 <= l < 10:
			bluelist.append(edge_list[2*i+1])
		elif 10 <= l < 15:
			yellowlist.append(edge_list[2*i+1])
		elif 15 <= l < 20:
			orangelist.append(edge_list[2*i+1])
		else:
			redlist.append(edge_list[2*i+1])
	#add edges
	gr.add_edges_from(greenlist)
	nx.draw_networkx_edges(gr, pos=pos, ax=ax, edge_color="green",width = 10)
	gr.remove_edges_from(greenlist)

	gr.add_edges_from(bluelist)
	nx.draw_networkx_edges(gr, pos=pos, ax=ax, edge_color="blue",width = 10)
	gr.remove_edges_from(bluelist)

	gr.add_edges_from(yellowlist)
	nx.draw_networkx_edges(gr, pos=pos, ax=ax, edge_color="yellow",width = 10)
	gr.remove_edges_from(yellowlist)

	gr.add_edges_from(orangelist)
	nx.draw_networkx_edges(gr, pos=pos, ax=ax, edge_color="orange",width = 10)
	gr.remove_edges_from(orangelist)

	gr.add_edges_from(redlist)
	nx.draw_networkx_edges(gr, pos=pos, ax=ax, edge_color="red",width = 10)
	gr.remove_edges_from(redlist)

	null_nodes = nx.draw_networkx_nodes(gr, pos=pos, nodelist=set(gr.nodes()), node_color="black",  ax=ax)
	null_nodes.set_edgecolor("black")

	#ax.set_title("Frame %d:    "%(num+1), fontweight="bold")


lent = sys.argv[1]
start()
ani = matplotlib.animation.FuncAnimation(fig, update, frames=lent, interval=10, repeat=True)
plt.show()
file.close()
print("done")


