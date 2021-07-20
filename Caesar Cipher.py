from turtle import position


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('What do you do want your key to be: '))
new_message = ''


message = input('Please enter a message: ')

position = alphabet.find(character)

new_position = (position + key) % 26

new_character = alphabet[new_position]
print(new_character)