
import string

#create function to encrypt 
def encrypt(text,key, choice):
    #start a string
    result = ""
    #if choice is to encrypt
    if choice == 'encrypt':
    # traverse text
        for char in text:
            #check if character is a letter or a space
            if char.isalpha() == True:
            #assign each char to a var
                letter = char
                #shift 
                result += chr((ord(letter) + key - 97) % 26 + 97)
            #if empty space keep in string
            else:
                result += char
        #display 
        for i in range(len(result)):
            print('Unencrypted letter: ', text[i], '| Encrypted to letter: ', result[i])
        print(result)

    else:
        #if option is to no encrypt automically is decrypt
        decrypt(text,key)

def decrypt(text, key):
#create new string
    result = ''
#for each character in the text
    for char in text:
        #check if letter or space
        if char.isalpha() == True:
    #save alphabet to compare charcaters
            alpha = string.ascii_lowercase
            #find where the character is
            pos = alpha.find(char)
            #shift backwards
            new_pos = (pos - key) % 26
            #find where the new letter is
            new_letter = alpha[new_pos]
            #add to string
            result += new_letter
        #for empty space
        else:
            result += char
    #display
    for i in range(len(result)):
            print('Unencrypted letter: ', text[i], '| Encrypted to letter: ', result[i])
    print(result)
        
 
 
#check the above function
text = "secret"
key = 3
choice = 'encrypt'

encrypt(text,key, choice)

text = "cbe bqqmf"
key = 1
choice = 'decrypt'
encrypt(text,key, choice)

