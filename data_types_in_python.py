import sys
a = 2
b = 3
z = 7.894
comp = 2+3j
# print("Data Types in Integer:", dir(a))
c = a.__add__(b)
print("Add function:",c)
print("A to the power B",pow(a,b))
print("Divmod",divmod(a,b))
print("Integer value of Z:", z.__int__())
print("Floating point truncated number of Z:", z.__trunc__())
print("Nearest Integer Value:", z.__ceil__())
print("Absolute value of a complex number:", comp.__abs__())

import asyncio

class AsyncioCounter:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.count = 0
    
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.count < self.limit:
            self.count += 1
            await asyncio.sleep(1)
            return self.count
        else:
            raise StopAsyncIteration
    
async def main():
    async for number in AsyncioCounter(5):
        print(f"Async iteration number:{number}")
asyncio.run(main())

s = [(1,2),(3,4),(5,6)]
# s = 121
try:
    if all(i for i in s):
        # breakpoint()
        print(f"Iterable is True")
    else:
        print(f"Iterable is False")
except Exception as e:
    print(f"Issue Found:{e}")

st = {
    "India": "Wridhimman",
    "Australia": "Gilchrist",
    "South Africa": "",
    "Sri Lanka": "Sangakara"
}
rt = [1,2,3,4,5]
try:
    if any(n%2 ==0 for n in rt):
        print(f"Iterable is True")
    else:
        print(f"Iterable is False")
except Exception as e:
    print(f"Issue Found:{e}")
name = "Sanju"
print(f"Ascii value of st is {ascii(st)}")
print("Binary value of 14 is {}".format(bin(14)))
new_name = bytearray(b"Sanju")
new_name[0] = ord("R")
print(f"Changed new name is:{new_name}")
b = bytes([65,66,67])
print(f"Bytes are:{b}")
name = bytes(name, encoding='utf-8')
print(f"After converting to bytes name:{name}")
def my_test():
    print(f"I am callable")
print(f"Callable function: {callable(my_test)}")
print(f"Global Variables: {globals()}")
list_one = [1,2,3,4,5,6]
evens = filter(lambda x: x%2==0, list_one)
print(f"Even numbers are: {list(evens)}")
# compiled = compile(code, '<string>','exec')
# exec(compiled)
class Person:
    def __init__(self, name):
        super().__setattr__('name', name)
    
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)
    

p = Person("Joy")
p.age = 30
print(f"Name is: {p.name}")
delattr(p, "name")
print(f"Age is: {p.age}")
fs = frozenset([12,13,44,55,85])
print(f"Frozenset is: {fs}")
var = hash("hello")
print(f"Hash Value of List One is: {var}")
new_list = [10,15,20,25,30]
itr = iter(new_list)
print(next(itr))