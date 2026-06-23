# [1452. 收藏清单](https://leetcode.cn/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [1452. 收藏清单 - 力扣](https://leetcode.cn/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

## 题目大意

**描述**：给定一个数组 $favoriteCompanies$，其中 $favoriteCompanies[i]$ 是第 $i$ 个人的收藏公司列表。

**要求**：返回人们索引列表（升序），这些人没有被其他人的列表完全包含（即 $favoriteCompanies[i]$ 不是 $favoriteCompanies[j]$ 的子集，对于所有 $j \ne i$）。

**说明**：
- $1 \le favoriteCompanies.length \le 100$。
- $1 \le favoriteCompanies[i].length \le 500$。

**示例**：

- 示例 1：

```python
输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
```

- 示例 2：

```python
输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1] 
解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。
```

## 解题思路

### 思路 1：集合运算

#### 1. 核心思想

将每个人的列表转为集合。对每个人 $i$，检查是否存在另一个人 $j$（$j \ne i$）使得 $set_i$ 是 $set_j$ 的子集。

如果 $i$ 不是任何人的子集，则 $i$ 加入答案。

#### 2. 具体步骤

**第 1 步**：将所有列表转为集合。

**第 2 步**：遍历 $i = 0 \to n-1$：
- 遍历 $j = 0 \to n-1$，$j \ne i$：
  - 如果 $set_i$ 是 $set_j$ 的子集且 $|set_i| \le |set_j|$（长度剪枝），标记 $i$ 被包含。
- 如果不被包含，加入答案。

**第 3 步**：返回答案列表。

#### 3. 举例说明

以 $favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]$ 为例：

- 第 0 人：$[leetcode,google,facebook]$ → 是其他人的子集？不是 → 保留
- 第 1 人：$[google,microsoft]$ → 不是任何人的子集 → 保留
- 第 2 人：$[google,facebook]$ → 是第 0 人的子集 → 排除
- 第 3 人：$[google]$ → 是第 0/1/2 人的子集 → 排除
- 第 4 人：$[amazon]$ → 不是任何人的子集 → 保留

结果：$[0, 1, 4]$。

### 思路 1：代码

```python
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        sets = [set(lst) for lst in favoriteCompanies]
        ans = []

        for i in range(n):
            is_subset = False
            for j in range(n):
                if i == j or len(sets[i]) > len(sets[j]):
                    continue
                if sets[i].issubset(sets[j]):
                    is_subset = True
                    break
            if not is_subset:
                ans.append(i)

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \times m)$，$n \le 100$，可行。
- **空间复杂度**：$O(n \times m)$，存储集合。
