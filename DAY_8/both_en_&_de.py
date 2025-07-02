alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("encode or decode:")
text = input("enter test:")
shift = int(input("enter number of shift:"))


def cypher(original_text, shift_amount, encode_or_decode):
    cyper = ""
    if encode_or_decode ==  "decode":
            shift_amount *= -1 
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet) 
        cyper += alphabet[shifted_position]
    print("the encrpyted word is", cyper)

cypher(text, shift, direction)   