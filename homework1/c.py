#c.py
memo = {}
count = {0: 0, 1:0}

def c(n, k): # memoized
	count[0] += 1
	if k == 0:
		return 1
	elif k == n:
		return 1
	elif (n,k) in memo:
		return memo[(n,k)]
	else:
		memo[(n-1, k)] = c(n-1, k)
		memo[(n-1, k-1)] = c(n-1, k-1)
		return c(n-1, k) + c(n-1, k-1)

def bad_c(n, k): # non-memoized
	count[1] += 1
	if k==0:
		return 1
	elif k ==n:
		return 1
	else:
		return bad_c(n-1, k) + bad_c(n-1, k-1)

	
print(c(20,11))
print(bad_c(20,11))
print("Memoized Calls: {}".format(count[0]))
print("Non-memoized Calls: {}".format(count[1]))