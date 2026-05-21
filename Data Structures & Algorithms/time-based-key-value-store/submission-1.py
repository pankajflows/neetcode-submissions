class TimeMap:

    def __init__(self):
        self.store = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        array = self.store[key]

        left = 0
        right = len(array)-1
        index = -1

        while left <= right:
            mid = left + math.floor((right-left)/2)
            if array[mid][0] < timestamp:
                left = mid + 1
                index = mid
            elif array[mid][0] > timestamp:
                right = mid - 1
                # index = right
            else:
                index = mid
                break

        # print("index", index)
        if index < 0:
            return ""
        else:
            return array[index][1]
        
        
