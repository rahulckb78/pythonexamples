def adder(value):
    def inner_function(base):
        return base + value
    return inner_function

add_5 = adder(5)
result = add_5(10)
print(result)

add = lambda x: lambda y: x+y
new_add = add(6)

print("New Adder: ",new_add(10))