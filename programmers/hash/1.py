import collections


def solution(participant, completion):
    fail_participant = collections.defaultdict(int)

    for p in participant:
        fail_participant[p] += 1

    for c in completion:
        fail_participant[c] -= 1
    for k, v in fail_participant.items():
        if v != 0:
            return k
