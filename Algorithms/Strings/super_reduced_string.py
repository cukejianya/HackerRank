s = raw_input()

def string_reduced(s):
    new_str = ""
    prev = 0
    for idx, x in enumerate(s):
        if (new_str.endswith(x)):
            new_str = new_str[:-1]
            continue
        new_str = new_str + x

    return new_str if new_str else "Empty String"

print string_reduced(s)
