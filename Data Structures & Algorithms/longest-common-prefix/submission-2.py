class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for index, char in enumerate(first):
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or strs[i][index] != char:
                    return first[:index]

        return first
                