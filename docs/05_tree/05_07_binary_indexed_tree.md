## 1. 树状数组简介

### 1.1 树状数组的定义

> **树状数组（Binary Indexed Tree）**：也因其发明者命名为 Fenwick 树，最早 Peter M. Fenwick 于 1994 年以 A New Data Structure for Cumulative Frequency Tables 为题发表在 SOFTWARE PRACTICE AND EXPERIENCE。其初衷是解决数据压缩里的累积频率（Cumulative Frequency）的计算问题，现多用于高效计算数列的前缀和，区间和。它可以以 $O(\log n)$ 的时间得到任意前缀 $\sum_{i=1}^{j}A[i], 1 \le j \le n$，并同时支持在 $O(\log n)$ 时间内支持动态单点值的修改。空间复杂度为 $O(n)$。

### 1.2 树状数组的原理

树状数组的核心思想是利用二进制数的特性，将前缀和分解成多个子区间的和。具体来说：

1. 每个节点存储的是以该节点为根的子树中所有节点的和
2. 对于任意一个数 $x$，其二进制表示中最低位的 1 所在的位置决定了该节点在树中的层级
3. 通过位运算可以快速找到需要更新的节点和需要求和的区间

例如，对于数组 $[1, 2, 3, 4, 5]$，其树状数组的结构如下：
```
      [15]
    /     \
  [3]     [12]
 /  \     /  \
[1] [2] [3]  [9]
              / \
            [4] [5]
```

## 2. 树状数组的基本操作

### 2.1 树状数组的建立

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def build(self, arr):
        for i in range(len(arr)):
            self.update(i + 1, arr[i])
```

### 2.2 树状数组的修改

```python
def update(self, index, val):
    while index <= self.n:
        self.tree[index] += val
        index += self.lowbit(index)
```

### 2.3 树状数组的求和

```python
def query(self, index):
    res = 0
    while index > 0:
        res += self.tree[index]
        index -= self.lowbit(index)
    return res
```

## 3. 树状数组的应用

### 3.1 单点更新 + 区间求值

这是树状数组最基本的应用，可以高效地：
1. 修改某个位置的值
2. 查询任意区间的和

时间复杂度：
- 单点更新：$O(\log n)$
- 区间查询：$O(\log n)$

具体实现：
```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def query_range(self, left, right):
        return self.query(right) - self.query(left - 1)

# 使用示例
def example_single_point_update():
    # 初始化数组 [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    bit = BinaryIndexedTree(n)
    
    # 构建树状数组
    for i in range(n):
        bit.update(i + 1, arr[i])
    
    # 单点更新：将第3个元素加2
    bit.update(3, 2)  # arr[2] += 2
    
    # 查询区间和：查询[2,4]的和
    sum_range = bit.query_range(2, 4)
    print(f"区间[2,4]的和为：{sum_range}")  # 输出：区间[2,4]的和为：11
```

### 3.2 区间更新 + 单点求值

通过差分数组的思想，可以实现：
1. 区间更新：将区间 $[l, r]$ 的所有值加上 $val$
2. 单点查询：查询某个位置的值

时间复杂度：
- 区间更新：$O(\log n)$
- 单点查询：$O(\log n)$

具体实现：
```python
class RangeUpdateBIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def range_update(self, left, right, val):
        # 在left位置加上val
        self.update(left, val)
        # 在right+1位置减去val
        self.update(right + 1, -val)

# 使用示例
def example_range_update():
    # 初始化数组 [0, 0, 0, 0, 0]
    n = 5
    bit = RangeUpdateBIT(n)
    
    # 区间更新：[2,4]区间所有元素加3
    bit.range_update(2, 4, 3)
    
    # 单点查询：查询第3个元素的值
    value = bit.query(3)
    print(f"第3个元素的值为：{value}")  # 输出：第3个元素的值为：3
```

### 3.3 求逆序对数

利用树状数组可以高效求解数组中的逆序对数量：
1. 对数组进行离散化处理
2. 从后向前遍历，统计每个数前面比它大的数的个数
3. 将统计结果累加得到逆序对总数

时间复杂度：$O(n \log n)$

具体实现：
```python
class InversionCountBIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def lowbit(self, x):
        return x & (-x)
    
    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res
    
    def count_inversions(self, arr):
        # 离散化处理
        sorted_arr = sorted(set(arr))
        rank = {val: i + 1 for i, val in enumerate(sorted_arr)}
        
        # 从后向前遍历，统计逆序对
        count = 0
        for i in range(len(arr) - 1, -1, -1):
            # 查询当前数前面比它大的数的个数
            count += self.query(rank[arr[i]] - 1)
            # 更新当前数的出现次数
            self.update(rank[arr[i]], 1)
        
        return count

# 使用示例
def example_inversion_count():
    # 测试数组 [5, 2, 6, 1, 3]
    arr = [5, 2, 6, 1, 3]
    n = len(arr)
    bit = InversionCountBIT(n)
    
    # 计算逆序对数量
    inversions = bit.count_inversions(arr)
    print(f"数组中的逆序对数量为：{inversions}")  # 输出：数组中的逆序对数量为：6
```

## 参考资料

- 【书籍】ACM-ICPC 程序设计系列 - 算法设计与实现 - 陈宇 吴昊 主编
- 【书籍】算法训练营 陈小玉 著
- 【博文】[聊聊树状数组 Binary Indexed Tree - halfrost](https://halfrost.com/binary_indexed_tree/)
- 【博文】[树状数组学习笔记 - AcWing](https://www.acwing.com/blog/content/80/)
