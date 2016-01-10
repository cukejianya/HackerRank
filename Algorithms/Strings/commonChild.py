first_word = list(raw_input())
second_word = list(raw_input())

def check_similar_char(main, checkin):
    new = []
    for idx, char in enumerate(main):
        if char in checkin:
            new.append(char)
    return new

def substring_len(sub_first, second):
    new = []
    for char in sub_first:
        if char in second:
            new.append(char)
            idx = second.index(char)
            second = second[idx+1::]
        if not second:
            break;
    print new
    return len(new)

def common_child(first, second):
    max_child = 0
    first = check_similar_char(first, second)
    second = check_similar_char(second, first)
    for 
    print "".join(first), "".join(second)

common_child(first_word, second_word)
