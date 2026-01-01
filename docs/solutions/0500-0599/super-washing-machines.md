# [0517. 超级洗衣机](https://leetcode.cn/problems/super-washing-machines/)

- 标签：贪心、数组
- 难度：困难

## 题目链接

- [0517. 超级洗衣机 - 力扣](https://leetcode.cn/problems/super-washing-machines/)

## 题目大意

**描述**：

假设有 $n$ 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
在每一步操作中，你可以选择任意 $m$ ($1 \le m \le n$) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个整数数组 $machines$ 代表从左至右每台洗衣机中的衣物数量。

**要求**：

给出能让所有洗衣机中剩下的衣物的数量相等的「最少的操作步数」。如果不能使每台洗衣机中衣物的数量相等，则返回 $-1$。

**说明**：

- $n == machines.length$。
- $1 \le n \le 10^{4}$。
- $0 \le machines[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：machines = [1,0,5]
输出：3
解释：
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2
```

- 示例 2：

```python
输入：machines = [0,3,0]
输出：2
解释：
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1
```

## 解题思路

### 思路 1：贪心算法

首先判断是否可能达到平衡：总衣物数必须能被洗衣机数量整除。

设目标值为 $target = sum(machines) / n$。

关键观察：

1. 对于每台洗衣机 $i$，计算它需要转移的衣物数量：$diff[i] = machines[i] - target$
2. 计算前缀和 $prefix[i]$，表示前 $i$ 台洗衣机需要向右转移的衣物总数
3. 最少操作步数取决于两个因素：
   - 某台洗衣机需要转出的最大衣物数：$\max(diff[i])$（如果为正）
   - 经过某台洗衣机的最大流量：$\max(|prefix[i]|)$

答案为 $\max(\max(diff[i]), \max(|prefix[i]|))$。

### 思路 1：代码

```python
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        
        # 如果无法平均分配，返回 -1
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        prefix_sum = 0
        
        for i in range(n):
            # 当前洗衣机需要转移的衣物数（正数表示需要转出，负数表示需要转入）
            diff = machines[i] - target
            prefix_sum += diff
            
            # 更新最大操作步数
            # 1. 当前洗衣机需要转出的衣物数
            # 2. 经过当前位置的最大流量
            max_moves = max(max_moves, abs(prefix_sum), diff)
        
        return max_moves
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是洗衣机的数量，只需要遍历一次数组。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
