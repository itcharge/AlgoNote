# [1376. 通知所有员工所需的时间](https://leetcode.cn/problems/time-needed-to-inform-all-employees/)

- 标签：树、深度优先搜索、图
- 难度：中等

## 题目链接

- [1376. 通知所有员工所需的时间 - 力扣](https://leetcode.cn/problems/time-needed-to-inform-all-employees/)

## 题目大意

**描述**：公司有 $n$ 名员工，编号 $0 \sim n-1$，$headID$ 是公司负责人的编号。给定一个 `manager` 数组，其中 $manager[i]$ 表示第 $i$ 名员工的直属上级。负责人 $headID$ 的上级为 $-1$。给定一个 `informTime` 数组，其中 $informTime[i]$ 表示第 $i$ 名员工通知其所有直接下属所需的时间（以分钟为单位）。

通知过程：负责人首先通知其直接下属，下属继续向下级通知，逐级传递。求通知所有员工所需的总时间。

**要求**：返回通知到所有员工所需的最少分钟数。

**说明**：
- $1 \le n \le 10^5$。
- $0 \le informTime[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：n = 1, headID = 0, manager = [-1], informTime = [0]
输出：0
解释：公司总负责人是该公司的唯一一名员工。
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/03/08/graph.png)

```python
输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
输出：1
解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
上图显示了公司员工的树结构。
```


## 解题思路

### 思路 1：建图 + DFS（树形 DP）

#### 1. 核心思想

公司组织结构是一棵树。每个人收到通知后，需要花 $informTime[i]$ 分钟通知其所有直接下属，且下属之间是**并行**通知的。

因此，从 $i$ 开始通知其所有下属所需的总时间 = $informTime[i] + \max(\text{所有下属所需的总时间})$。

这是典型的树形 DP + 后序遍历。

#### 2. 具体步骤

**第 1 步：建图**

用邻接表存储每个节点的直接下属列表。遍历 $i = 0 \to n-1$，将 $i$ 加入 $manager[i]$ 的子节点列表。

**第 2 步：DFS 后序遍历**

定义 $dfs(node)$ 返回从 $node$ 开始通知完其所有下属所需的总时间：
- 如果 $node$ 没有下属（叶子节点），返回 $0$。
- 否则，对每个子节点 $child$ 递归调用 $dfs(child)$，取最大值，加上 $informTime[node]$。

**第 3 步**：返回 $dfs(headID)$。

#### 3. 举例说明

以 $n=6$，$headID=2$，$manager=[2,2,-1,2,2,2]$，$informTime=[0,0,1,0,0,0]$ 为例：

```
       2 (1 min)
     /|\ \
    0 1 3 4 5
```

$informTime[2] = 1$，其下属 $0,1,3,4,5$ 都没有下属，所需时间各为 $0$。

总时间 = $1 + \max(0,0,0,0,0) = 1$。

更复杂的例子：$n=7$，$manager=[1,2,-1,2,1,4,4]$，$informTime=[0,1,2,0,3,0,0]$：

```
        2 (2 min)
       / \
      1   3
     / \   \
    0   4   (叶子)
       / \
      5   6
```

- $dfs(5)=0, dfs(6)=0, dfs(4)=3+max(0,0)=3$
- $dfs(0)=0, dfs(1)=1+max(0,3)=4$
- $dfs(3)=0$
- $dfs(2)=2+max(4,0)=6$

总时间 = $6$ 分钟。

### 思路 1：代码

```python
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # 第 1 步：建图（邻接表）
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                children[m].append(i)

        # 第 2 步：DFS 后序遍历
        def dfs(node):
            if not children[node]:
                return 0
            # 取所有子节点的最大通知时间
            max_child_time = max(dfs(child) for child in children[node])
            return informTime[node] + max_child_time

        return dfs(headID)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个节点遍历一次。
- **空间复杂度**：$O(n)$，邻接表存储 $O(n)$，递归栈 $O(h)$ 最坏 $O(n)$。

---

### 思路 2：迭代（后序遍历栈）

为避免递归栈溢出（最坏情况下树退化为链），可以用栈实现迭代后序遍历：

```python
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                children[m].append(i)

        # 存储每个节点通知完下属所需的时间
        time_needed = [0] * n
        # 后序遍历栈：(node, state) state=0 表示第一次访问，state=1 表示子节点处理完毕
        stack = [(headID, 0)]

        while stack:
            node, state = stack.pop()
            if state == 0:
                # 第一次访问，压回并压入子节点
                stack.append((node, 1))
                for child in children[node]:
                    stack.append((child, 0))
            else:
                # 子节点已处理完，计算本节点时间
                max_time = 0
                for child in children[node]:
                    max_time = max(max_time, time_needed[child])
                time_needed[node] = informTime[node] + max_time

        return time_needed[headID]
```

迭代法避免了最大递归深度限制，在 $n=10^5$ 的最坏情况下访问更稳定。
