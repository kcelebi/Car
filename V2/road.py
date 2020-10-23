#Consider network of roads
#Cars flow across roads


nodes = {
	1: ['e0102','e0201','e0103'],
	2: ['e0102','e0201','e0204','e0402'],
	3: ['e0103','e0304'],
	4: ['e0304','e0204','e0402']
}

#graph edges
roads = {  
	'e0102': 0,
	'e0201': 1,
	'e0103': 2,
	'e0304': 3,
	'e0204': 4,
	'e0402': 5
}

#capc for roads, all integers
capc = {
	'e0102': 3,
	'e0201': 4,
	'e0103': 2,
	'e0304': 7,
	'e0204': 3,
	'e0402': 1
}