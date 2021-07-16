# 다중상속 시 super()를 사용하면 첫 번째 상속받은 것만 초기화 시켜주므로
# 상속받은 모든 생성자를 초기화시켜주기 위해서는 super()를 쓰지 않고 명시적으로 나타내야 한다.

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()