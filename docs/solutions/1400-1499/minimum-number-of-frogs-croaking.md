# [1419. 数青蛙](https://leetcode.cn/problems/minimum-number-of-frogs-croaking/)

- 标签：字符串、计数
- 难度：中等

## 题目链接

- [1419. 数青蛙 - 力扣](https://leetcode.cn/problems/minimum-number-of-frogs-croaking/)

## 题目大意

**描述**：给定一个字符串 $croakOfFrogs$，它表示青蛙的叫声序列 `"croak"`（一只青蛙的完整叫声）。不同青蛙的叫声可能重叠。

**要求**：返回模拟所有青蛙叫声所需的最少青蛙数量。如果字符串不是有效的青蛙叫声序列，返回 $-1$。

**说明**：
- $1 \le croakOfFrogs.length \le 10^5$。

**示例**：

- 示例 1：

```python
输入：croakOfFrogs = "croakcroak"
输出：1 
解释：一只青蛙 “呱呱” 两次
```

- 示例 2：

```python
输入：croakOfFrogs = "crcoakroak"
输出：2 
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"
```

## 解题思路

### 思路 1：状态机计数

#### 1. 核心思想

每只青蛙发出 `"croak"`，顺序固定：`c → r → o → a → k`。可以用 5 个计数器跟踪处于每个阶段的青蛙数量。

遍历字符：
- `c`：新的青蛙开始叫，$count[c]++$。
- `r`：必须有青蛙在 `c` 阶段，即 $count[c] > 0$，$count[c]--, count[r]++$。
- `o`、`a`、`k` 同理。
- 当一只青蛙完成 `k`（完成一次叫声），它可以立即开始新的叫声（从 `c` 开始），因此 count 减少。

答案 = 在所有时刻 $count[c] + count[r] + count[o] + count[a] + count[k]$ 的最大值。

#### 2. 具体步骤

**第 1 步**：用数组 $cnt = [0,0,0,0,0]$ 对应 $c,r,o,a,k$ 的状态。

**第 2 步**：遍历字符：
- 如果是 `c`：$cnt[0]++$
- 如果是 `r`：$cnt[0]--, cnt[1]++$（检查 $cnt[0] > 0$）
- 如果是 `o`：$cnt[1]--, cnt[2]++$
- 如果是 `a`：$cnt[2]--, cnt[3]++$
- 如果是 `k`：$cnt[3]--, cnt[4]$ 不变（青蛙释放，可以重新开始）
- 更新 $ans = \max(ans, sum(cnt))$

**第 3 步**：遍历结束时，检查 $cnt[0..3]$ 是否都为 $0$。如果有残余，返回 $-1$。

#### 3. 举例说明

以 $croakOfFrogs = "croakcroak"$ 为例：

- `c`: cnt=[1,0,0,0,0], sum=1
- `r`: cnt=[0,1,0,0,0], sum=1
- `o`: cnt=[0,0,1,0,0], sum=1
- `a`: cnt=[0,0,0,1,0], sum=1
- `k`: cnt=[0,0,0,0,0], sum=0
- 重复第二次 `croak`...

最大 sum = 1，最少 $1$ 只青蛙。

以 $croakOfFrogs = "crcoakroak"$（重叠）：

- 第 1 只青蛙开始 `c`，第 2 只青蛙也开始 `c`
- 最大 sum = 2，最少 $2$ 只青蛙。

### 思路 1：代码

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # c, r, o, a, k
        cnt = [0] * 5
        ans = 0
        # 映射字符到索引
        idx_map = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}

        for ch in croakOfFrogs:
            idx = idx_map[ch]
            if ch == 'c':
                cnt[0] += 1
            else:
                if cnt[idx - 1] == 0:
                    return -1
                cnt[idx - 1] -= 1
                if ch != 'k':
                    cnt[idx] += 1
            ans = max(ans, sum(cnt))

        # 检查是否有未完成的叫声
        if any(cnt[i] != 0 for i in range(4)):
            return -1

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
