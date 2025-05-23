class Solution:
    def getSecondLargest(self, arr):
        first= second = -1
        for num in arr:
            if num>first:
                second = first
                first = num
            elif num!= first and num>second:
                second = num
        return secon
