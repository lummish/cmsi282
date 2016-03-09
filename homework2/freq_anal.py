import operator

def letter_anal(text):
	txt = text.split(" ")
	freq_dict = {}
	for word in txt:
		for letter in word:
			if letter in freq_dict:
				freq_dict[letter] += 1
			else:
				freq_dict[letter] = 1
	return(sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True))

def bigram_anal(text):
	txt = text.split(" ")
	freq_dict = {}
	for word in txt:
		if len(word) == 1:
			continue
		for ind in range(len(word) - 1):
			if word[ind:ind+2] in freq_dict:
				freq_dict[word[ind:ind+2]] += 1
			else:
				freq_dict[word[ind:ind+2]] = 1
	return(sorted(freq_dict.items(), key=operator.itemgetter(1), reverse=True))

print(letter_anal("""RYW QVKOVWPP KT KLV FVBP, LQKU DYZIY FEE WEPW IYZWTEG HWQWUHP, ZP FP
	DWEE AUKDU RK RYW QLXEZI FP RK BGPWET, FUH ZR ZP, Z RVLPR, VWFPKUFXEG
	PFRZPTFIRKVG FUH WUIKLVFOZUO RK FEE. DZRY YZOY YKQW TKV RYW TLRLVW,
	UK QVWHZIRZKU ZU VWOFVH RK ZR ZP JWURLVWH."""))
print(bigram_anal("""RYW QVKOVWPP KT KLV FVBP, LQKU DYZIY FEE WEPW IYZWTEG HWQWUHP, ZP FP
	DWEE AUKDU RK RYW QLXEZI FP RK BGPWET, FUH ZR ZP, Z RVLPR, VWFPKUFXEG
	PFRZPTFIRKVG FUH WUIKLVFOZUO RK FEE. DZRY YZOY YKQW TKV RYW TLRLVW,
	UK QVWHZIRZKU ZU VWOFVH RK ZR ZP JWURLVWH.\n\n"""))

print("""RYW QVKOVWPP KT KLV FVBP, LQKU DYZIY FEE WEPW IYZWTEG HWQWUHP, ZP FP
DWEE AUKDU RK RYW QLXEZI FP RK BGPWET, FUH ZR ZP, Z RVLPR, VWFPKUFXEG
PFRZPTFIRKVG FUH WUIKLVFOZUO RK FEE. DZRY YZOY YKQW TKV RYW TLRLVW,
UK QVWHZIRZKU ZU VWOFVH RK ZR ZP JWURLVWH.""".replace("[^KRWYZ]*", "-"))