class Solution:
	def duplicateZeros(self, arr: list[int]) -> None:
		i = 0
		starting_len = len(arr)  # this is used to remove all elements that exceed the starting len of arr
		while i < len(arr):
			if arr[i] == 0:
				arr.insert(i + 1, 0)  # inserts a 0 one place after the first 0
				i += 2  # this is to stop infinitely adding 0 because it will keep adding 0 and finding that 0 next loop
			else:
				i += 1  # goes to next loop

		while len(arr) > starting_len:  # loops until it's the same len as it started with
			arr.pop(-1)