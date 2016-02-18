1.

	a) f = Θ(g)
	b) f = O(g)
	c) f = O(g)
	d) f = Θ(g)
	e) f = Θ(g)
	f) f = Θ(g)
	g) f = Ω(g)
	h) f = Ω(g) 
	i) f = Ω(g)
	j) f = Ω(g)
	k) f = Ω(g)
	l) f = O(g)
	m) f = O(g)
	n) f = Θ(g) 
	o) f = Ω(g)
	p) f = O(g)
	q) f = Θ(g)

2.

		print(pow(5, 30000, 31))
		print(pow(6, 123456, 31))
		# output 1, 1

	Take difference of mods, get 0. Yes, the difference is divisible by 31

 
3.

	Proposition: b = floor(log_2(n+1))

	Base Case n = 1: b = log_2(1+1)
				 2^b = 2
				 b = 1
	
	True. 1 can be represented using only one binary digit: 1

	Assume the truth of our inductive hypothesis: 
	
	b = floor(log_2(k+1)) for some integer k > 1 or 
	2^b <= k+1

Test truth for k+1: 
		
	2^b + 1 <= k + 1 + 1

	log_2(2^b + 1) <= log_2(k + 2)
	log_2(2^b) + log_2(1 + 1/2^b) <= log_2(k+2)

The second term on the left side of this equation is clearly less than 1 but greater than 0, which means that it will not be included in the integer part of the result:

	log_2(2^b) <= log_2((k+1) + 1)

Therefore by our inductive hypothesis, the proposition must be true.
					

4.
The sum of all powers of 2 up to a power n can be expressed:
	
	2^n+1 - 1
	eg: 2^0 + 2^1 + 2^2 + 2^3 = 15 = 2^4 - 1
	 
So if the number of grains of rice on the board can be expressed as the sum of all 2^n from n = 0 to n = 63 is equivalent to (2^64) - 1

b) 
This can be seen as a sum that can be calculated like so:

	def summit():
		sum = 0
		for i in range(64):
			sum += 2 * i + 1
		return sum
		
	print(summit()) #4096
5. See poly.py
6. See three_partition.py
7. For method, see c.py 
		
	No memoization: 335919
	Memoization: 397
