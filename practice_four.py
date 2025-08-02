dict_one = {
    "A": 1,
    "B": 2

}
dict_two = {
    "C": 3,
    "D": 4
}

new_dict = {**dict_one, **dict_two}
dict_one.update(dict_two)
print(new_dict)
print(*range(1,10))

MyClass = type('MyClass', (object,), {'greet': lambda self: 'Hello, world!','add': lambda self,a,b: a+b})
# Create an instance of MyClass
instance = MyClass()

# Call the greet method
print(instance.greet())  # Output: Hello, world!
print(instance.add(4,5))
