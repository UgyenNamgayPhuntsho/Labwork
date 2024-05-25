class Solution(object):
    def climbstairs(self, n):
        stair_number = {}
        return self.ways(n, stair_number)

    def ways(self, n, stair_number):
        if n == 1 or n == 2:
            return n
        elif n in stair_number:
            return stair_number[n]
        else:
            stair_number[n] = self.ways(n-1, stair_number) + self.ways(n-2, stair_number)
            return stair_number[n]

