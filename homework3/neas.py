# neas.py
from backtracker import backtracker

def isCorrect(toTest):
	if len(toTest) > 1:
		if toTest[-1] == toTest[-2]:
			return False
		compSize = 2
		while(compSize <= len(toTest) / 2): #max substring will be half size of test array
			if toTest[-compSize:] == toTest[-compSize * 2:-compSize]:
				return False
			compSize += 1
	return True