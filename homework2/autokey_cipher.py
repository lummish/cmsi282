# autokey_cipher.py
def autokey_vigenere_encrypt(message, keyphrase):
	
	len_diff = len(keyphrase) - len(message)
	
	if len_diff > 0:
		key = keyphrase[:len(message)]
	else:
		if len(keyphrase) < -len_diff:
			key = keyphrase + message[:-len_diff]
		else:
			key = keyphrase + message[:-len_diff]
	
	
	# if message and keyphrase are strings
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
		print(cipher_charcode)
		cipher_string = chr(cipher_charcode) + cipher_string

		ciphertext_codepoints = ['\\' + hex(cipher_charcode)[1:]] + ciphertext_codepoints
		#ciphertext_codepoints = [hex(cipher_charcode)] + ciphertext_codepoints
	return cipher_string
	
	

def autokey_vigenere_decrypt(ciphertext, key):
	return 0
	

print(autokey_vigenere_encrypt("hello", "afg"))
	
