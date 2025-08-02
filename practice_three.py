#
test_dict={}
for i in range(5):
    key_R=input("Enter Person Name ")
    value_S=int(input("Enter Person Age "))
    test_dict[key_R]=value_S
print(str(test_dict))
print("Name of Person whose age is more than 21 years ")
# for i in range(len(list(test_dict.values()))):
#     if (list(test_dict.values())[i] >=21):
#         print(list(test_dict.keys())[i] +"  "+ str((list(test_dict.values())[i])))
find_persons = {key: value for key, value in test_dict.items() if value > 21}
print(find_persons)