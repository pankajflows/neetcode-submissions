class CountSquares:

    def __init__(self):
        self.bank = defaultdict(lambda: defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        x, y = point
        self.bank[x][y] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        
        for k,v in self.bank.items():
            if k != x:
                x_diff = abs(k-x)
                for l,m in v.items():
                    y_diff = abs(l-y)
                    if x_diff == y_diff: # diagonal found
                        point_3 = (x, l)
                        point_4 = (k, y)
                        freq_xl = self.bank.get(x, {}).get(l, 0)
                        freq_ky = self.bank.get(k, {}).get(y, 0)
                        if freq_xl and freq_ky:
                            count += m * freq_xl * freq_ky 

        return count


        
