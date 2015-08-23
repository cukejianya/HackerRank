N = input()
S = input()
K = input()

def changeChar(char, increase):
    increase %= 26
    code = ord(char)
    if code >= 97 and code <= 122:
        code+=increase
        if code > 122:
            code -= 122
            code += 96

    if code >= 65 and code <= 90:
        code+=increase
        if code > 90:
            code -= 90
            code += 64

    return chr(code)

response = ''.join([changeChar(str(char), K) for char in S])
print response
