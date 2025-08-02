class Calculation:
    def __init__(self, num):
        self.num = list(range(num))
    def square(self):
        for val in self.num:
            if val >= 0:
                print(pow(val,2))
                
if __name__ == '__main__':
    n = int(input())
    cal = Calculation(n)
    cal.square()