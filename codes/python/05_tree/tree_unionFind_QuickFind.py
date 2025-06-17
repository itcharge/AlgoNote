class UnionFind:
    def __init__(self, n):                          # 初始化：将每个元素的集合编号初始化为数组下标索引
        self.ids = [i for i in range(n)]

    def find(self, x):                              # 查找元素所属集合编号内部实现方法
        return self.ids[x]

    def union(self, x, y):                          # 合并操作：将集合 x 和集合 y 合并成一个集合
        x_id = self.find(x)
        y_id = self.find(y)
        
        if x_id == y_id:                            # x 和 y 已经同属于一个集合
            return False
        
        for i in range(len(self.ids)):              # 将两个集合的集合编号改为一致
            if self.ids[i] == y_id:
                self.ids[i] = x_id
        return True

    def is_connected(self, x, y):                   # 查询操作：判断 x 和 y 是否同属于一个集合
        return self.find(x) == self.find(y)