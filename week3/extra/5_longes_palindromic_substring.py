class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        start = 0
        max_len = 0

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2:
                        dp[i][j] == True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start: start + max_len]
