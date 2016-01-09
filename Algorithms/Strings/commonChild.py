first_word = list(raw_input())
second_word = list(raw_input())

def check_similar_char(main, checkin):
    new = []
    for idx, char in enumerate(main):
        if char in checkin:
            new.append(char)
    return new

def common_child(first, second):
    max_child = 0
    first = check_similar_char(first, second)
    second = check_similar_char(second, first)
    print "".join(first), "".join(second)

common_child(first_word, second_word)
