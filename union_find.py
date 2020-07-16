# union_find.py
from typing import List


class UnionFind(object):
    """并查集类"""

    def __init__(self, n):
        """长度为n的并查集"""
        self.uf = [-1 for i in range(n + 1)]  # 列表0位置空出
        self.sets_count = n  # 判断并查集里共有几个集合, 初始化默认互相独立

    # def find(self, p):
    #     """查找p的根结点(祖先)"""
    #     r = p  # 初始p
    #     while self.uf[p] > 0:
    #         p = self.uf[p]
    #     while r != p:  # 路径压缩, 把搜索下来的结点祖先全指向根结点
    #         self.uf[r], r = p, self.uf[r]
    #     return p

    # def find(self, p):
    #     while self.uf[p] >= 0:
    #         p = self.uf[p]
    #     return p

    def find(self, p):
        """尾递归，同时将遍历到的路径节点指向根节点"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p，规模小的指向规模大的"""
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        if self.uf[proot] > self.uf[qroot]:  # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1  # 连通后集合总数减一

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find(p) == self.find(q)  # 即判断两个结点是否是属于同一个祖先


def main():
    # 使用并查集解决朋友圈问题，leetcode 547
    class Solution:
        def findCircleNum(self, M: List[List[int]]) -> int:
            n = len(M)
            union_find = UnionFind(n)
            for i in range(n):
                for j in range(i + 1, n):
                    if M[i][j] == 1:
                        union_find.union(i, j)
            return union_find.sets_count

    sol = Solution()

    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]

    res = sol.findCircleNum(M)
    print(res)

    M = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]

    res = sol.findCircleNum(M)
    print(res)


if __name__ == '__main__':
    main()
