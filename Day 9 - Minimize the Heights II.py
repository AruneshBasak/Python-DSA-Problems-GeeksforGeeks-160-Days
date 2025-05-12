class Solution:
    def getMinDiff(self, arr,k):
        n = len(arr)
        if n ==1:
            return 0
        arr.sort()
        ans = arr[-1]-arr[0]
        smallest = arr[0]+k
        largest = arr[-1]-k
        for i in range (1,n):
            if arr[i]-k<0:
                continue
            min_height = min(smallest,arr[i]-k)
            max_height = max(largest,arr[i-1]+k)
            ans = min(ans,max_height-min_height)
        return ans
