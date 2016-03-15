#recursion.py

def f(n):
	if n > 1:
		print('still going')
		f(n/2)
		f(n/2)

f(64)