class TimeMap:

    def binarySearch(self, arr, target):
        l,r = 0, len(arr)

        while l < r:
            mid = l+(r-l)//2
            if arr[mid][0] > target:
                r = mid
            else:
                l = mid+1
        
        return l-1

    def __init__(self):
        self.dt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dt[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dt[key]
        if len(arr) == 0:
            return ""
        
        index = self.binarySearch(arr, timestamp)
        if index >= len(arr):
            return arr[-1][1]
        if arr[index][0] > timestamp:
            return ""
        return arr[index][1]