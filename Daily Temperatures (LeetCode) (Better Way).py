class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		result = [0] * len(temperatures)
		stack = [] # stores index

		# decreasing stack implementation
		for i in range(len(temperatures)):
			while stack and temperatures[stack[-1]] < temperatures[i]:
				idx = stack.pop()
				result[idx] = i - idx
			stack.append(i)

		return result