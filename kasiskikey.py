def find_vigenere_key(plaintext, ciphertext):
    key = []
    for p, c in zip(plaintext, ciphertext):
        if p.isalpha() and c.isalpha():
            shift = (ord(c.upper()) - ord(p.upper())) % 26
            key.append(chr(shift + ord('A')))
        else:
            key.append(' ')  # Preserve spaces or non-alphabet characters
    
    # Extract the repeating pattern of the key
    key_str = ''.join(key).replace(' ', '')
    for i in range(1, len(key_str)):
        if key_str[:i] == key_str[i:2*i]:
            return key_str[:i]
    
    return key_str  # Return full key if no repeating pattern is found

# Example usage
plaintext = "CRYPTOGR"
ciphertext = "UIGVTZGB"
key = find_vigenere_key(plaintext, ciphertext)
print("Recovered Key:", key)
