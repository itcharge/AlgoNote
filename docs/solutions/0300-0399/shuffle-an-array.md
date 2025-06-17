# [0384. 打乱数组](https://leetcode.cn/problems/shuffle-an-array/)

- 标签：数组、数学、随机化
- 难度：中等

## 题目链接

- [0384. 打乱数组 - 力扣](https://leetcode.cn/problems/shuffle-an-array/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是等可能的。

实现 `Solution class`:

- `Solution(int[] nums)` 使用整数数组 $nums$ 初始化对象。
- `int[] reset()` 重设数组到它的初始状态并返回。
- `int[] shuffle()` 返回数组随机打乱后的结果。

**说明**：

- $1 \le nums.length \le 50$。
- $-10^6 \le nums[i] \le 10^6$。
- $nums$ 中的所有元素都是 唯一的。
- 最多可以调用 $10^4$ 次 `reset` 和 `shuffle`。

**示例**：

- 示例 1：

```python
输入：
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出：
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释：
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
```

## 解题思路

### 思路 1：洗牌算法

题目要求在打乱顺序后，数组的所有排列应该是等可能的。对于长度为 $n$ 的数组，我们可以把问题转换为：分别在 $n$ 个位置上，选择填入某个数的概率是相同。具体选择方法如下：

- 对于第 $0$ 个位置，我们从 $0 \sim n - 1$ 总共 $n$ 个数中随机选择一个数，将该数与第 $0$ 个位置上的数进行交换。则每个数被选到的概率为 $\frac{1}{n}$。
- 对于第 $1$ 个位置，我们从剩下 $n - 1$ 个数中随机选择一个数，将该数与第 $1$ 个位置上的数进行交换。则每个数被选到的概率为 $\frac{n - 1}{n} \times \frac{1}{n - 1} = \frac{1}{n}$ （第一次没选到并且第二次被选中）。
- 对于第 $2$ 个位置，我们从剩下 $n - 2$ 个数中随机选择一个数，将该数与第 $2$ 个位置上的数进行交换。则每个数被选到的概率为 $\frac{n - 1}{n} \times \frac{n - 2}{n - 1} \times \frac{1}{n - 2} = \frac{1}{n}$ （第一次没选到、第二次没选到，并且第三次被选中）。
- 依次类推，对于每个位置上，每个数被选中的概率都是 $\frac{1}{n}$。

### 思路 1：洗牌算法代码

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        self.shuffle_nums = self.nums.copy()
        for i in range(len(self.shuffle_nums)):
            swap_index = random.randrange(i, len(self.shuffle_nums))
            self.shuffle_nums[i], self.shuffle_nums[swap_index] = self.shuffle_nums[swap_index], self.shuffle_nums[i]
        return self.shuffle_nums
```

## 参考资料

- 【题解】[「Python/Java/JavaScript/Go」 洗牌算法 - 打乱数组 - 力扣](https://leetcode.cn/problems/shuffle-an-array/solution/pythonjavajavascriptgo-xi-pai-suan-fa-by-k7i2/)