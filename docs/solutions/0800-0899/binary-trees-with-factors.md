# [0823. 带因子的二叉树](https://leetcode.cn/problems/binary-trees-with-factors/)

- 标签：数组、哈希表、动态规划、排序
- 难度：中等

## 题目链接

- [0823. 带因子的二叉树 - 力扣](https://leetcode.cn/problems/binary-trees-with-factors/)

## 题目大意

**描述**：

给出一个含有不重复整数元素的数组 $arr$ ，每个整数 $arr[i]$ 均大于 1。

用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。

**要求**：

计算出满足条件的二叉树的数量。答案可能很大，返回 对 $10^9 + 7$ 取余的结果。

**说明**：

- $1 \le arr.length \le 10^{3}$。
- $2 \le arr[i] \le 10^{9}$。
- $arr$ 中的所有值互不相同。

**示例**：

- 示例 1：

```python
输入: arr = [2, 4]
输出: 3
解释: 可以得到这些二叉树: [2], [4], [4, 2, 2]
```

- 示例 2：

```python
输入: arr = [2, 4, 5, 10]
输出: 7
解释: 可以得到这些二叉树: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
```

## 解题思路

### 思路 1：动态规划 + 哈希表

这道题要求计算用数组中的元素构建二叉树的方案数，其中每个非叶节点的值等于其两个子节点值的乘积。

关键观察：

- 对于一个值 $arr[i]$，如果它是非叶节点，那么它的两个子节点值 $left$ 和 $right$ 必须满足 $left \times right = arr[i]$，且 $left$ 和 $right$ 都在数组中。
- 使用动态规划：$dp[x]$ 表示以 $x$ 为根节点的二叉树的方案数。

算法步骤：

1. 将数组排序，方便从小到大处理。
2. 使用哈希表 $dp$，$dp[x]$ 表示以 $x$ 为根节点的二叉树方案数。
3. 初始化：每个元素本身可以作为叶节点，$dp[x] = 1$。
4. 对于每个元素 $x$，枚举所有可能的因子对 $(left, right)$：
   - 如果 $left$ 和 $right$ 都在数组中，则 $dp[x] += dp[left] \times dp[right]$。
5. 返回所有 $dp[x]$ 的和。

### 思路 1：代码

```python
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        # 排序，从小到大处理
        arr.sort()
        
        # dp[x] 表示以 x 为根节点的二叉树方案数
        dp = {}
        
        # 将数组元素存入集合，方便查找
        arr_set = set(arr)
        
        for x in arr:
            # 初始化：x 本身可以作为叶节点
            dp[x] = 1
            
            # 枚举所有可能的左子节点
            for left in arr:
                # 如果 left > sqrt(x)，后面的 left 更大，right 会更小，会重复计算
                if left * left > x:
                    break
                
                # 检查是否能整除
                if x % left == 0:
                    right = x // left
                    
                    # 如果 right 在数组中
                    if right in arr_set:
                        if left == right:
                            # 左右子树相同
                            dp[x] = (dp[x] + dp[left] * dp[right]) % MOD
                        else:
                            # 左右子树不同，有两种组合方式
                            dp[x] = (dp[x] + 2 * dp[left] * dp[right]) % MOD
        
        # 返回所有方案数的和
        return sum(dp.values()) % MOD
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$，其中 $n$ 是数组的长度。需要对每个元素枚举所有可能的因子。
- **空间复杂度**：$O(n)$，需要使用哈希表存储 DP 状态。
