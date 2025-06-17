# [0904. 水果成篮](https://leetcode.cn/problems/fruit-into-baskets/)

- 标签：数组、哈希表、滑动窗口
- 难度：中等

## 题目链接

- [0904. 水果成篮 - 力扣](https://leetcode.cn/problems/fruit-into-baskets/)

## 题目大意

给定一个数组 `fruits`。其中 `fruits[i]` 表示第 `i` 棵树会产生 `fruits[i]` 型水果。

你可以从你选择的任何树开始，然后重复执行以下步骤：

- 把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
- 移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
- 请注意，在选择一棵树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有 `2` 个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

要求：返回你能收集的水果树的最大总量。

## 解题思路

只有 `2` 个篮子，要求在连续子数组中装最多 `2` 种不同水果。可以理解为维护一个水果种类数为 `2` 的滑动数组，求窗口中最大的水果树数目。具体做法如下：

- 用滑动窗口 `window` 来维护不同种类水果树数目。`window` 为哈希表类型。`ans` 用来维护能收集的水果树的最大总量。设定两个指针：`left`、`right`，分别指向滑动窗口的左右边界，保证窗口中水果种类数不超过 `2` 种。
- 一开始，`left`、`right` 都指向 `0`。
- 将最右侧数组元素 `fruits[right]` 加入当前窗口 `window` 中，该水果树数目 +1。
- 如果该窗口中该水果树种类多于 `2` 种，即 `len(window) > 2`，则不断右移 `left`，缩小滑动窗口长度，并更新窗口中对应水果树的个数，直到 `len(window) <= 2`。
- 维护更新能收集的水果树的最大总量。然后右移 `right`，直到 `right >= len(fruits)` 结束。
- 输出能收集的水果树的最大总量。

## 代码

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = dict()
        window_size = 2
        ans = 0
        left, right = 0, 0
        while right < len(fruits):
            if fruits[right] in window:
                window[fruits[right]] += 1
            else:
                window[fruits[right]] = 1

            while len(window) > window_size:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
```

