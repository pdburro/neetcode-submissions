class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        for index, char in enumerate(strs[0]):
            for word in strs[1:]:
                if index >= len(word) or word[index] != char:
                    return answer
            
            answer += char
        return answer
                