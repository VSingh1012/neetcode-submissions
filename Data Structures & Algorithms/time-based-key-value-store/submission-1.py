class TimeMap:

    def __init__(self):
        # constructor
        self.records = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.records[key].append((timestamp, value)) # O(1)

        

    def get(self, key: str, timestamp: int) -> str:
        # O(log(N))
        res = self.records.get(key)
        if not res or timestamp < res[0][0]:
            return ""

        # commence the binary search 
        l, r = 0, len(res) - 1

        while l <= r:
            m = (l + r) // 2
            if res[m][0] == timestamp:
                return res[m][1]
            elif timestamp > res[m][0]:
                l = m + 1
            else:
                r = m - 1

        # if we cannot find the corresponding timestamp, choose the next largest at pointer r
        return res[r][1]
        
            








        
