# [0768. 最多能完成排序的块 II](https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/)

- 标签：栈、贪心、数组、排序、单调栈
- 难度：困难

## 题目链接

- [0768. 最多能完成排序的块 II - 力扣](https://leetcode.cn/problems/max-chunks-to-make-sorted-ii/)

## 题目大意

**描述**：

给定一个整数数组 $arr$。将 $arr$ 分割成若干块，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

**要求**：

返回能将数组分成的最多块数。

**说明**：

- $1 \le arr.length \le 2000$。
- $0 \le arr[i] \le 10^{8}$。

**示例**：

- 示例 1：

```python
输入：arr = [5,4,3,2,1]
输出：1
解释：
将数组分成2块或者更多块，都无法得到所需的结果。 
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。
```

- 示例 2：

```python
输入：arr = [2,1,3,4,4]
输出：4
解释：
可以把它分成两块，例如 [2, 1], [3, 4, 4]。 
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。
```

## 解题思路

### 思路 1：单调栈

这道题要求将数组分成若干块，每块单独排序后连接起来，结果与整体排序相同。

**核心观察**：

- 如果可以在位置 $i$ 处分割，那么 $arr[0:i+1]$ 中的最大值必须 $\leq$ $arr[i+1:]$ 中的最小值。
- 等价于：前 $i+1$ 个元素排序后，应该恰好是整体排序后的前 $i+1$ 个元素。

**解题步骤**：

1. 从左到右遍历数组，维护当前的最大值 $max\_left$。
2. 同时预处理从右到左的最小值数组 $min\_right$。
3. 如果在位置 $i$ 处，$max\_left \leq min\_right[i+1]$，说明可以在此处分割。
4. 统计所有可以分割的位置数量。

**优化**：可以使用单调栈来解决，但对于这道题，简单的贪心方法更直观。

### 思路 1：代码

```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        
        # 预处理从右到左的最小值
        min_right = [0] * (n + 1)
        min_right[n] = float('inf')
        for i in range(n - 1, -1, -1):
            min_right[i] = min(arr[i], min_right[i + 1])
        
        chunks = 0
        max_left = 0
        
        # 从左到右遍历
        for i in range(n):
            max_left = max(max_left, arr[i])
            # 如果当前最大值 <= 右侧最小值，可以分割
            if max_left <= min_right[i + 1]:
                chunks += 1
        
        return chunks
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $arr$ 的长度。需要遍历数组两次。
- **空间复杂度**：$O(n)$。需要存储 $min\_right$ 数组。
