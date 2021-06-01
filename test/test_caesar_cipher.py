from caesar_cipher.caesar_cipher import *

def test_cipher():
    input = ['abc','zzz']
    actual = [encrypt(i,1) for i in input]
    expected = ['bcd','aaa']
    assert actual == expected
    actual2 = [decrypt(i,1) for i in input]
    assert actual2 == input

def test_cipher2():
    actual = encrypt('abc',27)
    expected = 'bcd'
    assert actual == expected

def test_crack():
    expected = 'It was the best of times, it was the worst of times.'
    encrypted = encrypt(expected, 50)
    actual = crack(encrypted)
    assert actual == expected
