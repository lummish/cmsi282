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