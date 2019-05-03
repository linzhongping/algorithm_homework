# 求解凸包
import random
import matplotlib.pyplot as plt


# 通过计算三角形p1p2p3的面积（点在直线左边结果为正，直线右边结果为负）来判断 p3相对于直线p1p2的位置
def calTri(p1, p2, p3):
    size = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p3[0] * p2[1] - p2[0] * p1[1] - p1[0] * p3[1]
    return size


# 找出距离直线最远的点（该点与直线围成的三角形的面积为正且最大）
def maxSize(seq, dot1, dot2, dotSet):
    '''
    :param seq:
    :param dot1: 左侧点
    :param dot2: 右侧点
    :param dotSet: 点集
    :return:
    '''
    maxSize = float('-inf')
    maxDot = ()
    online = []
    maxSet = []
    for u in seq:
        size = calTri(dot1, dot2, u)
        # 判断点u是否能是三角形u dot1 dot2 的面积为正
        if size < 0:
            continue
        elif size == 0:
            online.append(u)
        # 若面积为正，则判断是否是距离直线最远的点
        if size > maxSize:
            if len(maxDot) > 0:
                maxSet.append(maxDot)
            maxSize = size
            maxDot = u
        else:
            maxSet.append(u)
    # 结果判断
    # maxSet为空
    if not maxSet:
        # 没找到分割点,同时可能有点落在直线dot1 dot2上
        if not maxDot:
            dotSet.extend(online)
            return [], ()
        # 有分割点
        else:
            dotSet.append(maxDot)
            return [], maxDot
    # maxSet不为空
    else:
        dotSet.append(maxDot)
        return maxSet, maxDot


# 找出据直线最远的点（该点与直线围成的三角形的面积为负数且最大）
def minSize(seq, dot1, dot2, dotSet):
    minSize = float('inf')
    minDot = ()
    online = []
    minSet = []
    for u in seq:
        size = calTri(dot1, dot2, u)
        # 判断点u是否能是三角形u dot1 dot2 的面积为负
        if size > 0:
            continue
        elif size == 0:
            online.append(u)
        # 若面积为负，则判断是否是距离直线最远的点
        if size < minSize:
            if len(minDot) > 0:
                minSet.append(minDot)
            minDot = u
            minSize = size
        else:
            minSet.append(u)
    # 结果判断
    # maxSet为空
    if not minSet:
        # 没找到分割点,同时可能有点落在直线dot1 dot2上
        if not minDot:
            dotSet.extend(online)
            return [], ()
        # 有分割点
        else:
            dotSet.append(minDot)
            return [], minSet
    # maxSet不为空
    else:
        dotSet.append(minDot)
        return minSet, minDot

# 上包的递归划分
def divideUp(seq, dot1, dot2, dot3, dot4, dotSet=None):
    print(dot1, dot2, dot3, dot4)
    # 初始化第一次运行时的参数
    if len(seq) == 0:
        return dotSet
    if dotSet is None:
        dotSet = []
    if len(seq) == 1:
        dotSet.append(seq[0])
        return dotSet
    leftSet, rightSet = [], []
    # 划分上包左边的点集
    leftSet, maxDot = maxSize(seq, dot1, dot2, dotSet)



    # 对上包左包的点集进一步划分
    if leftSet:
        divideUp(leftSet, dot1, maxDot, maxDot, dot2, dotSet)

    # 划分上包右边的点集
    rightSet, maxDot = maxSize(seq, dot3, dot4, dotSet)


    # 对上包右包的点集进一步划分
    if rightSet:
        divideUp(rightSet, dot3, maxDot, maxDot, dot4, dotSet)

    return dotSet


# 下包的递归划分
def divideDown(seq, dot1, dot2, dot3, dot4, dotSet=None):
    # 初始化第一次运行时的参数
    if len(seq) == 0:
        return dotSet
    if dotSet is None:
        dotSet = []
    if len(seq) == 1:
        dotSet.append(seq[0])
        return dotSet
    leftSet, rightSet = [], []
    # 划分下包左边的点集
    leftSet, minDot = minSize(seq, dot1, dot2, dotSet)


    # 对下包的左包进行进一步划分
    if leftSet:
        divideDown(leftSet, dot1, minDot, minDot, dot2, dotSet)

    # 划分下包右包的点集
    rightSet, minDot = minSize(seq, dot3, dot4, dotSet)


    # 对下包的右包进一步划分
    if rightSet:
        divideDown(rightSet, dot3, minDot, minDot, dot4, dotSet)

    return dotSet


# 递归主函数
def mainDivide(seq):
    # 将序列中的点按横坐标升序排序
    seq.sort()
    res = []
    # 获取横坐标做大、最小的点及横坐标中位数
    dot1 = seq[0]
    dot2 = seq[-1]
    seq1 = []
    maxSize = float('-inf')
    maxDot = ()
    seq2 = []
    minSize = float('inf')
    minDot = ()
    # 对序列划分为直线dot1 dot2左右两侧的点集并找出两个点集的距直线最远点
    for u in seq[1:-1]:
        size = calTri(dot1, dot2, u)
        if size > 0:
            if size > maxSize:
                if len(maxDot) > 0:
                    seq1.append(maxDot)
                maxSize = size
                maxDot = u
                continue
            else:
                seq1.append(u)
        elif size < 0:
            if size < minSize:
                if len(minDot) > 0:
                    seq2.append(minDot)
                minSize = size
                minDot = u
                continue
            else:
                seq2.append(u)
    print('seq1', seq1, maxDot)
    print('seq2', seq2, minDot)
    # 调用内建递归函数
    res1 = divideUp(seq1, dot1, maxDot, maxDot, dot2)
    res2 = divideDown(seq2, dot1, minDot, minDot, dot2)
    if res1 is not None:
        res.extend(res1)
    if res2 is not None:
        res.extend(res2)
    for u in [dot for dot in [dot1, dot2, maxDot, minDot] if len(dot) > 0]:
        res.append(u)
    return res

import random
random.seed(1996)
seq0 = [(random.randint(-1000, 1000), random.randint(-1000, 1000)) for x in range(200000)]
seq0 = list(set(seq0))
res = mainDivide(seq0)
print('res', sorted(res))
plt.axis([-1100, 1100, -1100, 1100])
plt.title("overview")
plt.scatter([dot[0] for dot in seq0], [dot[1] for dot in seq0], color='black')
plt.scatter([dot[0] for dot in res], [dot[1] for dot in res], color='red')
plt.show()