import time, datetime, pytz
variable_time = 60 * 60 * 1000
current_date_and_time = datetime.datetime.now(pytz.utc).timestamp()
print(current_date_and_time)
current_time = round(current_date_and_time * 1000)

deffered_time = current_time - variable_time

# print(datetime.datetime.timestamp(deffered_time))

search_to_date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(current_date_and_time))

search_from_date = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(deffered_time))

print(search_to_date)

print(search_from_date)

str = "Rahul"
print(str[::-1])
array_one= [1,3,7]
array_two= [2,4,5,6]

for items in array_two:
    array_one.append(items)

print(array_one)
print(array_one)

str = '^[a-z][A-Z][0-9]\@([gmail|rediffmail])\.[a-z]'

