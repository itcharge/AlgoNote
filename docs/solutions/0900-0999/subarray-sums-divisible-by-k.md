# [974. 和可被 K 整除的子数组](https://leetcode.cn/problems/subarray-sums-divisible-by-k/)

- 标签：数组、哈希表、前缀和
- 难度：中等

## 题目链接

- [974. 和可被 K 整除的子数组 - 力扣](https://leetcode.cn/problems/subarray-sums-divisible-by-k/)

## 题目大意

给定一个整数数组 `nums` 和一个整数 `k`。

要求：返回其中元素之和可被 `k` 整除的（连续、非空）子数组的数目。

## 解题思路

先考虑暴力计算子数组和，外层两重循环，遍历所有连续子数组，然后最内层再计算一下子数组的和。部分代码如下：

```python
for i in range(len(nums)):
    for j in range(i + 1):
        sum = countSum(i, j)
```

这样下来时间复杂度就是 $O(n^3)$ 了。下一步是想办法降低时间复杂度。

先用一重循环遍历数组，计算出数组 `nums` 中前 i 个元素的和（前缀和），保存到一维数组 `pre_sum` 中，那么对于任意 `[j..i]` 的子数组 的和为 `pre_sum[i] - pre_sum[j - 1]`。这样计算子数组和的时间复杂度降为了 $O(1)$。总体时间复杂度为 $O(n^2)$。

由于我们只关心和为 `k` 出现的次数，不关心具体的解，可以使用哈希表来加速运算。

`pre_sum[i]` 的定义是前 `i` 个元素和，则 `[j..i]` 子数组和可以被 `k` 整除可以转换为：`（pre_sum[i] - pre_sum[j - 1]）% k == 0`。再转换一下：`pre_sum[i] % k == pre_sum[j - 1] % k`。

所以，我们只需要统计满足 `pre_sum[i] % k == pre_sum[j - 1] % k` 条件的组合个数。具体做法如下：

使用 `pre_sum` 变量记录前缀和（代表 `pre_sum[i]`）。使用哈希表 `pre_dic` 记录 `pre_sum[i] % k` 出现的次数。键值对为 `pre_sum[i] : count`。

- 从左到右遍历数组，计算当前前缀和并对 `k`  取余，即 `pre_sum = (pre_sum + nums[i]) % k`。
  - 如果 `pre_sum` 在哈希表中，则答案个数累加上 `pre_dic[pre_sum]`。同时 `pre_sum` 个数累加 1，即 `pre_dic[pre_sum] += 1`。
  - 如果 `pre_sum` 不在哈希表中，则 `pre_sum` 个数记为 1，即 `pre_dic[pre_sum] += 1`。
- 最后输出答案个数。

## 代码

```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        ans = 0
        nums_dict = {0: 1}
        for i in range(len(nums)):
            pre_sum = (pre_sum + nums[i]) % k
            if pre_sum < 0:
                pre_sum += k
            if pre_sum in nums_dict:
                ans += nums_dict[pre_sum]
                nums_dict[pre_sum] += 1
            else:
                nums_dict[pre_sum] = 1
        return ans
```

