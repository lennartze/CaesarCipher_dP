lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def warmup(letter, no):
    if letter in lowerCase:
        no = no % 26
        result = lowerCase[lowerCase.find(letter) + no]
        return result
    else:
        return 'Error: Bitte geben sie einen Kleinbuchstaben an.'

def findNextNo(no, letterIndex):
    if letterIndex + no > 25:
        no = (letterIndex + no) % 26
    else:
        no = no + letterIndex
    return no

def shiftLetter(letter, no):
    if letter in lowerCase:
        shiftedLetter = lowerCase[findNextNo(no, lowerCase.find(letter))]
    elif letter in upperCase:
        shiftedLetter = upperCase[findNextNo(no, upperCase.find(letter))]
    elif letter == ' ':
        shiftedLetter = ' '
    else:
        return 'Error: Bitte geben Sie entweder Groß- oder Kleinbcuhstaben an!'
    return shiftedLetter

def caeser(text, no):
    no = no % 26
    result = ''
    for letter in text:
       result = result + shiftLetter(letter, no)
    return result

print(caeser('Test mit Leerzeichen', 1))
print(caeser('Uftu nju Mffsafjdifo', 25))
print(caeser('dailyprogrammer', 6))