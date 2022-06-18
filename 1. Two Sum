class Solution:
	def twoSum(self, A: List[int], target: int) -> List[int]:
		# add your logic here
		dict={}
		
		for i in range(len(A)):
			temp= target-A[i]
			if temp in dict:
				return [dict[temp],i]
			else:
				dict[A[i]] = i
