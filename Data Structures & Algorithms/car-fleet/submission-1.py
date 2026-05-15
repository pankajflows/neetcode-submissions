class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(position[i], speed[i]) for i in range(len(speed))]
        pos_speed.sort(key=lambda p: p[0], reverse=True)
        # print(pos_speed)
        fleets = deque()

        for ps in pos_speed:
            t = (target-ps[0])/ps[1]
            # print("comp", fleets, t)
            if fleets:
                if fleets[-1] < t:
                    fleets.append(t)
            else:
                fleets.append(t)

        # print(fleets)
        return len(fleets)
