url = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

# 쿼리 문자열 분리
query_string = url.split('?')[1]

# 쿼리 파라미터를 딕셔너리로 변환
params = {}
for param in query_string.split('&'):
    key, value = param.split('=')
    params[key] = value

# 결과 출력
print(params)