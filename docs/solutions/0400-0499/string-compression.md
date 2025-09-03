# [0443. 压缩字符串](https://leetcode.cn/problems/string-compression/)

- 标签：双指针、字符串
- 难度：中等

## 题目链接

- [0443. 压缩字符串 - 力扣](https://leetcode.cn/problems/string-compression/)

## 题目大意

**描述**：给定一个字符数组 $chars$。请使用下述算法压缩：

从一个空字符串 $s$ 开始。对于 $chars$ 中的每组连续重复字符：

- 如果这一组长度为 $1$，则将字符追加到 $s$ 中。
- 如果这一组长度超过 $1$，则需要向 $s$ 追加字符，后跟这一组的长度。

压缩后得到的字符串 $s$ 不应该直接返回 ，需要转储到字符数组 $chars$ 中。需要注意的是，如果组长度为 $10$ 或 $10$ 以上，则在 $chars$ 数组中会被拆分为多个字符。

**要求**：在修改完输入数组后，返回该数组的新长度。

**说明**：

- $1 \le chars.length \le 2000$。
- $chars[i]$ 可以是小写英文字母、大写英文字母、数字或符号。
- 必须设计并实现一个只使用常量额外空间的算法来解决此问题。

**示例**：

- 示例 1：

```python
输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
```

- 示例 2：

```python
输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。
```

## 解题思路

### 思路 1：快慢指针

题目要求原地修改字符串数组。我们可以使用快慢指针来解决原地修改问题，具体解决方法如下：

- 定义两个快慢指针 $slow$，$fast$。其中 $slow$ 指向压缩后的当前字符位置，$fast$ 指向压缩前的当前字符位置。
- 记录下当前待压缩字符的起始位置 $fast\_start = start$，然后过滤掉连续相同的字符。
- 将待压缩字符的起始位置的字符存入压缩后的当前字符位置，即  $chars[slow] = chars[fast\_start]$，并向右移动压缩后的当前字符位置，即 $slow += 1$。
- 判断一下待压缩字符的数目是否大于 $1$：
  - 如果数量为 $1$，则不用记录该数量。
  - 如果数量大于 $1$（即 $fast - fast\_start > 0$），则我们需要将对应数量存入压缩后的当前字符位置。这时候还需要判断一下数量是否大于等于 $10$。
    - 如果数量大于等于 $10$，则需要先将数字从个位到高位转为字符，存入压缩后的当前字符位置（此时数字为反，比如原数字是 $321$，则此时存入后为 $123$）。因为数字为反，所以我们需要将对应位置上的子字符串进行反转。
    - 如果数量小于 $10$，则直接将数字存入压缩后的当前字符位置，无需取反。
- 判断完之后向右移动压缩前的当前字符位置 $fast$，然后继续压缩字符串，直到全部压缩完，则返回压缩后的当前字符位置 $slow$ 即为答案。

### 思路 1：代码

```python
class Solution:
    
    def compress(self, chars: List[str]) -> int:
        def reverse(left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        slow, fast = 0, 0
        while fast < len(chars):
            fast_start = fast
            while fast + 1 < len(chars) and chars[fast + 1] == chars[fast]:
                fast += 1
            
            chars[slow] = chars[fast_start]
            slow += 1

            if fast - fast_start > 0:
                cnt = fast - fast_start + 1
                slow_start = slow
                while cnt != 0:
                    chars[slow] = str(cnt % 10)
                    slow += 1
                    cnt = cnt // 10
                reverse(slow_start, slow - 1)
            
            fast += 1
        return slow
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串 $s$ 的长度。
- **空间复杂度**：$O(1)$。
