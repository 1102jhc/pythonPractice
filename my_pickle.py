# pickle, 프로그램상에서 사용하는 데이터를 파일 형태로 저장
# 항상 바이너리 파일 사용
# 사용하려는 모듈과 동일한 이름(pickle.py)으로 파일을 생성하면 import 시에 동일한 경로에 있는 이 파일을 먼저 인식하게 되기 때문에 오류 발생
# 

import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) 
# profile_file.close()


profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()