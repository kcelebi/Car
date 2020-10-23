file = open('sample.txt','w')
letters = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
file.write("if part[0] == 'A':\n	A[0].append(part[1])\n	A[1].append(part[2])\n")
for lett in letters:
	file.write("elif part[0] == '%s':\n	%s[0].append(part[1])\n	%s[1].append(part[2])\n" %(lett,lett,lett))

file.close()