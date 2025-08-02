# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def get_captain_room_number(members_per_group, room_numbers_list=[]):
    if len(room_numbers_list) > 0:
        group_of_familes = len(room_numbers_list)//members_per_group
        count_rooms = Counter(room_numbers_list)
        unique_rooms =[x for x, freq in count_rooms.items() if freq == 1]
        return unique_rooms

mem_per_group = int(input())
room_numbers = list(input().split(' '))
print(room_numbers)
room_numbers = list(map(int,room_numbers))
captain_rooms = get_captain_room_number(mem_per_group, room_numbers)
print(captain_rooms)