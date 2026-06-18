class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        bank = dict()
        for h in hand:
            bank[h] = bank.get(h,0) + 1

        count = 0
        while bank:
            mini = float("inf")
            for h in bank.keys():
                mini = min(mini, h)

            for i in range(groupSize):
                if mini not in bank:
                    return False
                
                bank[mini] -= 1
                if bank[mini] <= 0:
                    del bank[mini]
                mini += 1
                
                

        return True

        