class Solution:


	def maxProduct(self,arr):
		                  n = len(arr)
		                  max_prod = min_prod = result =arr[0]
		                  for i in range(1,n):
		                      num = arr[i]
		                      if num<0:
		                          max_prod,min_prod = min_prod,max_prod
		                      max_prod = max(num,max_prod * num)
		                      min_prod = min (num,min_prod * num)
		                      result = max (result,max_prod)
		                  return result

