# [1363. 形成三的最大倍数](https://leetcode.cn/problems/largest-multiple-of-three/)

- 标签：贪心、数组、动态规划
- 难度：困难

## 题目链接

- [1363. 形成三的最大倍数 - 力扣](https://leetcode.cn/problems/largest-multiple-of-three/)

## 题目大意

**描述**：给定一个整数数组 $digits$（$0$-$9$）。可以用其中的任意个数字组成一个整数（每个数字最多用一次）。

**要求**：返回能组成的最大整数，且是 $3$ 的倍数。如果没有，返回空字符串。

**示例**：

- 示例 1：

```python
输入：digits = [8,1,9]
输出："981"
```

- 示例 2：

```python
输入：digits = [8,6,7,1,0]
输出："8760"
```


## 解题思路

### 思路 1：贪心 + 余数分类

#### 1. 核心思想

一个数能被 $3$ 整除等价于各位数字之和能被 $3$ 整除。

先计算总和 $total$ 和余数 $remainder = total \% 3$。
- 如果 $remainder == 0$：全部数字可用。
- 如果 $remainder == 1$：删除一个余 $1$ 的数字，或删除两个余 $2$ 的数字。
- 如果 $remainder == 2$：删除一个余 $2$ 的数字，或删除两个余 $1$ 的数字。

删除时尽量删最小的数字，以得到最大结果。

#### 2. 具体步骤

**第 1 步**：统计所有数字的出现次数。分类按余数分组。

**第 2 步**：根据余数决定要删除哪些数字。

**第 3 步**：从 $9$ 到 $0$ 构建结果字符串（注意前导 $0$ 的处理）。

### 思路 1：代码

```python
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = [0] * 10
        total = 0
        for d in digits:
            cnt[d] += 1
            total += d

        def delete(num):
            """尝试删除一个数字 num"""
            if cnt[num] > 0:
                cnt[num] -= 1
                return True
            return False

        remainder = total % 3
        if remainder == 1:
            if not (delete(1) or delete(4) or delete(7)):
                delete(2) and delete(2) or delete(5) and delete(5) or delete(8) and delete(8)
                # 更严谨的写法：删除两个余 2 的最小数字
        elif remainder == 2:
            if not (delete(2) or delete(5) or delete(8)):
                delete(1) and delete(1) or delete(4) and delete(4) or delete(7) and delete(7)

        ans = ''.join(str(d) * cnt[d] for d in range(9, -1, -1))
        if ans and ans[0] == '0':
            return '0'
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(10)$。
