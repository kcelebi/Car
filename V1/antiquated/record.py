file = open('carstats.txt','r')

lines = file.readLines()

zA,oA,zB,oB,zC,oC,zD,oD,zE,oE,zF,oF,zG,oG,zH,oH,zI,oI,zJ,oJ,zK,oK,zL,oL,zM,oM,zN,oN,zO,oO,zP,oP,zQ,oQ = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q = [zA,oA],[zB,oB],[zC,oC],[zD,oD],[zE,oE],[zF,oF],[zG,oG],[zH,oH],[zI,oI],[zJ,oJ],[zK,oK],[zL,oL],[zM,oM],[zN,oN],[zO,oO],[zP,oP],[zQ,oQ]
roads = [A,B,C,D,E,F,G,H,U,J,K,L,M,N,O,P,Q]
for line in lines:
	part = line.split(' ')
	if part[0] == 'A':
		A[0].append(part[1])
		A[1].append(part[2])
	elif part[0] == 'B':
		B[0].append(part[1])
		B[1].append(part[2])
	elif part[0] == 'C':
		C[0].append(part[1])
		C[1].append(part[2])
	elif part[0] == 'D':
		D[0].append(part[1])
		D[1].append(part[2])
	elif part[0] == 'E':
		E[0].append(part[1])
		E[1].append(part[2])
	elif part[0] == 'F':
		F[0].append(part[1])
		F[1].append(part[2])
	elif part[0] == 'G':
		G[0].append(part[1])
		G[1].append(part[2])
	elif part[0] == 'H':
		H[0].append(part[1])
		H[1].append(part[2])
	elif part[0] == 'I':
		I[0].append(part[1])
		I[1].append(part[2])
	elif part[0] == 'J':
		J[0].append(part[1])
		J[1].append(part[2])
	elif part[0] == 'K':
		K[0].append(part[1])
		K[1].append(part[2])
	elif part[0] == 'L':
		L[0].append(part[1])
		L[1].append(part[2])
	elif part[0] == 'M':
		M[0].append(part[1])
		M[1].append(part[2])
	elif part[0] == 'N':
		N[0].append(part[1])
		N[1].append(part[2])
	elif part[0] == 'O':
		O[0].append(part[1])
		O[1].append(part[2])
	elif part[0] == 'P':
		P[0].append(part[1])
		P[1].append(part[2])
	elif part[0] == 'Q':
		Q[0].append(part[1])
		Q[1].append(part[2])

for road in roads:
	
