def subsetsum(sumset, gsum):
	for s in sumset:
		if s > gsum:
			sumset.remove(s) # elements larger than goal not part of solution
	if 0 not in sumset:
		sumset.insert(0,0) # need 0 element

	dp_grid = [[False for i in range(gsum + 1)] for j in range(len(sumset))]
	dp_grid[0][0] = True

	print(sumset)
	for i in range(1, len(sumset)):
		dp_grid[i][sumset[i]] = True

	for i in range(1, len(sumset)):
		for j in range(gsum + 1):
			if j - sumset[i] < 0:
				dp_grid[i][j] = dp_grid[i - 1][j]
			else:
				dp_grid[i][j] = dp_grid[i - 1][j] or dp_grid[i - 1][j - sumset[i]]

	return dp_grid[len(sumset) - 1][gsum]




print(subsetsum([1,3,7,5,4,2], 16))
