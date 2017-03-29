s = raw_input()

def camel_case(s):
    count = 1
    for x in s:
        if (x.isupper()):
            count = count + 1

    return count

print camel_case(s)
