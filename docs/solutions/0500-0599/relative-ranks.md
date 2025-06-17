# [0506. 相对名次](https://leetcode.cn/problems/relative-ranks/)

- 标签：数组、排序、堆（优先队列）
- 难度：简单

## 题目链接

- [0506. 相对名次 - 力扣](https://leetcode.cn/problems/relative-ranks/)

## 题目大意

**描述**：给定一个长度为 $n$ 的数组 $score$。其中 $score[i]$ 表示第 $i$ 名运动员在比赛中的成绩。所有成绩互不相同。

**要求**：找出他们的相对名次，并授予前三名对应的奖牌。前三名运动员将会被分别授予「金牌（`"Gold Medal"`）」，「银牌（`"Silver Medal"`）」和「铜牌（`"Bronze Medal"`）」。

**说明**：

- $n == score.length$。
- $1 \le n \le 10^4$。
- $0 \le score[i] \le 10^6$。
- $score$ 中的所有值互不相同。

**示例**：

- 示例 1：

```python
输入：score = [5,4,3,2,1]
输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"]
解释：名次为 [1st, 2nd, 3rd, 4th, 5th] 。
```

- 示例 2：

```python
输入：score = [10,3,8,9,4]
输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"]
解释：名次为 [1st, 5th, 3rd, 2nd, 4th] 。
```

## 解题思路

### 思路 1：排序

1. 先对数组 $score$ 进行排序。
2. 再将对应前三个位置上的元素替换成对应的字符串：`"Gold Medal"`, `"Silver Medal"`, `"Bronze Medal"`。

### 思路 1：代码

```python
class Solution:
    def shellSort(self, arr):
        size = len(arr)
        gap = size // 2

        while gap > 0:
            for i in range(gap, size):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap = gap // 2
        return arr

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        nums = score.copy()
        nums = self.shellSort(nums)
        score_map = dict()
        for i in range(len(nums)):
            score_map[nums[i]] = i + 1

        res = []
        for i in range(len(score)):
            if score[i] == nums[0]:
                res.append("Gold Medal")
            elif score[i] == nums[1]:
                res.append("Silver Medal")
            elif score[i] == nums[2]:
                res.append("Bronze Medal")
            else:
                res.append(str(score_map[score[i]]))
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。因为采用了时间复杂度为 $O(n \times \log n)$ 的希尔排序。
- **空间复杂度**：$O(n)$。
