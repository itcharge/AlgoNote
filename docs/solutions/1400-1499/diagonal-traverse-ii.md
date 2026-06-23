# [1424. 对角线遍历 II](https://leetcode.cn/problems/diagonal-traverse-ii/)

- 标签：数组、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [1424. 对角线遍历 II - 力扣](https://leetcode.cn/problems/diagonal-traverse-ii/)

## 题目大意

**描述**：给定一个二维整数数组 $nums$（每行长度可能不同），按对角线顺序遍历。对角线方向为「右上到左下」，即同一对角线上元素的行列索引和 $(i+j)$ 相同。

**要求**：返回按对角线顺序遍历得到的一维数组。

**说明**：
- $1 \le nums.length \le 10^5$。
- $1 \le nums[i].length \le 10^5$。
- $nums$ 总元素数 $\le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/04/23/sample_1_1784.png)

```python
输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]
```

- 示例 2：

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/04/23/sample_2_1784.png)

```python
输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
```

## 解题思路

### 思路 1：按 (i+j, -i) 排序

#### 1. 核心思想

对于每个元素 $(i, j)$：
- 属于第 $(i+j)$ 条对角线。
- 在同一对角线内，按 $i$ 降序（即从下到上）遍历。

因此可以将所有元素按键 $(i+j, -i)$ 排序。

#### 2. 具体步骤

**第 1 步**：遍历 $nums$，将所有 $(i, j, val)$ 加入列表。

**第 2 步**：按 $(i+j, -i)$ 排序。

**第 3 步**：提取值返回。

#### 3. 举例说明

以 $nums = [[1,2,3],[4,5,6],[7,8,9]]$ 为例：

元素的 $(i+j, -i)$：
- $(0,0)$：$(0, 0)$
- $(0,1)$：$(1, 0)$
- $(0,2)$：$(2, 0)$
- $(1,0)$：$(1, -1)$
- $(1,1)$：$(2, -1)$
- $(1,2)$：$(3, -1)$
- $(2,0)$：$(2, -2)$
- $(2,1)$：$(3, -2)$
- $(2,2)$：$(4, -2)$

排序后顺序：$(0,0), (1,-1), (1,0), (2,-2), (2,-1), (2,0), (3,-2), (3,-1), (4,-2)$

输出：$[1, 4, 2, 7, 5, 3, 8, 6, 9]$。

### 思路 1：代码

```python
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        elements = []
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                elements.append((i + j, -i, val))  # (对角线, 行倒序, 值)
        elements.sort()
        return [val for _, _, val in elements]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(N \log N)$，$N$ 为总元素数。
- **空间复杂度**：$O(N)$。

---

### 思路 2：BFS 层序遍历

核心观察：遍历顺序就是 BFS 的层序遍历，从 $(0,0)$ 开始，每层向右和向下扩展。

```python
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        q = deque([(0, 0)])
        visited = {(0, 0)}
        while q:
            i, j = q.popleft()
            ans.append(nums[i][j])
            # 向下走
            if i + 1 < len(nums) and j < len(nums[i + 1]) and (i + 1, j) not in visited:
                q.append((i + 1, j))
                visited.add((i + 1, j))
            # 向右走
            if j + 1 < len(nums[i]) and (i, j + 1) not in visited:
                q.append((i, j + 1))
                visited.add((i, j + 1))
        return ans
```

BFS 法 $O(N)$ 时间，但需要处理访问标记。
