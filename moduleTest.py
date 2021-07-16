# import my_module
# my_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# my_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# my_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때 가격

#======================

# import my_module as mm
# mm.price(3)
# mm.price_morning(4)
# mm.price_soldier(5)

#======================

# from my_module import *
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

#======================

# from my_module import price, price_morning
# price(5)
# price_morning(6)

#======================

from my_module import price_soldier as price
price(5) # price_soldier 의 값

