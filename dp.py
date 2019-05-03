

def maxSubSeq(s):
    # 生成dp数
    dp = [[0 for i in range(len(s))] for j in range(len(s))]
    pos = 0
    max_len = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i]== s[j]:
                dp[i][j]=1
    for i in range(len(s)+1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                # 处理边界条件
                if i ==0 or j==len(s)-1:
                    dp[i][j] = 1
                #递推式子更新
                else:
                    dp[i][j] = dp[i-1][j+1] + dp[i][j]
                #记录最优解
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    pos = i
    left = pos + 1 - max_len
    right = left + max_len

    return s[left:right]


# 测试阶段1
# import random
# import string
# for i in range(10):
#     ran_str = ''.join(random.sample(string.ascii_letters.lower(), 48))
#     print(ran_str, '\t', maxSubSeq(ran_str))


# 测试阶段2
test_str=['',
          'ALGORITHM',
          'RCURSION',
          'REDIVIDE',
          'a',
          'abcddcba',
          'qazxxwedcdewsxzaq',
          'qwer3765kjhfdkgh234'
          ]
print('\n'.join([s+'\t'+maxSubSeq(s) for s in test_str]))

