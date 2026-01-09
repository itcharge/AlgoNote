# [0954. 二倍数对数组](https://leetcode.cn/problems/array-of-doubled-pairs/)

- 标签：贪心、数组、哈希表、排序
- 难度：中等

## 题目链接

- [0954. 二倍数对数组 - 力扣](https://leetcode.cn/problems/array-of-doubled-pairs/)

## 题目大意

**描述**：

给定一个长度为偶数的整数数组 $arr$。

**要求**：

只有对 $arr$ 进行重组后可以满足「对于每个 $0 \le i < len(arr) / 2$，都有 $arr[2 \times i + 1] = 2 \times arr[2 \times i]$」时，返回 true；否则，返回 false。

**说明**：

- $0 \le arr.length \le 3 \times 10^{4}$。
- $arr.length$ 是偶数。
- $-10^{5} \le arr[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：arr = [3,1,3,6]
输出：false
```

- 示例 2：

```python
输入：arr = [2,1,2,6]
输出：false
```

## 解题思路

### 思路 1：贪心 + 哈希表

#### 思路

这道题要求判断数组能否重组为二倍数对的形式，即 $arr[2 \times i + 1] = 2 \times arr[2 \times i]$。

我们可以使用贪心策略：

1. **统计频次**：使用哈希表统计每个数字出现的次数。
2. **排序**：按绝对值从小到大排序。这样可以保证先处理较小的数，避免遗漏。
3. **贪心匹配**：对于每个数 $x$，如果它还有剩余次数，就尝试找它的二倍 $2x$：
   - 如果 $2x$ 的次数不足，返回 `False`。
   - 否则，将 $x$ 和 $2x$ 的次数都减 $1$。
4. 如果所有数都能成功匹配，返回 `True`。

**注意**：需要按绝对值排序，因为负数的二倍关系是 $-4$ 和 $-2$，而不是 $-2$ 和 $-4$。

#### 代码

```python
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter
        
        # 统计每个数字的出现次数
        count = Counter(arr)
        
        # 按绝对值从小到大排序
        for x in sorted(count, key=abs):
            # 如果 x 还有剩余次数
            if count[x] > 0:
                # 检查 2x 的次数是否足够
                if count[2 * x] < count[x]:
                    return False
                # 匹配 x 和 2x
                count[2 * x] -= count[x]
        
        return True
```

#### 复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是数组长度。主要时间消耗在排序上。
- **空间复杂度**：$O(n)$，需要哈希表存储每个数字的频次。
