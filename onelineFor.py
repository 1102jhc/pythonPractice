# #출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "Groot"]
# students = [len(i) for i in students]
# print(students)

# #학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "Groot"]
# students = [i.upper() for i in students]
# print(students)



students = ["기", "차", "가"]
students = [len(i)+2 for i in students]
print(students)




k = [1,2,3,4,5]
k = [i+100 for i in k]
print(k)

h = ["whooo", "are", "YOuuuuu"]
h = [i.upper() for i in h]
print(h)