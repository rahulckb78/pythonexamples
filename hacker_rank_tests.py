def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    l = res = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r - l + 1)
    return res

str_one = "After approximately 433 hours, 18 days, and 288 orbits around Earth, covering nearly 7.6 million miles since docking with the International Space Station, the Axiom Mission 4 crew is officially homeward bound. Check here for key updates."
print(f"Long sub-string is: {lengthOfLongestSubstring(str_one)}")

def merge(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # if merged is empty or no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # there is overlap, so we merge
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
    
intervals = [[1,3], [2,6], [8,10], [15,18]]

print(f"Merged intervals: {merge(intervals)}")
    
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first item (least recently used)
            self.cache.popitem(last=False)

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))   # returns 1
lru.put(3, 3)       # evicts key 2
print(lru.get(2))   # returns -1 (not found)
lru.put(4, 4)       # evicts key 1
print(lru.get(1))   # returns -1
print(lru.get(3))   # returns 3
print(lru.get(4))   # returns 4

