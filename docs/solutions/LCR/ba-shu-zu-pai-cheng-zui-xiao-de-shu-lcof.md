# [LCR 164. 破解闯关密码](https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

- 标签：贪心、字符串、排序
- 难度：中等

## 题目链接

- [LCR 164. 破解闯关密码 - 力扣](https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

## 题目大意

**描述**：给定一个非负整数数组 $nums$。

**要求**：将数组中的数字拼接起来排成一个数，打印能拼接出的所有数字中的最小的一个。

**说明**：

- $0 < nums.length \le 100$。
- 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
- 拼接起来的数字可能会有前导 $0$，最后结果不需要去掉前导 $0$。

**示例**：

- 示例 1：

```python
输入: [10,2]
输出: "102"
```

- 示例 2：

```python
输入：[3,30,34,5,9]
输出："3033459"
```

## 解题思路

### 思路 1：自定义排序

本质上是给数组进行排序。假设 $x$、$y$ 是数组 $nums$ 中的两个元素。则排序的判断规则如下所示：

- 如果拼接字符串 $x + y > y + x$，则 $x$ 大于 $y$，$y$ 应该排在 $x$ 前面，从而使拼接起来的数字尽可能的小。
- 反之，如果拼接字符串 $x + y < y + x$，则 $x$ 小于 $y$，$x$ 应该排在 $y$ 前面，从而使拼接起来的数字尽可能的小。

按照上述规则，对原数组进行排序。这里使用了 `functools.cmp_to_key` 自定义排序函数。

### 思路 1：自定义排序代码

```python
import functools

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        nums_s = list(map(str, nums))
        nums_s.sort(key=functools.cmp_to_key(cmp))
        return ''.join(nums_s)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。排序算法的时间复杂度为 $O(n \times \log n)$。
- **空间复杂度**：$O(1)$。

## 参考资料

- 【题解】[LCR 164. 破解闯关密码（自定义排序，清晰图解） - 把数组排成最小的数 - 力扣](https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/)
