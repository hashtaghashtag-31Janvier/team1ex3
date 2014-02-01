
def relationDInfluence(nbRelation, tabRelation):
    if nbRelation != len(tabRelation):
		print('Input incorrecte')
    else:
        plusLongueRelation = [None] * nbRelation
        for x in range(0, nbRelation):
            pivot = tabRelation[x].partition('_')[2]
            y = x+1
            for n in range(0, nbRelation-1):
                pivot = tabRelation[x][0]
            	if tabRelation[n][0] == pivot:
                   plusLongueRelation[x] = pivot
                   pivot = tabRelation[y].partition(' ')[2]
    	plusLongueRelation.sort()
    	print plusLongueRelation




nbRelation = 5
tabRelation ="1_2", "2_3", "3_4", "2_5", "5_6"
relationDInfluence(nbRelation, tabRelation)

def recursiveFunc(a, b, taille, nbMax, tab):
	if n > 0:
		return nbMax
