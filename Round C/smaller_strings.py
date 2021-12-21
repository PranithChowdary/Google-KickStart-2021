# Copyright (c) 2021 PranithChowdary. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem A. Smaller Strings
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ebe5e
#
# Time:  O(N)
# Space: O(1)
#  

def smaller_strings():
    N, K = map(int, input().strip().split())
    S = input().strip()

    result = 0
    for i in range((len(S)+1)//2):
        result = (result*K+(ord(S[i])-ord('a')))%MOD
    for i in range((len(S)+1)//2, len(S)):
        if S[-1-i] != S[i]:
            result = (result+int(S[-1-i] < S[i]))%MOD
            break
    return result

MOD = 10**9+7
for case in range(input()):
    print("Case #%d: %s" % (case+1, smaller_strings()))
