def conflict(k, sum):
    if sum | F[k] > X:
        return True
    return False

def get_index(x, target):
    '''
    布尔向量转索引
    '''
    return [i for i in range(len(x)) if x[i] == target]

def index_to_element(indices, l):
    '''
    索引转元素
    '''
    return [l[index] for index in indices]

def Backtrack(sum , k):
    global n, x, min_num, opt_x
    if k >= n:
        if sum==X:
            # 子集个数
            tmp = x.count(True)
            if tmp < min_num:
                # 结果输出
                min_num = tmp
                indices = get_index(x,True)
                print('——————————————————————————寻找最小覆盖——————————————————————————')
                print('最小集合数目:',min_num)
                print(index_to_element(indices,F))
    else:
        for i in [True,False]:
            x[k] = i
            if x[k]:
                if not conflict(k , sum):
                    Backtrack(sum | F[k], k + 1)
            else:
                if not conflict(k, sum):
                    Backtrack(sum, k + 1)


#测试阶段
X = set([1,2,3,4,5,6])
F = [set([1,2]),set([4]),set([2,3,5]),set([1,3]),set([1,6])]
n = len(F)
x = [False for i in range(n)]
res = list()
min_num = 2^n
opt_x = []
Backtrack(set(),0)
