def circularSubarraySum(arr):
    def kadane(nums):
        max_sum = curr = nums[0]
        for num in nums[1:]:
            curr = max(num,curr +num)
            max_sum = max(max_sum,curr)
        return max_sum
    def min_kadane(nums):
        min_sum = curr = nums[0]
        for num in nums[1:]:
            curr = min (num,curr +num)
            min_sum = min (min_sum,curr)
        return min_sum
    total_sum = sum(arr)
    max_kadane = kadane(arr)
    min_kad = min_kadane(arr)
    
    if max_kadane<0:
        return max_kadane
    return max(max_kadane,total_sum-min_kad
