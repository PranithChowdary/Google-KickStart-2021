# Copyright (c) 2021 PranithChowdary. All rights reserved.
#
# Google Kick Start 2021 Round C - Problem C. Rock Paper Scissors
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435c44/00000000007ec28e
#
# Time:  O(N)
# Space: O(1)
#

def rock_paper_scissors():
    W, E = map(int,input().strip().split())

    if W == E:
        return RESULT[0]
    if W == E*2:
        return RESULT[1]
    if W == E*10:
        return RESULT[2]
    return RESULT[3]

RESULT = ['SRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRPSRP', 'SPPRRRRSSSSSSSSPPPPPPPPPPPPPPPPRRRRRRRRRRRRRRRRRRRSSSSSSSSSS', 'SPPPPRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSPPPPPPPPPPPPPPP', 'SPPPPPPPPPRRRRRRRRRRRRRRRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSS']
T, X = input(), input()
for case in range(T):
    print("Case #%d: %s" % (case+1, rock_paper_scissors()))