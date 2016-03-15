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


	
key = autokey_vigenere_gen_key("hello what is good", "How goes it my d00d?")
ct = autokey_vigenere_encrypt("hello what is good", key)
print(autokey_vigenere_decrypt(ct, key))
	
