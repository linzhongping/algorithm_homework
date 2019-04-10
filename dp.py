

def maxSubSeq(s):

    dp = [[0 for i in range(len(s))] for j in range(len(s))]  #dp数组
    pos = 0
    max_len = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                if i ==0 or j==len(s)-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j+1] +1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    pos = i
    left = pos + 1 - max_len
    right = left + max_len
    return s[left:right]



print(maxSubSeq('asdf12353425fdsa87724'))