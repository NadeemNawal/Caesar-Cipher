alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt")
text=input("Type your message").lower()
shift= int(input("Type the shift number"))
def caesar(start_text, shift_amount, cipher_direction):
  end_text=""
  if cipher_direction =="decode":
    shift_amount*= -1
  for character in start_text:
    if character in alphabet:
      position=alphabet.index(character)
      new_position=position +shift_amount
      end_text+= alphabet[new_position]
    else:
      end_text+=character
  print(f"The {cipher_direction}d text is {end_text}")
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
should_continue=True
while should_continue:
  direction=input("Type 'encode' to encrypt, type 'decode' to decrypt ")
  text=input("Type your message ").lower()
  shift= int(input("Type the shift number "))
  shift=shift%26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if restart== "no":
    should_continue=False
    print("Goodbye")
