import re
import string
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

alephbet = string.ascii_uppercase 

def encrypt(plain, key): 
    encrypted_text = ""
    plain_len = len(plain)
    for i in range(plain_len):
        char = plain[i] 
        if  not(char.islower() or  char.isupper()):
            encrypted_text += char
            continue
        if char.islower():
            location = alephbet.index(char.upper()) 
            new_location = (location + key) % 26 
            encrypted_text += alephbet[new_location].lower()
        else:
            location = alephbet.index(char) 
            new_location = (location + key) % 26 
            encrypted_text += alephbet[new_location]

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key+1)


def count_words(text):

    candidate_words = text.split() # list of our words 
    word_count = 0 
    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    return word_count

def crack(encrypted):
    percentage_init = 0
    for i in range(len(encrypted.split())*26):
        candidate_dec = decrypt(encrypted, i)
        word_count = count_words(candidate_dec)
        percentage = int(word_count / len(candidate_dec.split()) * 100)
        if percentage > percentage_init:
            percentage_init = percentage 
            decrypt_word = candidate_dec
    return decrypt_word


if __name__ == "__main__":

    input = ['abc','zzz']
    actual = [encrypt(i,1) for i in input]
    expected = ['bcd','aaa']
    print(expected,actual)
    actual2 = [decrypt(i,1) for i in input]
    print(actual2)

    word = 'It was the best of times, it was the worst of times.'
    encrypted = encrypt(word, 50)
    print('en',encrypt(word, 50))

    print("the right decrypt is ", crack(encrypted))
    