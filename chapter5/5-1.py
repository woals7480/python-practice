class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)

print(a.add())


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(1, 3)
print(b.mul())
print(b.pow())


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
        
c = SafeFourCal(4, 0)
print(c.div())