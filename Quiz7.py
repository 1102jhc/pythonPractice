
# for i in range(1,51):
#     report = open("{0}주차.txt".format(i),"w",encoding="utf8")
#     report.write("부서 :")
#     report.write("\n이름 :")
#     report.write("\n업무 요약 :")
#     report.close()

    #-----------------------------------

for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report:
        report.write("- {0} 주차 주간보고 -".format(i))
        report.write("\n부서 : ")
        report.write("\n이름 : ")
        report.write("\n업무 요약 : ")
