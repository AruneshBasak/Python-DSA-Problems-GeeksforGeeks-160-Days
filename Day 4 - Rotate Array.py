class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d%n
        def reverse(sub_arr,start,end):
            while start<end:
                sub_arr[start], sub_arr[end] = sub_arr[end], sub_arr[start]
                start +=1
                end -=1
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
        reverse(arr,0,n-1)
        return arr
