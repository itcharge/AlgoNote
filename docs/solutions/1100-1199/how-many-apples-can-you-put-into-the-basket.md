# [1196. 最多可以买到的苹果数量](https://leetcode.cn/problems/how-many-apples-can-you-put-into-the-basket/)

- 标签：贪心、数组、排序
- 难度：简单

## 题目链接

- [1196. 最多可以买到的苹果数量 - 力扣](https://leetcode.cn/problems/how-many-apples-can-you-put-into-the-basket/)

## 题目大意

**描述**：你有一个篮子，最多能装 $5000$ 单位重量的苹果。给你一个数组 $weight$，$weight[i]$ 表示第 $i$ 个苹果的重量。

**要求**：最多能往篮子里放多少个苹果？

**说明**：

- $1 \le weight.length \le 10^{3}$。
- $1 \le weight[i] \le 10^{3}$。

**示例**：

```python
输入：weight = [100,200,150,1000]
输出：4
解释：4 个苹果总重 1450，没超过 5000，全部可以装进去。
```

## 解题思路

### 思路 1：贪心 + 排序

这道题很简单：要想装最多数量的苹果，肯定优先挑最轻的装。就像你在自助餐拿水果，盘子容量有限，想多拿几个，就挑小的拿。

**步骤拆解：**

1. 把苹果按重量从小到大排序。
2. 从最轻的开始，一个一个往篮子里放，同时累加总重量。
3. 如果加上当前苹果会超过 5000，就停下来。
4. 返回已经放进去的苹果数量。

### 思路 1：代码

```python
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # 从轻到重排序
        weight.sort()
        
        total_weight = 0  # 当前总重量
        count = 0          # 已放入的苹果数
        
        for w in weight:
            if total_weight + w <= 5000:  # 还能装得下
                total_weight += w
                count += 1
            else:  # 装不下了，后面的更重，更装不下
                break
        
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$。排序是最花时间的。
- **空间复杂度**：$O(\log n)$。排序需要一些额外的栈空间。
