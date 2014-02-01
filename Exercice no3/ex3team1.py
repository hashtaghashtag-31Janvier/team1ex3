
def relationDInfluence(nbRelation, tabRelation):
	if nbRelation != len(tabRelation):
		print('Input incorrecte')
	plusLongueRelation
	for x in nbRelation:
		pivot = tabRelation[x].partition(' ')[2]
		plusLongueRelation[x] = 1
		y = x+1
		while y <= n:
			if tabRelation[y].partition(' ')[2] == pivot:
				plusLongueRelation[x] = plusLongueRelation[x] + 1
				pivot = tabRelation[y].partition(' ')[2]


	nbRelMax = plusLongueRelation.sort()
	

	print(nbRelMax)


def main():
	nbRelation = 5
	tabRelation = {1 2, 1 3, 2 4, 3 4, 1 4}
	relationDInfluence(nbRelation, tabRelation)

def recursiveFunc(a, b, taille, nbMax, tab):
	if n > 0:
		return nbMax
