import sys

alphabet = 'zyxwvutsrqponmlkjihgfedcba'
special = '[@_!#$%^&*()<>?/\|}{~:]1234567890'
newMessage = ''

message = input('Please enter a message to decrypt: ').lower()

specialInMessage = [c for c in special if c in message]
if specialInMessage:
    print('Invalid character found in message, exiting program')
    exit()
        
key = input('Please enter a key from 1-26: ')
key = int(key)

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character

print('Your decrypted message is: ' + newMessage)
exit()
