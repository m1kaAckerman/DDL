def find_numbers(S, P):
    for X in range(1, 1001):
        for Y in range(1, 1001):
            if X + Y == S and X * Y == P:
                return X, Y
print()            

S = 7
P = 10
X, Y = find_numbers(S, P)
print(X, Y)