numberWords = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
    'twenty',
]

H = int(input())
M = input()

def changeWords(number):
    if number == 30:
        return 'half '
    if number == 15:
        return 'quarter '
    mins = ' minutes ' if number > 1 else ' minute '
    if number > 20:
        ones = number%10
        return numberWords[20]+' '+numberWords[ones]+mins
    return numberWords[number]+mins

def theTimeInWords(H, M):
    if M is '0':
        return numberWords[H]+' o\' clock'
    M = int(M)
    new_M = M if M < 30 else 60-M
    return_statement = changeWords(new_M)
    if M > 30:
        return_statement += 'to '+numberWords[H+1]
    else:
        return_statement += 'past '+numberWords[H]
    return return_statement

print theTimeInWords(H, M)
