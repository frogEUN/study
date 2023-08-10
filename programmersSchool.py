# Lv1. 제일 작은 수 제거하기
def solution(arr):
    answer = arr
    small = arr[0]
    small_idx = 0
    for i in range(len(arr)):
        if arr[i] <= small:
            small = arr[i]
            small_idx = i
    del answer[small_idx]
    if len(answer) == 0:
        answer = [-1]
    return answer


'''
def solution(players, callings):
    answer = players
    for call in callings:
        idx = players.index(call)
        answer[idx], answer[idx-1] = answer[idx-1], answer[idx]
    return answer
''' # 시간초과
'''
def solution(players, callings):
    player_lank = {player: lank for player in players for lank in range(1, len(players)+1)}
    lank_player = {lank: player for player in players for lank in range(1, len(players)+1)}
    for call in callings:
        pre_lank = player_lank[call]
        player_lank[call], player_lank[lank_player[pre_lank-1]] = player_lank[lank_player[pre_lank-1]], player_lank[call]
        lank_player[pre_lank], lank_player[pre_lank-1] = lank_player[pre_lank-1], lank_player[pre_lank]
    return [lank_player[i] for i in range(1, len(players)+1)]
'''  # 틀림
