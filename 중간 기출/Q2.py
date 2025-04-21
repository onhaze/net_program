lst = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']

# A. 리스트 마지막에 '!' 추가 후 출력
lst.append('!')
print(lst)

# B. 다섯 번째 요소('o') 제거 후 출력
lst.pop(4)
print(lst)

# C. 인덱스 4에 'a' 삽입 후 출력
lst.insert(4, 'a')
print(lst)

# D. 리스트를 문자열로 변환하여 출력
print(''.join(lst))

# E. 리스트를 오름차순으로 정렬하여 출력
print(sorted(lst))