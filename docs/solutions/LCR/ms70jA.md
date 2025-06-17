# [LCR 067. 数组中两个数的最大异或值](https://leetcode.cn/problems/ms70jA/)

- 标签：位运算、字典树、数组、哈希表
- 难度：中等

## 题目链接

- [LCR 067. 数组中两个数的最大异或值 - 力扣](https://leetcode.cn/problems/ms70jA/)

## 题目大意

给定一个整数数组 `nums`。

要求：返回 `num[i] XOR nums[j]` 的最大运算结果。其中 `0 ≤ i ≤ j < n`。

## 解题思路

最直接的想法暴力求解。两层循环计算两两之间的异或结果，记录并更新最大异或结果。

更好的做法可以减少一重循环。首先，要取得异或结果的最大值，那么从二进制的高位到低位，尽可能的让每一位异或结果都为 `1`。

将数组中所有数字的二进制形式从高位到低位依次存入字典树中。然后是利用异或运算交换律：如果 `a ^ b = max` 成立，那么 `a ^ max = b` 与 `b ^ max = a` 均成立。这样当我们知道 `a` 和 `max` 时，可以通过交换律求出 `b`。`a` 是我们遍历的每一个数，`max` 是我们想要尝试的最大值，从 `111111...` 开始，从高位到低位依次填 `1`。

对于 `a` 和 `max`，如果我们所求的 `b` 也在字典树中，则表示 `max` 是可以通过 `a` 和 `b` 得到的，那么 `max` 就是所求最大的异或。如果 `b` 不在字典树中，则减小 `max` 值继续判断，或者继续查询下一个 `a`。

## 代码

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isEnd = False


    def insert(self, num: int, max_bit: int) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for i in range(max_bit, -1, -1):
            bit = num >> i & 1
            if bit not in cur.children:
                cur.children[bit] = Trie()
            cur = cur.children[bit]
        cur.isEnd = True

    def search(self, num: int, max_bit: int) -> int:
        """
        Returns if the word is in the trie.
        """
        cur = self
        res = 0
        for i in range(max_bit, -1, -1):
            bit = num >> i & 1
            if 1 - bit not in cur.children:
                res = res * 2
                cur = cur.children[bit]
            else:
                res = res * 2 + 1
                cur = cur.children[1 - bit]
        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie_tree = Trie()
        max_bit = len(format(max(nums), 'b')) - 1
        ans = 0
        for num in nums:
            trie_tree.insert(num, max_bit)
            ans = max(ans, trie_tree.search(num, max_bit))
            
        return ans
```

