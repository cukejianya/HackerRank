def removeAllDoubles(string):
    letters = set(string)
    isDoubles = true
    while(isDoubles):
        isDoubles, string, letters = findAndRemoveDouble(string, letters)

def findAndRemoveDouble(string, letters):
    for x in letters:
        if x*2 in string:
            string.replace(x,'')
            letters.remove(x)
            return (true, string, letters)
    return (false, string, letters)

def sortByAmount(string):
    letters = set(string)
    match = {x: string.count(x) for x in string}
    compare = lambda x,y: cmp(match[x],
    return sorted(set(string), cmp=compare)
