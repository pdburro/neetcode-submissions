class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}
        answer = []

        for index, n in enumerate(nums):
            complement = target - n

            if complement in solution:
                return [solution[complement], index]

            solution[n] = index
