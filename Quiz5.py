from random import *


cnt = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("{0}손님은 {1}분이 걸리기 때문에 탑승이 가능합니다.".format(i, time))
        cnt+=1
    else:
        print("{0}손님은 {1}분이 걸리기 때문에 탑승이 불가합니다.".format(i, time))
    
    
print("총 탑승 승객 {0} 분".format(cnt))
