
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    # return answer
    return list(answer.keys())[0]

print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))