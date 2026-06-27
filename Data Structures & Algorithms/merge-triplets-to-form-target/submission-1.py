class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        # filtering large
        # filtered_triplets = list(filter(lambda x: x[0] <= a or x[1] <= b or x[2] <= c, triplets))
        filtered_triplets = []
        for triplet in triplets:
            x,y,z = triplet
            if x > a or y > b or z > c:
                continue
            else:
                filtered_triplets.append(triplet)

        # print("filtered", filtered_triplets)
        xf = yf = zf = False
        for x, y, z in filtered_triplets:
            if not xf and x == a:
                xf = True
            if not yf and y == b:
                yf = True
            if not zf and z == c:
                zf = True
        return xf and yf and zf

        