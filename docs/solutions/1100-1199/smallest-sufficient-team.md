# [1125. 最小的必要团队](https://leetcode.cn/problems/smallest-sufficient-team/)

- 标签：位运算、数组、动态规划、状态压缩
- 难度：困难

## 题目链接

- [1125. 最小的必要团队 - 力扣](https://leetcode.cn/problems/smallest-sufficient-team/)

## 题目大意

**描述**：作为项目经理，你有一份需求技能清单 $req\_skills$，还有一份候选人员名单 $people$，$people[i]$ 表示第 $i$ 个人掌握的技能列表。你需要选出一些人组成一个团队，使得需求技能清单上的每个技能都至少有一个人掌握。

**要求**：返回任意一个规模最小的必要团队（用人员编号表示）。

**说明**：

- $1 \le req\_skills.length \le 16$（技能最多 16 个）。
- $1 \le people.length \le 60$。
- 题目保证答案存在。

**示例**：

```python
输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
输出：[0,2]
解释：人员 0 会 java，人员 2 会 nodejs 和 reactjs，正好覆盖所有技能，且只有 2 个人。
```

## 解题思路

### 思路 1：状态压缩动态规划

**拆解步骤**：

1. **技能编号**：把每个技能映射到一个从 $0$ 开始的编号。

2. **每个人的技能转成二进制**：对每个人，把他会的技能对应的二进制位设为 $1$，得到一个整数。

3. **动态规划**：
   - 定义 $dp[mask]$：达到技能状态 $mask$ 所需的最小团队（人员列表）。
   - 初始状态 $dp[0] = []$：没有任何技能时不需要人。
   - 目标状态 $dp[target]$，其中 $target = 2^n - 1$（所有技能都掌握）。

4. **遍历每个人**，对当前已有的每个状态：
   - 计算加入这个人后的新状态 $new\_mask = mask \mid skill\_mask$
   - 如果新状态还没人达到过，或者新方案人数更少，就更新 $dp[new\_mask]$

5. **返回 $dp[target]$**。

### 思路 1：代码

```python
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        # 给每个技能分配一个编号（二进制位）
        skill_to_idx = {skill: i for i, skill in enumerate(req_skills)}

        # 把每个人的技能列表转成二进制状态
        people_skills = []
        for person in people:
            mask = 0
            for skill in person:
                mask |= 1 << skill_to_idx[skill]
            people_skills.append(mask)

        target = (1 << n) - 1  # 所有技能都掌握的目标状态
        # dp[mask] = 达到 mask 状态的最小团队
        dp = {0: []}

        for i, skill_mask in enumerate(people_skills):
            # 对当前已有的每个状态，尝试加入这个人
            for curr_mask in list(dp.keys()):
                new_mask = curr_mask | skill_mask
                # 如果新状态还没达到过，或者新团队更小
                if new_mask not in dp or len(dp[new_mask]) > len(dp[curr_mask]) + 1:
                    dp[new_mask] = dp[curr_mask] + [i]

        return dp[target]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times 2^n)$。用人话说就是：有 $m$ 个人，最多 $2^n$ 种技能状态，每个人都要过一遍所有状态。因为 $n \le 16$，$2^{16} = 65536$，在可接受范围内。
- **空间复杂度**：$O(2^n \times n)$。需要存储每个状态对应的团队列表。
