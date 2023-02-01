from numpy import loadtxt
import random
import sys

sys.setrecursionlimit(1500)

# retrieving wordle data
lines = loadtxt("wordle.txt", comments="#", delimiter=",", dtype='str', unpack=False)
array = []
for i in range(len(lines)):
    array.append(lines[i][0])


# Concatenate text
def concatenate(a, b, c, d, e):
    word = a + b + c + d + e
    return word


# Check if word is in database with binary search
def check(data, word, start, end):
    if start == end:
        return False
    mid = (start + end) / 2
    if data[int(mid)] == word:
        return True
    if data[int(mid)] > word:
        return check(data, word, start, mid)
    return check(data, word, mid + 1, end)


# Generate random word
def randomWord(data):
    return data[random.randrange(0, len(data))]


def checkWin(score):
    for i in range(0, 5):
        if score[i] != 2:
            return False
    return True


def round(guess, word):
    score = [0,0,0,0,0]
    tempGuess = []
    tempWord = []
    tempWord2 = []

    for i in range(0, 5):
        tempGuess.append(guess[i])
        tempWord.append(word[i])
        tempWord2.append(word[i])

    for i in range(0, 5):
        if word[i] == tempGuess[i]:
            score[i] = 2
            tempGuess[i] = str(i)
            tempWord[i] = str(i)
        else:
            score[i] = 0

    letterCount = [1, 1, 1, 1, 1]

    x = 3
    for j in range(0, 4):
        for i in range(j + 1, 5):
            if tempWord2[j] == tempWord2[i]:
                letterCount[j] = letterCount[j] + 1
                letterCount[i] = letterCount[i] -1
                tempWord2[i] = str(x)
                x = x + 1

    for i in range(0,5):

        for j in range(0,5):
            if tempGuess[i] == tempWord2[j] and letterCount[j] > 0:
                score[i] = 1
                letterCount[j] = letterCount[j] - 1

    print(score)
    return score


word = randomWord(array)
"""
for i in range (0,6):
    a = input("Enter letter 1")
    b = input("Enter letter 2")
    c = input("Enter letter 3")
    d = input("Enter letter 4")
    e = input("Enter letter 5")

    guess = concatenate(a, b, c, d, e)

    if not check(array,guess,0,len(array)):
        print("YOU LOST!!")
        break

    arr = round(guess,word)
    if checkWin(arr):
        print("YOU WON!!")
        print(word)
        break

"""



