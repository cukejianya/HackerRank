def validate_match(G, P, index_array, start_index, end_index):
    j=0
    for idx in index_array:
        for i in range(start_index, end_index):
            g = G[i]
            print '--idx...', idx
            if g[idx:idx+c] == P[j]:
                print '--P[i]...', P[j]
                print '--g[]...', g[idx:idx+c]
                j+=1;
            if j == r:
                return 'YES'
        j=0
    return 'NO'

T = int(input());
for i in range(T):
    input_list = input().split()
    R = int(input_list[0])
    C = int(input_list[1])
    G = []
    for i in range(R):
        G.append(input())
    input_list = input().split()
    r = int(input_list[0])
    c = int(input_list[1])
    P = []
    for i in range(r):
        P.append(input())

    answer = 'NO'
    for g in G:
        print '--g...', g
        if P[0] in g:
            index_array = [idx for idx, elm in enumerate(g) if g[idx:idx+c] == P[0]]
            start_index = G.index(g)
            end_index = start_index + r
            print '--index...', index_array
            answer = validate_match(G, P, index_array, start_index, end_index)
        if answer is 'YES':
            break

    print answer
