

def maxProfit(n, deadlines, incomes):
    '''
    贪心问题求解单机调度问题
    :param n:  task number
    :param deadlines:
    :param incomes:
    :return:  最大收益
    '''
    # 根据最迟时间期限从小到大排序
    ts = sorted(zip(deadlines,incomes))
    # 定义收益矩阵
    P = [[0 for i in range(n)] for j in range(n)]
    t = 0
    for i in range(n): #O(n)
        if t==0:
            P[i][t] = ts[i][1]

        else:
            if t < ts[i][0]:  #未超过时间
                P[i][t] = P[i-1][t-1] + ts[i][1]

            else:
                P[i][t] = P[i-1][t-1]
        t += 1
    print(P)



deadlines=[2,4,1,6,8,3,3]
incomes = [2,1,5,7,8,10,5]
maxProfit(len(deadlines) , deadlines, incomes)