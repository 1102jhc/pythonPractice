# # score_file = open("score.txt", "w", encoding="utf8")
# # print("수학 : 0", file=score_file)
# # print("영어 : 50", file=score_file)
# # score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(),end="")    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True: 
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()


#================================================================================== 연습
# score2_file = open("score2_txt", "w", encoding="utf8")
# print("asdf", file=score2_file)
# print("deed", file=score2_file)
# score2_file.close()


# score2_file = open("score2_txt", "a", encoding="utf8")
# score2_file.write("\n나나sn33")
# score2_file.write("\n33298나나sn")
# score2_file.close()

# score2_file = open("score2_txt", "r", encoding="utf8")
# print(score2_file.read())
# score2_file.close()

# score2_file = open("score2_txt", "r", encoding="utf8")
# while True:
#     line = score2_file.readline()
#     if not line:
#         break
#     print(line)
# score2_file.close()


score2_file = open("score2_txt", "r", encoding="utf8")
lines = score2_file.readlines()
for line in lines:
    print(line, end="")
score2_file.close()
