# 8장 - 딕셔너리와 셋

print("[딕셔너리!]")
heroes = dict(kiriko="support", genji="dps", winston="tank")
# [key]와 get()의 차이
# 딕셔너리에 해당 키가 없으면
# [key]는 예외 발생
# get()은 none, 또는 두번째 파라미터로 넣은 값을 반환
print("heroes  :  ", heroes)
print(".keys()  :  ", heroes.keys())
print(".values()  :  ", heroes.values())
print(".items()  :  ", heroes.items())
# 결합하기 :  {**dict1, **dict2}    or     dict1.update(dict2)
# del dict1[key1] -> 삭제
# dict1.pop(key1) -> 해당 값 반환하고 삭제
# 모든 항목 삭제하기 : .clear()
# 딕셔너리 컴프리헨션 {키 표현식 : 값 표현식 for 표현식 in 순회 가능한 객체}
