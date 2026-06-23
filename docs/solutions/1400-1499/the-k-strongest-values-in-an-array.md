# [1471. 数组中的 k 个最强值](https://leetcode.cn/problems/the-k-strongest-values-in-an-array/)

- 标签：数组、双指针、排序
- 难度：中等

## 题目链接

- [1471. 数组中的 k 个最强值 - 力扣](https://leetcode.cn/problems/the-k-strongest-values-in-an-array/)

## 题目大意

**描述**：给定一个整数数组 $arr$ 和一个整数 $k$。定义「强度」为 $|arr[i] - median|$，其中 $median$ 是数组中位数（从小到大排序后第 $\lfloor (n-1)/2 \rfloor$ 个元素）。

比较规则：
- 强度大的更强。
- 如果强度相同，值大的更强。

**要求**：返回数组中 $k$ 个最强元素（按强度降序，强度相同按值降序）。

**说明**：
- $1 \le arr.length \le 10^5$。
- $1 \le k \le arr.length$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,3,4,5], k = 2
输出：[5,1]
解释：中位数为 3，按从强到弱顺序排序后，数组变为 [5,1,4,2,3]。最强的两个元素是 [5, 1]。[1, 5] 也是正确答案。
注意，尽管 |5 - 3| == |1 - 3| ，但是 5 比 1 更强，因为 5 > 1 。
```

- 示例 2：

```python
输入：arr = [1,1,3,5,5], k = 2
输出：[5,5]
解释：中位数为 3, 按从强到弱顺序排序后，数组变为 [5,5,1,1,3]。最强的两个元素是 [5, 5]。
```

## 解题思路

### 思路 1：排序 + 双指针

#### 1. 核心思想

先排序，确定中位数 $median = arr[(n-1)//2]$。然后在排序后的数组两端用双指针取 $k$ 个最强元素（距离中位数越远越强）。

#### 2. 具体步骤

**第 1 步**：排序 $arr$。

**第 2 步**：计算中位数索引 $mid = (n-1)//2$，$median = arr[mid]$。

**第 3 步**：双指针 $l=0, r=n-1$。循环 $k$ 次：
- 比较 $arr[l]$ 和 $arr[r]$ 与中位数的距离，取更强的那个（距离相同取值大的）。
- 将结果加入答案，移动指针。

**第 4 步**：返回结果。

#### 3. 举例说明

以 $arr = [1,2,3,4,5], k = 2$ 为例：

排序后：$[1,2,3,4,5]$，中位数 $arr[2]=3$。

双指针：
- 比较左边 $1$（$|1-3|=2$）和右边 $5$（$|5-3|=2$）：强度相同，值 $5 > 1$，取 $5$，$r=3$
- 比较 $1$（强度 $2$）和 $4$（强度 $1$）：取 $1$，$l=1$

结果：$[5, 1]$。

### 思路 1：代码

```python
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        l, r = 0, n - 1
        ans = []

        for _ in range(k):
            left_dist = abs(arr[l] - median)
            right_dist = abs(arr[r] - median)
            if right_dist >= left_dist:
                ans.append(arr[r])
                r -= 1
            else:
                ans.append(arr[l])
                l += 1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序。
- **空间复杂度**：$O(1)$。
