# 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    dict = {}
    lists = []
    system = ''
    userId = ''
    name = ''
    for i in range(len(record)):
        imsi = record[i].split()
        if imsi[0] == 'Enter':
            dict[imsi[1]] = imsi[2]
            lists.append(['enter', imsi[1]])
        elif imsi[0] == 'Leave':
            imsiimsi = []
            lists.append(['leave', imsi[1]])
        elif imsi[0] == 'Change':
            dict[imsi[1]] = imsi[2]
            
    for i in range(len(lists)):
        what = ''
        if lists[i][0] == 'enter':
            what = '들어왔습니다.'
        elif lists[i][0] == 'leave':
            what = '나갔습니다.'
        
        who = dict[lists[i][1]]
        answer.append(who + "님이 " + what)
        
    return answer
