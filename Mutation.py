S = raw_input()
T = tuple(raw_input().split(' '))
S = S[:int(T[0])] + T[1] + S[int(T[0]) + 1:]
print S
