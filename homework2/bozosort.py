from random import randint
from random import sample
import time

def bozosort(lst):
	while any(lst[i] > lst[i+1] for i in range(len(lst) - 1)):
		index_1 = randint(0, len(lst) - 1)
		index_2 = randint(0, len(lst) - 1)

		if index_1 != index_2:
			swap = lst[index_1]
			lst[index_1] = lst[index_2]
			lst[index_2] = swap
	
	return lst

for i in range(1, 11):
	sum_time = 0 # will be used to calculate avg time

	for j in range(10): # Generates average time for array of size 
		start = time.time()
		bozosort(sample(range(1,100), i))
		end = time.time()
		sum_time += end - start

	print("Array of size {}: {}".format(i, sum_time / 10))

'''
Array of size 1: 5.26905059814e-06
Array of size 2: 1.13248825073e-05
Array of size 3: 2.44140625e-05
Array of size 4: 0.000106883049011
Array of size 5: 0.00056631565094
Array of size 6: 0.00689549446106
Array of size 7: 0.0229957580566
Array of size 8: 0.128792262077
Array of size 9: 0.792087674141
Array of size 10: 8.95592021942
'''