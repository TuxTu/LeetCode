#64ms, 13.9MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lCP = ""
        i = 0

        if not strs:
            return lCP

        while i < len(strs[0]):
            ch = strs[0][i]
            for item in strs:
                if i >= len(item) or item[i] != ch:
                    return lCP
            lCP += ch
            i += 1

        return lCP

#64ms, 14.1MB
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:len(prefix) - 1]
                if not prefix:
                    return ""

        return prefix

print(Solution2().longestCommonPrefix(input()))