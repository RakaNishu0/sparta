# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
#
# count = 0
# for fruit in fruits:
#     if fruit == '배':
#         count += 1
#
# print(count)
#
# people = [{'name': 'bob', 'age': 20},
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7},
#           {'name': 'smith', 'age': 17},
#           {'name': 'ben', 'age': 27}]
#
# for person in people:
#     if person['age'] >= 20:
#         print(person['name'])
#
#
txt = 'sparta@gmail.com'

# result = txt.replace('gmail','naver')
# print(result)
#
a_dict = {'user': txt.split('@')[0], 'domain': txt.split('@')[1]}

print(a_dict['domain'].replace('gmail','naver'))
