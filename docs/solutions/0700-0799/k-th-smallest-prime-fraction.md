# [0786. 第 K 个最小的质数分数](https://leetcode.cn/problems/k-th-smallest-prime-fraction/)

- 标签：数组、双指针、二分查找、排序、堆（优先队列）
- 难度：中等

## 题目链接

- [0786. 第 K 个最小的质数分数 - 力扣](https://leetcode.cn/problems/k-th-smallest-prime-fraction/)

## 题目大意

**描述**：

给定一个按递增顺序排序的数组 $arr$ 和一个整数 $k$。数组 $arr$ 由 $1$ 和若干质数组成，且其中所有整数互不相同。

对于每对满足 $0 \le i < j < arr.length$ 的 $i$ 和 $j$，可以得到分数 $arr[i] / arr[j]$。

**要求**：

计算第 $k$ 个最小的分数。以长度为 $2$ 的整数数组返回你的答案, 这里 $answer[0] == arr[i]$ 且 $answer[1] == arr[j]$。

**说明**：

- $2 \le arr.length \le 10^{3}$。
- $1 \le arr[i] \le 3 * 10^{4}$。
- $arr[0] == 1$。
- $arr[i]$ 是一个「质数」，$i \gt 0$。
- arr 中的所有数字「互不相同」，且按「严格递增」排序。
- $1 \le k \le arr.length \times (arr.length - 1) / 2$。

- 进阶：你可以设计并实现时间复杂度小于 $O(n^2)$ 的算法解决此问题吗？

**示例**：

- 示例 1：

```python
输入：arr = [1,2,3,5], k = 3
输出：[2,5]
解释：已构造好的分数,排序后如下所示: 
1/5, 1/3, 2/5, 1/2, 3/5, 2/3
很明显第三个最小的分数是 2/5
```

- 示例 2：

```python
输入：arr = [1,7], k = 1
输出：[1,7]
```

## 解题思路

### 思路 1：优先队列（最小堆）

这道题要求找到第 $k$ 个最小的质数分数。可以使用优先队列来解决。

**解题步骤**：

1. 将所有可能的分数 $\frac{arr[i]}{arr[j]}$（$i < j$）加入优先队列。
2. 由于数组是递增的，对于每个分母 $arr[j]$，最小的分数是 $\frac{arr[0]}{arr[j]}$。
3. 使用最小堆，初始时将所有 $\frac{arr[0]}{arr[j]}$（$j > 0$）加入堆中。
4. 每次从堆中取出最小的分数，如果这是第 $k$ 个，返回结果。
5. 如果取出的分数是 $\frac{arr[i]}{arr[j]}$ 且 $i + 1 < j$，将 $\frac{arr[i+1]}{arr[j]}$ 加入堆中。

**优化**：使用索引而不是实际的分数值，避免浮点数比较的精度问题。

### 思路 1：代码

```python
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        import heapq
        
        n = len(arr)
        # 最小堆，存储 (分数值, 分子索引, 分母索引)
        heap = []
        
        # 初始化：将所有 arr[0]/arr[j] 加入堆
        for j in range(1, n):
            heapq.heappush(heap, (arr[0] / arr[j], 0, j))
        
        # 取出前 k-1 个最小的分数
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            # 如果还有更大的分子，加入堆中
            if i + 1 < j:
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))
        
        # 第 k 个最小的分数
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(k \log n)$，其中 $n$ 是数组 $arr$ 的长度。初始化堆需要 $O(n \log n)$，取出 $k$ 个元素需要 $O(k \log n)$。
- **空间复杂度**：$O(n)$。堆中最多存储 $n$ 个元素。
