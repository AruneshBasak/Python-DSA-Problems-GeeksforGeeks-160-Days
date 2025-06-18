class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        if not arr:
            return []
        candidate1 = candidate2 = None
        count1=count2 = 0
        for num in arr:
            if num == candidate1:
                count1+=1
            elif num == candidate2:
                count2+=1
            elif count1 == 0:
                candidate1,count1 = num,1
            elif count2 == 0:
                candidate2,count2 = num ,1
            else:
                count1 -=1
                count2 -=1
        count1 = count2 =0
        for num in arr:
            if num == candidate1:
                count1+=1
            elif num == candidate2:
                count2+= 1
        result = []
        if count1> n //3:
            result.append(candidate1)
        if count2> n //3:
            result.append(candidate2)
        return sorted(result)
        

