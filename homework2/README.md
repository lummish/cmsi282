#1.

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
| Size | Time (s)|
|------|------|
| 1 | 5.26905059814e-06 |
| 2 | 1.13248825073e-05 |
| 3 | 2.44140625e-05 |
| 4 | 0.000106883049011 |
| 5 | 0.00056631565094 |
| 6 | 0.00689549446106 |
| 7 | 0.0229957580566 |
| 8 | 0.128792262077 |
| 9 | 0.792087674141 |
| 10 | 8.95592021942 |
 
#2. 
    # autokey_cipher.py

        def autokey_vigenere_gen_key(message, keyphrase):
	        len_diff = len(keyphrase) - len(message)
	
	        if len_diff > 0:
		        key = keyphrase[:len(message)]
	        else:
		        if len(keyphrase) < -len_diff:
			        key = keyphrase + message[:-len_diff]
		        else:
			        key = keyphrase + message[:-len_diff]
	        return key

        def autokey_vigenere_encrypt(message, key):	
	        message_codepoints = [ord(c) for c in message]
	        key_codepoints = [ord(c) for c in key]
	        ciphertext_codepoints = []
	        carry = 0
	        cipher_string = ''

	        for i in range(len(message_codepoints) - 1, -1, -1):
		        cipher_charcode = message_codepoints[i] + key_codepoints[i] + carry
		        if cipher_charcode > 255:
			        carry = 1
			        cipher_charcode -= 256
		        ciphertext_codepoints = [hex(cipher_charcode)] + ciphertext_codepoints

	        return ciphertext_codepoints
	    
        def autokey_vigenere_decrypt(ciphertext, key):
            ciphertext_codepoints = [int(c, 16) for c in ciphertext]
            key_codepoints = [ord(c) for c in key]
        
	        return "".join([chr(c_i - k_i) for c_i, k_i in zip(ciphertext_codepoints, key_codepoints)])

#3.
    RYW QVKOVWPP KT KLV FVBP, LQKU DYZIY FEE WEPW IYZWTEG HWQWUHP, ZP FP
    THE PROGRESS OF OUR ARMS, UPON WHICH ALL ELSE CHIEFLY DEPENDS, IS AS
    
    DWEE AUKDU RK RYW QLXEZI FP RK BGPWET, FUH ZR ZP, Z RVLPR, VWFPKUFXEG
    WELL KNOWN TO THE PUBLIC AS TO MYSELF, AND IT IS, I TRUST, REASONABLY
    
    PFRZPTFIRKVG FUH WUIKLVFOZUO RK FEE. DZRY YZOY YKQW TKV RYW TLRLVW,
    SATISFACTORY AND ENCOURAGING TO ALL. WITH HIGH HOPE FOR THE FUTURE, 
    
    UK QVWHZIRZKU ZU VWOFVH RK ZR ZP JWURLVWH.
    NO PREDICTION IN REGARD TO IT IS VENTURED.
    
    See that Z is on its own, know that it must correspond ot A or I
    W is most frequent character, so most likely E
    Try R = T, Y = H
    See RK, K must be O
    Try Z = I
    See ZR followed by ZP, so IT followed by I_ probably P is S 
    F probably to frequent to be U, but followed by an S in a two letter word. Probably A
    See SATIS-A-TO--, assume SATISFACTORY, fill in blanks
    See REASO-A--Y, assume REASONABLY, fill in blanks
    See HO-E, HOPE fill in blanks
    See P-BLIC, fill in blanks
    See -HICH, fill in blanks
    HI-H HOPE, fill in blanks
    WELL -NOWN, fill in blanks
    -YSELF, fill in blanks
    -EPEN-S, fill in blanks
#4. 
    
    # Darn, not another cryptanalysis question
    
    # D A R N O
    # U B F G T
    # Q X Z K H
    # I W V M E
    # S L P Y C
    
    # D A R N O
    # T H E C Y
    # P L S I Q 
    # U B F G K
    # M V W X Z
    
    # D A R N O T H E C Y P L S I Q U B F G K M V W X Z
    
    bifid_array = 'D A R N O T H E C Y P L S I Q U B F G K M V W X Z'.split(" ")
    bifid_mat = {}
    decrypt_mat = {}
    
    k = 0
    for i in range(5):
    	for j in range(5):
    		bifid_mat[bifid_array[k]] = (i, j)
    		decrypt_mat[(i,j)] = bifid_array[k]
    		k += 1
    
    bif_string = ""
    
    for c in "TWBTLLAEPODTUBTWBTLTDLDDVSNNHEETLSKDDSIFGIIMWLYDKDDSPHBPQKOFHMDLSKRS":
    	bif_string += `bifid_mat[c][0]` + `bifid_mat[c][1]`
    
    
    row = bif_string[0:len(bif_string)/2]
    col = bif_string[len(bif_string)/2:]
    
    result = ""
    for i in range(len(bif_string) / 2):
    	result += decrypt_mat[(int(row[i]), int(col[i]))]
    
    print(result)
    
    #COMPUTERSCIENCEISNOMOREABOUTCOMPUTERSTHANASTRONOMYISABOUTTELESCOPESS
#5.
    p=23847623789462398745236743254827634647
    
    q=80147623789462398745236743254827634711
    
    N = pq = 1911330379750465988511865475607817924950038631764482538080744390093883432017
    
    (p-1)(q-1) = 1911330379750465988511865475607817924846043384185557740590270903584228162660
    
    pick e relatively prime to (p-1)(q-1): 
    e = 7
    
    public key: (1911330379750465988511865475607817924950038631764482538080744390093883432017, 7)
    
    d = invmod(e, (p-1)(q-1)) = invmod(7, (23847623789462398745236743254827634646)(80147623789462398745236743254827634710))
      = invmod(7, 1911330379750465988511865475607817924846043384185557740590270903584228162660)
      = 546094394214418853860532993030805121384583824053016497311505972452636617903
    
    private key: (1911330379750465988511865475607817924950038631764482538080744390093883432017, 546094394214418853860532993030805121384583824053016497311505972452636617903)

#6.

    public = (729880581317, 5)
    
    729880581317 = pq
    
    p = 822893, q = 886969
    
    (p - 1)(q - 1) = 822892 * 886968 = 729878871456
    
    d = invmod(5, 729878871456) 
    d = 583903097165
    
    private key: (729880581317, 583903097165)
    
#7.
    a)	The purpose of signatures is to verify the source of a message is indeed who it is purported to be.
    b)	verify((N,e), M^d, M) = [(M^d(mod N))^e mod(N)] == M
    	
    	We know that given some public key (N, e) and a plaintext message m, we can encrypt our message as
    	ciphertext: c
    
    	c = m^e (mod N)
    
    	And that to decrypt this message, we do
    
    	m = c^d (Mod N)
    
    	so if instead we start with a signed message 
    
    	σ = m^d (mod N)
    
    	we should be able to achieve
    
    	m = σ^e (mod N)
    
    	Only if the signature is valid.
    
    c)	p = 103, q = 11
    	
    	N = pq = 1133
    	
    	(p-1)(q-1) = 102 * 10 = 1020
    
    	gcd(7, 1020) = 1; pick e = 7
    
    	d = invmod(7, 1020) = 583
    
    	Mapping:
    	00 -> [space]
    	01 -> A
    	02 -> B
    	...
    	08 -> H
    	...
    	12 -> L
    	...
    	26 -> Z
    	27 -> a
    	...
    	35 -> i
    	36 -> j
    	37 -> k
    	38 -> l
    	39 -> m
    	...
    	44 -> r
    	45 -> s
    	46 -> t
    	47 -> u
    	...
    	52 -> z
    
    	Harris Lummis -> 08 27 44 44 35 45 00 12 47 39 39 35 45
    	
    	m_1 = 08
    	
    	(m_1)^d (mod N) = (8)^583 (mod 1133) = 941
    
    	941^7 (mod N) = 8
    
    d)	Assume 17 = e and 391 = N = pq (as 17 is prime, not expressable as a product of 2 primes)
    	
    	391 = (17)(23)
    	
    	(p - 1)(q - 1) = (16)(22) = 352
    
    	d = invmod(17, 352) = 145
    
    	ans: 145

#8.

a)	Given m^d (mod N) and m, by trial and error, Eve could arrive at d by attempting
	m^x (mod N) for x in the range 1...N
b) 

#9. 

    T(n) = 1 if n = 1 else T(n/2) + T(n/2) + 1 
	T(n) = 2T(n/2) + 1

	log_2(2) > 0 

	f(n) = Θ(n)
	
#10.

a)	The essential idea here is to split the problem into two subproblems each half the size of the original
		problem and check if they have a majority element. If either subproblem does have a majority element, 
		if they are the same, then that element is returned. If they are different, then each answer is checked.
		If one appears more than n/2 times in the original input, then it is output as the majority element. Otherwise,
		the input has no majority element. 
b) 

    public class MajorityElement {
    	
    	public static Integer[] major(Object[] ar, int start, int end) {
    		//System.out.println("running major..."); //used to determine time complexity
    
    		int sz = end - start;
    
    		if (sz > 1) {
    
    			int mid = start + (sz / 2);
    			Integer[] left = major(ar, start, mid);
    			Integer[] right = major(ar, mid, start + sz);
    							
    				if (left[0] == null && right[0] == null) 
    
    					return new Integer[] {null, (Integer) 0};
    				
    				else {
    
    					if (left[0] == null && right[0] != null) 
    
    						return new Integer[] {right[0], (Integer) 1};
    					
    					else if (right[0] == null && left[0] != null) 
    
    						return new Integer[] {left[0], (Integer) 1};
    
    					else {
    						
    						if (left[0] != right[0]) 
    
    							if (left[1] == right[1])
    
    								return new Integer[] {null, (Integer) 0};
    
    							else
    								
    								if (left[1] == 2)
    
    									return new Integer[] {left[0], (Integer) 1};
    								
    								else
    									
    									return new Integer[] {right[0], (Integer) 1};
    						
    						else 
    						
    							return new Integer[] {left[0], (Integer) 2};
    
    					}
    				}
    		}
    
    		else return new Integer[] {(Integer) ar[start], (Integer) 1};
    	}
    	public static void printAr(Object[] ar, int st, int end) {
    
    		for (int i = st; i < end; i++) System.out.print(ar[i] + " ");
    
    		System.out.println();
    	
    	}
    
    	public static void printOut(Object[] ar) {
    		System.out.println(ar.length);
    		System.out.print("I/P: ");
    		printAr(ar, 0, ar.length);
    		
    		Integer[] maj = major(ar, 0, ar.length);
    		String res = "";
    		
    		if (maj[1].equals((Integer) 2)) {
    			res += maj[0];
    		}
    		
    		else {
    			int count = 0;
    			
    			for (int i = 0; i < ar.length; i++) {
    				if (ar[i] == maj[0]) count++;
    			}
    			
    			if (count > ar.length/2) res += maj[0];
    			else res += "none";
    		}
    		
    		System.out.println("O/P: " + res);
    	}
    	public static void main(String[] args) {
    
    		Integer[] in = new Integer[args.length];
    
    		for (int i = 0; i < args.length; i++) {
    			in[i] = Integer.parseInt(args[i]); 
    		}
    
    		printOut(in);
    		
    	}
    }
