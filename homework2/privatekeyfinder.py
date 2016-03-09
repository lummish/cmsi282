# privatekeyfinder.py

# modified from stackoverflow user agf to remove factors 1, n
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))

# from stackoverflow user Mart Bakhoff
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def generate_private_key((N, e)):
	factor_list = list(factors(N))
	p = factor_list[0]
	q = factor_list[1]

	return modinv(e, (p-1) * (q-1))




#(729880581317, 5)

print(generate_private_key((729880581317, 5)))
