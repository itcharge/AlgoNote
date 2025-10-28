# [0458. 可怜的小猪](https://leetcode.cn/problems/poor-pigs/)

- 标签：数学、动态规划、组合数学
- 难度：困难

## 题目链接

- [0458. 可怜的小猪 - 力扣](https://leetcode.cn/problems/poor-pigs/)

## 题目大意

**描述**：

有 $buckets$ 桶液体，其中「正好有一桶」含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 $minutesToTest$ 分钟时间来确定哪桶液体是有毒的。

喂猪的规则如下：

1. 选择若干活猪进行喂养。
2. 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
3. 小猪喝完水后，必须有 $minutesToDie$ 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
4. 过了 $minutesToDie$ 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
5. 重复这一过程，直到时间用完。

给定桶的数目 $buckets$，$minutesToDie$ 和 $minutesToTest$。

**要求**：

返回在规定时间内判断哪个桶有毒所需的「最小」猪数。

**说明**：

- $1 \le buckets \le 10^{3}$。
- $1 \le minutesToDie \le minutesToTest \le 10^{3}$。

**示例**：

- 示例 1：

```python
输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
输出：5
```

- 示例 2：

```python
输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
输出：2
```

## 解题思路

### 思路 1：数学

这是一道经典的数学和信息论问题。

假设有 $x$ 只小猪，每只小猪可以进行 $rounds = \lfloor \frac{minutesToTest}{minutesToDie} \rfloor + 1$ 轮测试（第一轮 + 冷却后继续测试）。

每只小猪有 $rounds + 1$ 种状态：
- 第 0 轮死亡（喝了第 0 次被毒死）。
- 第 1 轮死亡（喝了第 1 次被毒死）。
- ...
- 第 $rounds - 1$ 轮死亡。
- 存活到最后（没有中毒）。

$x$ 只小猪的状态组合总数为 $rounds^x$，每一种状态组合可以对应一个桶。

因此问题转化为：需要找到最小的 $x$，使得 $rounds^x \ge buckets$。

对不等式两边取对数：$x \times \log(rounds) \ge \log(buckets)$。

解得：$x \ge \frac{\log(buckets)}{\log(rounds)}$。

因此最小的 $x$ 为 $\lceil \frac{\log(buckets)}{\log(rounds)} \rceil$。

具体步骤：

- 计算 $rounds = \lfloor \frac{minutesToTest}{minutesToDie} \rfloor + 1$（即每只小猪可能的死亡状态数）。
- 如果 $rounds = 1$，说明无法进行有效测试，需要小猪数等于桶数。
- 否则计算 $\frac{\log(buckets)}{\log(rounds)}$。
- 由于浮点数精度问题，如果结果接近整数，直接返回该整数，否则向上取整。

### 思路 1：代码

```python
import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # rounds 表示每只小猪可能的死亡状态数
        rounds = minutesToTest // minutesToDie + 1
        
        # 特殊情况：如果只有 1 个状态（即无法测试），需要小猪数等于桶数
        if rounds == 1:
            return buckets
        
        # 使用换底公式：log_rounds(buckets) = log(buckets) / log(rounds)
        # 添加小的 epsilon 避免浮点数精度问题
        result = math.log(buckets) / math.log(rounds)
        
        # 如果 result 是整数（考虑浮点误差），直接返回，否则向上取整
        if abs(result - round(result)) < 1e-10:
            return round(result)
        else:
            return math.ceil(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。只进行常数次计算。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
