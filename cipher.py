# add your code here

letters = 'abcdefghijklmnopqrstuvwxyz'
msg = input('Please enter a sentence: ')
shift = 5
encymsg = ''
#Please enter a senctence: python is fun!
#The encrypted sentence is: udymts nx kzs!
for i in msg:
    if i in letters:
        filter1 = letters.find(i)
        calc = (filter1 + shift) % 26
        filter2 = letters[calc]
        encymsg += filter2
    else:
        encymsg += i
print('The encrypted message is: ' + encymsg )




