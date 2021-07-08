# print("Python", "Java", "JavaScript", sep=" vs ")
# print("Python", "Java", "JavaScript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("python","java", file=sys.stdout)     # 표준 출력
# print("python","java", file=sys.stderr)     # 표준 에러

# scores = {"수학":0, "영어":50, "코딩": 100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #  8칸 확보 후 왼쪽 정렬, 4칸 확보후 오른쪽 정렬

# 은행 대기순번표 
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))    # 3크기 확보, 빈공간 0으로 채움

# 사용자 입력을 받으면 항상 문자열로 입력받는다.
answer = input ("아무 값이나 입력하세요 : ")
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")