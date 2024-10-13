alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    cipher_text = ""
    for letter in text:
            if direction == 'decode':
                shift *= -1
            shifted_position = alphabet.index(letter) + shift
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {direction}d result: {cipher_text}")

caesar(direction, text, shift)
