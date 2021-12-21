# Copyright (c) 2021 PranithChowdary. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem C. Rock Paper Scissors
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e
#
# Time:  O(N^3)
# Space: O(N^3)
#

def backtracing(dp):
    result = []
    r = s = p = 0
    while r+s+p < N:
        result.append(dp[r][s][p][1])
        if result[-1] == 'R':
            r += 1
        elif result[-1] == 'S':
            s += 1
        else:
            p += 1
    return "".join(result)

def solve(W, E):
    dp = [[[[0.0, ''] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    for r in reversed(range(N+1)):
        for s in reversed(range(N+1-r)):
            for p in reversed(range(N+1-r-s-1)):
                dp[r][s][p] = max(dp[r][s][p], [dp[r+1][s][p][0] + ((W*p+E*s)/(r+s+p) if r+s+p != 0 else (W+E)/3), 'R'])
                dp[r][s][p] = max(dp[r][s][p], [dp[r][s+1][p][0] + ((W*r+E*p)/(r+s+p) if r+s+p != 0 else (W+E)/3), 'S'])
                dp[r][s][p] = max(dp[r][s][p], [dp[r][s][p+1][0] + ((W*s+E*r)/(r+s+p) if r+s+p != 0 else (W+E)/3), 'P'])
    return backtracing(dp)

def rock_paper_scissors():
    W, E = map(float, input().strip().split())
    return solve(W, E)

N = 60
T, X = input(), input()
for case in range(T):
    print("Case #%d: %s" % (case+1, rock_paper_scissors()))
