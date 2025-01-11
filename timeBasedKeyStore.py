from collections import defaultdict
from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if not key:
            return ""
        values = self.store[key]

        time = [t for t,s in values]

        idx = bisect_right(time, timestamp) - 1

        if idx >= 0:
            return values[idx][1]
        return ""

        
'''
Time Complexity:

set: 
𝑂
(
1
)
O(1) — appending to a list.
get: 
𝑂
(
log
⁡
𝑛
)
O(logn) — binary search over timestamps.
Space Complexity:

𝑂
(
𝑁
)
O(N) — where 
𝑁
N is the total number of set operations'''
