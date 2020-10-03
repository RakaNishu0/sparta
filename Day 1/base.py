# 변수
first_name = 'mh'
last_name = 'yoo'

a = '2'
b = 3

print(a+last_name)

# 변수의 이름은 의미를 가지도록 해주는 것이 좋다
# 회사마다 일종의 협의된 네이밍을 따르면 됨

# 자료형

a_list = ['사과', '밤', '배']
b_list = ['스카', '요닝', ['에밀', '앙닥' ]]


print(a_list[1])
print(b_list[2][0])

# 딕셔너리 형

a_dict = {'name': 'mhyoo', 'age': '37'}
# 딕셔너리는 Key: Value 의 구성 / 순서는 중요하지 않다 / 키로 값을 찾는 방식
print(a_dict['age'])

a_dict['height'] = 160
print(a_dict)
print(a_dict['height'])

c_list = ['수박', '사과', '포도']

a_dict['fruits'] = c_list

print(a_dict)
print(a_dict['fruits'][1])