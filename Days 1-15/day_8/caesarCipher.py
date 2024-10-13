alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted = ''
    for letter in text:
        if letter in alphabet:
            alphabet_index = alphabet.index(letter)
            shifted_index = (alphabet_index + shift)  % len(alphabet)
            encrypted += alphabet[shifted_index]
    print(f'Your excrytion is: {encrypted}')
    return encrypted
encrypt(text, shift)
