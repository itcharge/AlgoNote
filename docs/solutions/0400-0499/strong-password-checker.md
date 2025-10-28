# [0420. 强密码检验器](https://leetcode.cn/problems/strong-password-checker/)

- 标签：贪心、字符串、堆（优先队列）
- 难度：困难

## 题目链接

- [0420. 强密码检验器 - 力扣](https://leetcode.cn/problems/strong-password-checker/)

## 题目大意

**描述**：

满足以下条件的密码被认为是强密码：

- 由至少 $6$ 个，至多 $20$ 个字符组成。
- 包含至少「一个小写字母」，至少「一个大写字母」，和至少「一个数字」。
- 不包含连续三个重复字符 (比如 `"Baaabb0"` 是弱密码, 但是 `"Baaba0"` 是强密码)。

给定一个字符串 $password$。

**要求**：

返回 将 $password$ 修改到满足强密码条件需要的最少修改步数。如果 $password$ 已经是强密码，则返回 $0$。

在一步修改操作中，你可以：

- 插入一个字符到 $password$ ，
- 从 $password$ 中删除一个字符，或
- 用另一个字符来替换 $password$ 中的某个字符。

**说明**：

- $1 \le password.length \le 50$。
- $password$ 由字母、数字、点 `'.'` 或者感叹号 `'!'` 组成。

**示例**：

- 示例 1：

```python
输入：password = "a"
输出：5
```

- 示例 2：

```python
输入：password = "aA1"
输出：3
```

## 解题思路

### 思路 1：分类讨论 + 贪心策略

**核心思想**：根据密码长度 $n$ 的不同情况，采用不同的修改策略。

**算法步骤**：

1. **统计缺少的字符类型**：
   - 使用布尔变量 $has\_lower$、$has\_upper$、$has\_digit$ 记录是否存在小写字母、大写字母和数字
   - 计算缺少的类型数量 $missing\_types = 3 - (has\_lower + has\_upper + has\_digit)$

2. **统计连续字符问题**：
   - 使用 $replace\_count$ 记录需要替换的总次数（每 $len$ 长度的连续段需要 $len // 3$ 次替换）
   - 使用 $one\_mod$ 记录长度模 3 余数为 0 的段的个数（删除 1 个字符可以减少 1 次替换）
   - 使用 $two\_mod$ 记录长度模 3 余数为 1 的段的个数（删除 2 个字符可以减少 1 次替换）

3. **根据长度分类处理**：
   - **情况 1**：$n < 6$（长度过短）。
     - 需要插入 $6 - n$ 个字符。
     - 需要替换的连续字符数为 $replace\_count$。
     - 需要添加的字符类型数为 $missing\_types$。
     - 返回 $\max(6 - n, replace\_count, missing\_types)$（插入操作可以同时解决多个问题）。
   
   - **情况 2**：$6 \le n \le 20$（长度合理）。
     - 只需要替换字符即可满足条件。
     - 返回 $\max(replace\_count, missing\_types)$。
   
   - **情况 3**：$n > 20$（长度过长）。
     - 需要删除 $deletions = n - 20$ 个字符。
     - 贪心地利用删除操作减少替换次数：
       * 优先删除 $one\_mod$ 段的 1 个字符（每次可以减少 1 次替换）。
       * 其次删除 $two\_mod$ 段的 2 个字符（每次可以减少 1 次替换）。
       * 最后删除其他段每 3 个字符（每次可以减少 1 次替换）。
     - 返回 $deletions + \max(replace\_count, missing\_types)$。

**注意**：删除字符可以同时减少替换次数，贪心策略能最大程度减少总操作次数。

### 思路 1：代码

```python
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # 统计缺少的字符类型
        has_lower = False
        has_upper = False
        has_digit = False
        
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
        
        # 缺少的字符类型数
        missing_types = 3 - (has_lower + has_upper + has_digit)
        
        # 统计连续相同字符段的长度及需要替换的次数
        replace_count = 0  # 需要替换的总次数
        one_mod = 0  # length % 3 == 0 的段的个数（删除 1 个可以减少 1 次替换）
        two_mod = 0  # length % 3 == 1 的段的个数（删除 2 个可以减少 1 次替换）
        
        i = 0
        while i < n:
            # 找出连续相同字符的结束位置
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            # 只处理长度 >= 3 的连续段
            if length >= 3:
                replace_count += length // 3
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
            i = j
        
        # 根据长度分类处理
        if n < 6:
            # 长度过短：需要插入字符
            # 插入操作可以同时解决多个问题
            return max(6 - n, missing_types, replace_count)
        
        elif n <= 20:
            # 长度合理：只需要替换
            return max(replace_count, missing_types)
        
        else:
            # 长度过长：需要删除字符
            delete_count = n - 20
            
            # 贪心地用删除操作减少替换次数
            # 优先删除 length % 3 == 0 的段的 1 个字符（删除 1 个可以减少 1 次替换）
            replace_count -= min(delete_count, one_mod)
            delete_count -= min(delete_count, one_mod)
            
            # 其次删除 length % 3 == 1 的段的 2 个字符（删除 2 个可以减少 1 次替换）
            replace_count -= min(delete_count // 2, two_mod)
            delete_count -= min(delete_count, 2 * two_mod)
            
            # 最后删除其他段的 3 个字符（删除 3 个可以减少 1 次替换）
            replace_count -= delete_count // 3
            
            return (n - 20) + max(replace_count, missing_types)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是密码的长度。只需要遍历一次字符串进行统计，后续处理是常数时间。
- **空间复杂度**：$O(1)$。只使用了常数个额外变量。
