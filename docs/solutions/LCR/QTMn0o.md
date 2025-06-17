# [LCR 010. 和为 K 的子数组](https://leetcode.cn/problems/QTMn0o/)

- 标签：数组、哈希表、前缀和
- 难度：中等

## 题目链接

- [LCR 010. 和为 K 的子数组 - 力扣](https://leetcode.cn/problems/QTMn0o/)

## 题目大意

给定一个整数数组 `nums` 和一个整数 `k`。

要求：找到该数组中和为 `k` 的连续子数组的个数。

## 解题思路

看到题目的第一想法是通过滑动窗口求解。但是做下来发现有些数据样例无法通过。发现这道题目中的整数不能保证都为正数，则无法通过滑动窗口进行求解。

先考虑暴力做法，外层两重循环，遍历所有连续子数组，然后最内层再计算一下子数组的和。部分代码如下：

```python
for i in range(len(nums)):
    for j in range(i + 1):
        sum = countSum(i, j)
```

这样下来时间复杂度就是 $O(n^3)$ 了。下一步是想办法降低时间复杂度。

先用一重循环遍历数组，计算出数组 `nums` 中前 i 个元素的和（前缀和），保存到一维数组 `pre_sum` 中，那么对于任意 `[j..i]` 的子数组 的和为 `pre_sum[i] - pre_sum[j - 1]`。这样计算子数组和的时间复杂度降为了 $O(1)$。总体时间复杂度为 $O(n^3)$。

但是还是超时了。。

由于我们只关心和为 `k` 出现的次数，不关心具体的解，可以使用哈希表来加速运算。

`pre_sum[i]` 的定义是前 `i` 个元素和，则 `pre_sum[i]` 可以由 `pre_sum[i - 1]` 递推而来，即：`pre_sum[i] = pre_sum[i - 1] + sum[i]`。 `[j..i]` 子数组和为 `k` 可以转换为：`pre_sum[i] - pre_sum[j - 1] == k`。

综合一下，可得：`pre_sum[j - 1] == pre_sum[i] - k `。

所以，当我们考虑以 `i` 结尾和为 `k` 的连续子数组个数时，只需要统计有多少个前缀和为 `pre_sum[i] - k` （即 `pre_sum[j - 1]`）的个数即可。具体做法如下：

- 使用 `pre_sum` 变量记录前缀和（代表 `pre_sum[i]`）。
- 使用哈希表 `pre_dic` 记录 `pre_sum[i]` 出现的次数。键值对为 `pre_sum[i] : pre_sum_count`。
- 从左到右遍历数组，计算当前前缀和 `pre_sum`。
- 如果 `pre_sum - k` 在哈希表中，则答案个数累加上 `pre_dic[pre_sum - k]`。
- 如果 `pre_sum` 在哈希表中，则前缀和个数累加 1，即 `pre_dic[pre_sum] += 1`。
- 最后输出答案个数。

## 代码

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_dic = {0: 1}
        pre_sum = 0
        count = 0
        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_dic:
                count += pre_dic[pre_sum - k]
            if pre_sum in pre_dic:
                pre_dic[pre_sum] += 1
            else:
                pre_dic[pre_sum] = 1
        return count
```

