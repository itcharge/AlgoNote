# [1487. 保证文件名唯一](https://leetcode.cn/problems/making-file-names-unique/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [1487. 保证文件名唯一 - 力扣](https://leetcode.cn/problems/making-file-names-unique/)

## 题目大意

**描述**：给定一个字符串数组 $names$，表示文件名列表。如果文件名重复，需要在后面加上 `(k)` 后缀（$k$ 为最小正整数），确保文件名唯一。

**要求**：返回重命名后的文件名列表。

**说明**：
- $1 \le names.length \le 5 \times 10^4$。
- 文件名只含小写字母、数字和 `.`。

**示例**：

- 示例 1：

```python
输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：文件系统将会这样创建文件名：
"pes" --> 之前未分配，仍为 "pes"
"fifa" --> 之前未分配，仍为 "fifa"
"gta" --> 之前未分配，仍为 "gta"
"pes(2019)" --> 之前未分配，仍为 "pes(2019)"
```

- 示例 2：

```python
输入：names = ["gta","gta(1)","gta","avalon"]
输出：["gta","gta(1)","gta(2)","avalon"]
解释：文件系统将会这样创建文件名：
"gta" --> 之前未分配，仍为 "gta"
"gta(1)" --> 之前未分配，仍为 "gta(1)"
"gta" --> 文件名被占用，系统为该名称添加后缀 (k)，由于 "gta(1)" 也被占用，所以 k = 2 。实际创建的文件名为 "gta(2)" 。
"avalon" --> 之前未分配，仍为 "avalon"
```

## 解题思路

### 思路 1：哈希表记录次数

#### 1. 核心思想

用哈希表 $count$ 记录每个「原始文件根」已被使用的次数。当遇到一个文件名时：
- 如果没出现过，直接使用，并将对应计数设为 $1$。
- 如果出现过，尝试 `name + (k)` 直到 $k$ 最小且不冲突。

优化：记录每个文件根当前尝试的 $k$ 值，避免从 $1$ 开始重复尝试。

#### 2. 具体步骤

**第 1 步**：初始化 $name\_to\_index$ 字典（记录每个文件名已用的最小 $k$ 值）。

**第 2 步**：遍历 $names$：
- 如果 $name$ 不在字典中：
  - 直接加入结果，字典 $name \to 1$。
- 否则：
  - 从 $name\_to\_index[name]$ 开始尝试 $k$。
  - 找到最小的 $k$ 使得 $name + (k)$ 不在字典中。
  - 加入结果，更新字典。

**第 3 步**：返回结果列表。

#### 3. 举例说明

以 $names = ["pes","fifa","gta","pes(2019)"]$ 为例：

- `"pes"` 没出现过 → 使用，$count["pes"]=1$
- `"fifa"` 没出现过 → 使用
- `"gta"` 没出现过 → 使用
- `"pes(2019)"` 没出现过 → 使用

结果：`["pes","fifa","gta","pes(2019)"]`。

再以 $names = ["gta","gta(1)","gta","avalon"]$ 为例：

- `"gta"` → 使用
- `"gta(1)"` → 使用
- `"gta"` → 已存在，尝试 `"gta(1)"` 也已被占，尝试 `"gta(2)"` → 可用
- `"avalon"` → 使用

结果：`["gta","gta(1)","gta(2)","avalon"]`。

### 思路 1：代码

```python
class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}  # name -> 下一个要尝试的 k 值
        ans = []

        for name in names:
            if name not in used:
                ans.append(name)
                used[name] = 1
            else:
                k = used[name]
                new_name = f"{name}({k})"
                while new_name in used:
                    k += 1
                    new_name = f"{name}({k})"
                ans.append(new_name)
                used[name] = k + 1  # 下次从 k+1 开始尝试
                used[new_name] = 1  # 新文件名也被占用

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：均摊 $O(n)$，每个文件名最多产生少量尝试。
- **空间复杂度**：$O(n)$。
