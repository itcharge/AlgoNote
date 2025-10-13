## 1. Boyer Moore 算法介绍

> **Boyer Moore 算法（BM 算法）**：由 Robert S. Boyer 和 J Strother Moore 于 1977 年提出，是一种高效的字符串搜索算法，实际应用中通常比 KMP 算法快 3~5 倍。
>
> - **BM 算法核心思想**：先对模式串 $p$ 预处理，生成辅助表。在匹配过程中，如果文本串 $T$ 某字符与模式串 $p$ 不匹配，通过启发式规则，直接跳过不可能匹配的位置，将模式串整体向后滑动多位。

BM 算法的关键在于两种启发式移动规则：**坏字符规则（Bad Character Rule）** 和 **好后缀规则（Good Suffix Rule）**。

这两种规则的计算只依赖于模式串 $p$，与文本串 $T$ 无关。预处理时分别生成对应的后移表，匹配时每次取两者中较大的后移位数进行滑动。

需要注意，BM 算法滑动模式串时仍是从左到右，但每次字符比较是从右到左（即从后缀开始）。

下面将详细介绍 BM 算法的两种启发式规则：「坏字符规则」和「好后缀规则」。

## 2. Boyer Moore 算法启发规则

### 2.1 坏字符规则

> **坏字符规则（Bad Character Rule）**：当文本串 $T$ 和模式串 $p$ 从右往左比较时，如果遇到第一个不匹配的字符（称为 **坏字符**），可以利用该字符快速决定模式串的滑动距离。

移动位数分两种情况：

- **情况 1：坏字符在模式串 $p$ 中出现过**
   - 将模式串中最后一次出现该坏字符的位置与文本串中的坏字符对齐。
   - **移动位数 = 坏字符在模式串的失配位置 - 坏字符在模式串中最后一次出现的位置**

![情况 1：坏字符出现在模式串 p 中](https://qcdn.itcharge.cn/images/20240511164026.png)

- **情况 2：坏字符未在模式串 $p$ 中出现**
   - 直接将模式串整体向右移动一位。
   - **移动位数 = 坏字符在模式串的失配位置 + 1**

![情况 2：坏字符没有出现在模式串 p 中](https://qcdn.itcharge.cn/images/20240511164048.png)

### 2.2 好后缀规则

> **好后缀规则（Good Suffix Rule）**：当从右往左比较时，遇到不匹配，已匹配的部分称为 **好后缀**。此时可以利用好后缀信息，让模式串整体向右跳跃移动，加快匹配。

好后缀规则分为三种情况：

- **情况 1：模式串中存在与好后缀相同的子串**
   - 直接将该子串与好后缀对齐（如果有多个，选最右侧的）。
   - **移动位数 = 好后缀最后一个字符在模式串中的位置 - 匹配子串最后一个字符的位置**

![情况 1：模式串中有子串匹配上好后缀](https://qcdn.itcharge.cn/images/20240511164101.png)

- **情况 2：模式串中没有子串匹配好后缀，但有前缀等于好后缀的后缀**
   - 找到最长的前缀与好后缀的后缀相等，将其对齐。
   - **移动位数 = 好后缀后缀最后一个字符在模式串中的位置 - 最长前缀最后一个字符的位置**

![情况 2：模式串中无子串匹配上好后缀， 但有最长前缀匹配好后缀的后缀](https://qcdn.itcharge.cn/images/20240511164112.png)

- **情况 3：既无子串匹配好后缀，也无前缀匹配**
   - 直接将模式串整体右移一整段。
   - **移动位数 = 模式串长度**

![情况 3：模式串中无子串匹配上好后缀，也找不到前缀匹配](https://qcdn.itcharge.cn/images/20240511164124.png)

## 3. Boyer Moore 算法匹配过程示例

下面我们以 J Strother Moore 教授的经典例子，详细演示 BM 算法的匹配流程，帮助大家更直观地理解 **「坏字符规则」** 和 **「好后缀规则」** 的实际应用。

::: tabs#Boyer-Moore

@tab <1>

假设文本串为 `"HERE IS A SIMPLE EXAMPLE"`，模式串为 `"EXAMPLE"`，如下图所示。

![Boyer Moore 算法步骤 1](https://qcdn.itcharge.cn/images/20220127164130.png)

@tab <2>

首先，将模式串与文本串的起始位置对齐，从模式串的末尾开始逐个字符向前比较。

![Boyer Moore 算法步骤 2](https://qcdn.itcharge.cn/images/20220127164140.png)

此时，`'S'` 与 `'E'` 不匹配。`'S'` 就是「坏字符（Bad Character）」，位于模式串的第 $6$ 位。由于 `'S'` 在模式串 `"EXAMPLE"` 中未出现（即最后一次出现的位置为 $-1$），根据坏字符规则，模式串可以直接向右移动 $6 - (-1) = 7$ 位，使得模式串的首字符与文本串中 `'S'` 的下一位对齐。

@tab <3>

将模式串向右移动 $7$ 位后，再次从模式串尾部开始比较，发现 `'P'` 与 `'E'` 不匹配，此时 `'P'` 是坏字符。

![Boyer Moore 算法步骤 3](https://qcdn.itcharge.cn/images/20220127164151.png)

此时，`'P'` 在模式串中的失配位置为第 $6$ 位，且在模式串中最后一次出现的位置为 $4$（下标从 $0$ 开始）。

@tab <4>

根据坏字符规则，模式串向右移动 $6 - 4 = 2$ 位，使文本串中的 `'P'` 与模式串中的 `'P'` 对齐。

![Boyer Moore 算法步骤 4](https://qcdn.itcharge.cn/images/20220127164202.png)

@tab <5>

继续从模式串尾部逐位比较。首先比较文本串的 `'E'` 和模式串的 `'E'`，二者匹配，此时 `"E"` 为好后缀，位于模式串的第 $6$ 位。

![Boyer Moore 算法步骤 5](https://qcdn.itcharge.cn/images/20220127164212.png)

@tab <6>

继续比较前一位，文本串的 `'L'` 与模式串的 `'L'` 匹配，此时 `"LE"` 为好后缀，位于模式串的第 $6$ 位。

![Boyer Moore 算法步骤 6](https://qcdn.itcharge.cn/images/20220127164222.png)

@tab <7>

继续比较前一位，文本串的 `'P'` 与模式串的 `'P'` 匹配，此时 `"PLE"` 为好后缀，位于模式串的第 $6$ 位。

![Boyer Moore 算法步骤 7](https://qcdn.itcharge.cn/images/20220127164232.png)

@tab <8>

继续比较前一位，文本串的 `'M'` 与模式串的 `'M'` 匹配，此时 `"MPLE"` 为好后缀，位于模式串的第 $6$ 位。

![Boyer Moore 算法步骤 8](https://qcdn.itcharge.cn/images/20220127164241.png)

@tab <9>

继续比较前一位，文本串的 `'I'` 与模式串的 `'A'` 不匹配。

![Boyer Moore 算法步骤 9-1](https://qcdn.itcharge.cn/images/20220127164251.png)

此时，如果仅用坏字符规则，模式串应向右移动 $2 - (-1) = 3$ 位。但根据好后缀规则，可以获得更优的移动距离。

对于好后缀 `"MPLE"`，其后缀 `"PLE"`、`"LE"`、`"E"` 中，只有 `"E"` 与模式串前缀 `"E"` 匹配，属于好后缀规则的第二种情况。好后缀 `"E"` 的最后一个字符在模式串中的位置为 $6$，最长前缀 `"E"` 的最后一个字符在位置 $0$，因此模式串可以直接向右移动 $6 - 0 = 6$ 位。

![Boyer Moore 算法步骤 9-2](https://qcdn.itcharge.cn/images/20220127164301.png)

@tab <10>

再次从模式串尾部开始逐位比较。

此时，`'P'` 与 `'E'` 不匹配，`'P'` 是坏字符。根据坏字符规则，模式串向右移动 $6 - 4 = 2$ 位。

![Boyer Moore 算法步骤 10](https://qcdn.itcharge.cn/images/20220127164312.png)

@tab <11>

继续从模式串尾部逐位比较，发现模式串全部匹配，搜索结束，返回模式串在文本串中的起始位置。

::: 

## 4. Boyer Moore 算法步骤

BM 算法的整体流程如下：

1. 计算文本串 $T$ 的长度 $n$ 和模式串 $p$ 的长度 $m$。
2. 对模式串 $p$ 进行预处理，分别生成坏字符表 $bc\_table$ 和好后缀规则后移位数表 $gs\_table$。
3. 将模式串 $p$ 的头部与文本串 $T$ 的当前位置 $i$ 对齐，初始 $i = 0$。每次从模式串的末尾（$j = m - 1$）开始向前逐位比较：
   - 如果 $T[i + j]$ 与 $p[j]$ 相等，则继续向前比较下一个字符。
      - 如果模式串所有字符均匹配，则返回当前匹配的起始位置 $i$。
   - 如果 $T[i + j]$ 与 $p[j]$ 不相等：
      - 分别根据坏字符表和好后缀表，计算坏字符移动距离 $bad\_move$ 和好后缀移动距离 $good\_move$。
      - 取两者的最大值作为本轮的实际移动距离，即 $i += \max(bad\_move,\, good\_move)$，然后继续下一轮匹配。
4. 如果模式串移动到文本串末尾仍未找到匹配，则返回 $-1$。

该流程充分利用了坏字符和好后缀两种规则，实现了高效的字符串匹配。

## 5. Boyer Moore 算法代码实现

BM 算法的匹配过程本身实现相对简单，真正的难点主要集中在预处理阶段，尤其是「坏字符位置表」和「好后缀规则后移位数表」的构建。其中，「好后缀规则后移位数表」的实现尤为复杂。接下来我们将分别详细讲解这两部分的实现方法。

### 5.1 生成坏字符位置表代码实现

坏字符位置表的构建非常直观，具体步骤如下：

- 创建一个哈希表 $bc\_table$，用于记录每个字符在模式串中最后一次出现的位置，即 $bc\_table[bad\_char]$ 表示坏字符 $bad\_char$ 在模式串中的最右下标。
- 遍历模式串 $p$，将每个字符 $p[i]$ 及其下标 $i$ 存入哈希表。如果某字符在模式串中多次出现，则后出现的下标会覆盖前面的值，确保记录的是最右侧的位置。

在 BM 算法匹配过程中，如果 $bad\_char$ 不在 $bc\_table$ 中，则视为其最右位置为 $-1$；如果存在，则直接取 $bc\_table[bad\_char]$。据此即可计算模式串本轮应向右移动的距离。

坏字符位置表的实现代码如下：

```python
# 生成坏字符位置表
# bc_table[bad_char] 表示坏字符 bad_char 在模式串中最后一次出现的位置
def generateBadCharTable(p: str):
    """
    构建坏字符位置表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为该字符在模式串中最后一次出现的下标
    """
    bc_table = dict()  # 初始化坏字符表

    # 遍历模式串，将每个字符及其下标记录到表中
    for i, ch in enumerate(p):
        bc_table[ch] = i  # 如果字符多次出现，保留最后一次出现的位置

    # 返回坏字符表
    return bc_table
```

### 5.2 生成好后缀规则后移位数表代码实现

为了生成好后缀规则的后移位数表，首先需要构建一个后缀数组 $suffix$。$suffix[i]$ 表示以 $i$ 结尾的子串（即 $p[0:i+1]$）与模式串后缀的最大匹配长度，即最大的 $k$ 使得 $p[i-k+1:i+1] == p[m-k:m]$。

下面是 $suffix$ 数组的构建代码：

```python
# 生成 suffix 数组
# suffix[i] 表示以 i 结尾的子串（p[0:i+1]）与模式串后缀的最大匹配长度
def generateSuffixArray(p: str):
    """
    构建 suffix 数组。
    输入:
        p: 模式串
    输出:
        suffix: 列表，suffix[i] 表示以 i 结尾的子串与模式串后缀的最大匹配长度
    """
    m = len(p)
    suffix = [0 for _ in range(m)]  # 初始化为 0，表示尚未匹配
    suffix[m - 1] = m               # 最后一个字符的后缀必然和自身完全匹配，长度为 m

    # 从倒数第二个字符开始向前遍历
    for i in range(m - 2, -1, -1):
        j = i                       # j 指向当前子串的起始位置
        # 比较 p[j] 与 p[m-1-(i-j)]，即从后缀和子串末尾同时向前比较
        while j >= 0 and p[j] == p[m - 1 - (i - j)]:
            j -= 1
        # 以 i 结尾的子串与模式串后缀的最大匹配长度为 i - j
        suffix[i] = i - j

    return suffix
```

有了 $suffix$ 数组后，我们可以基于它构建好后缀规则的后移位数表 $gs\_list$。该表用一个数组表示，其中 $gs\_list[j]$ 表示在模式串第 $j$ 位遇到坏字符时，根据好后缀规则可以向右移动的距离。

根据「2.2 好后缀规则」的分析，好后缀的移动分为三种情况：

- 情况 1：模式串中存在与好后缀完全相同的子串。
- 情况 2：模式串中不存在匹配好后缀的子串，但存在前缀与好后缀的后缀相等。
- 情况 3：既无匹配子串，也无匹配前缀。

实际上，情况 2 和情况 3 可以合并处理（情况 3 可视为最长前缀长度为 $0$ 的特殊情况）。当某个坏字符同时满足多种情况时，应优先选择移动距离最小的方案，以避免遗漏可能的匹配。例如，如果既有匹配子串又有匹配前缀，应优先采用匹配子串的移动方式。

具体构建 $gs\_list$ 的步骤如下：

- 首先，假设所有位置均为情况 3，即 $gs\_list[i] = m$。
- 然后，利用后缀和前缀的匹配关系，更新情况 2 下的移动距离：$gs\_list[j] = m - 1 - i$，其中 $j$ 是好后缀前的坏字符位置，$i$ 是最长前缀的末尾下标，$m - 1 - i$ 为可移动的距离。
- 最后，处理情况 1：对于好后缀的左端点（$m - 1 - suffix[i]$ 处）遇到坏字符时，更新其可移动距离为 $gs\_list[m - 1 - suffix[i]] = m - 1 - i$。

下面是生成好后缀规则后移位数表 $gs\_list$ 的代码：

```python
# 生成好后缀规则后移位数表
# gs_list[j] 表示在模式串下标 j 处遇到坏字符时，根据好后缀规则可以向右移动的距离
def generateGoodSuffixList(p: str):
    """
    构建好后缀规则的后移位数表 gs_list。
    输入:
        p: 模式串
    输出:
        gs_list: 列表，gs_list[j] 表示在 j 处遇到坏字符时可向右移动的距离
    """
    m = len(p)
    gs_list = [m for _ in range(m)]  # 情况3：默认全部初始化为 m，表示完全不匹配时的最大移动
    suffix = generateSuffixArray(p)  # 生成后缀数组

    # 处理情况 2：寻找最长的前缀与好后缀的后缀相等
    # j 表示好后缀前的坏字符位置
    j = 0
    # 从后往前遍历，i 表示前缀的结尾下标
    for i in range(m - 1, -1, -1):
        # 如果 suffix[i] == i + 1，说明 p[0: i+1] == p[m-1-i: m]，即前缀和后缀相等
        if suffix[i] == i + 1:
            # 对于所有 j < m-1-i 的位置，如果还未被更新，则设置为 m-1-i
            while j < m - 1 - i:
                if gs_list[j] == m:
                    gs_list[j] = m - 1 - i  # 更新移动距离
                j += 1

    # 处理情况 1：模式串中存在与好后缀完全相同的子串
    # i 表示好后缀的右端点
    for i in range(m - 1):
        # m-1-suffix[i] 是好后缀的左端点
        # m-1-i 是可移动的距离
        gs_list[m - 1 - suffix[i]] = m - 1 - i  # 更新在好后缀左端点遇到坏字符时的移动距离

    return gs_list
```

### 5.3 Boyer Moore 算法整体代码实现

```python
# Boyer-Moore 字符串匹配算法实现
def boyerMoore(T: str, p: str) -> int:
    """
    Boyer-Moore 算法主函数，返回模式串 p 在文本串 T 中首次出现的位置，如果无则返回 -1。
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0 if n == 0 else -1  # 约定空模式串匹配空文本串返回 0，否则 -1
    if n < m:
        return -1

    bc_table = generateBadCharTable(p)      # 生成坏字符表
    gs_list = generateGoodSuffixList(p)     # 生成好后缀表

    i = 0
    while i <= n - m:
        j = m - 1
        # 从模式串末尾向前比较
        while j >= 0 and T[i + j] == p[j]:
            j -= 1
        if j < 0:
            return i  # 匹配成功，返回起始下标
        # 坏字符规则：j - bc_table.get(T[i + j], -1)
        bad_move = j - bc_table.get(T[i + j], -1)
        # 好后缀规则：gs_list[j]
        good_move = gs_list[j]
        # 取两者最大值进行滑动
        i += max(bad_move, good_move)
    return -1

def generateBadCharTable(p: str):
    """
    生成坏字符表：记录每个字符在模式串中最后一次出现的位置。
    """
    bc_table = dict()
    for i, ch in enumerate(p):
        bc_table[ch] = i  # 只保留最后一次出现的位置
    return bc_table

def generateGoodSuffixList(p: str):
    """
    生成好后缀规则的后移位数表 gs_list。
    gs_list[j] 表示在模式串下标 j 处遇到坏字符时，根据好后缀规则可以向右移动的距离。
    """
    m = len(p)
    gs_list = [m for _ in range(m)]  # 默认全部为情况 3：最大移动 m
    suffix = generateSuffixArray(p)  # 生成后缀数组

    # 处理情况 2：寻找最长的前缀与好后缀的后缀相等
    j = 0
    for i in range(m - 1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if gs_list[j] == m:
                    gs_list[j] = m - 1 - i    # 更新移动距离
                j += 1

    # 处理情况 1：模式串中存在与好后缀完全相同的子串
    for i in range(m - 1):
        # m-1-suffix[i] 是好后缀的左端点
        gs_list[m - 1 - suffix[i]] = m - 1 - i

    return gs_list

def generateSuffixArray(p: str):
    """
    生成后缀数组 suffix。
    suffix[i] 表示以 i 结尾的子串与模式串后缀的最大匹配长度。
    """
    m = len(p)
    suffix = [m for _ in range(m)]  # 初始化为 0，表示尚未匹配
    suffix[m - 1] = m  # 最后一个字符的后缀长度为 m
    for i in range(m - 2, -1, -1):
        j = i
        # 从 i 向前与模式串后缀比较
        while j >= 0 and p[j] == p[m - 1 - i + j]:
            j -= 1
        suffix[i] = i - j
    return suffix

# 测试用例
print(boyerMoore("abbcfdddbddcaddebc", "aaaaa"))  # -1
print(boyerMoore("", ""))                         # 0
print(boyerMoore("HERE IS A SIMPLE EXAMPLE", "EXAMPLE"))  # 17
print(boyerMoore("abcabcabcabc", "abcabc"))       # 0
```

## 6. Boyer Moore 算法分析

| 指标         | 复杂度         | 说明                                                         |
| ------------ | -------------- | ------------------------------------------------------------ |
| 最好时间复杂度   | $O(n / m)$     | 每次匹配时，模式串 $p$ 中不存在与文本串 $T$ 中第一个匹配的字符，滑动距离最大，比较次数最少。|
| 最坏时间复杂度   | $O(m \times n)$| 文本串 $T$ 中有大量重复字符，且模式串 $p$ 由 $m-1$ 个相同字符和一个不同字符组成，导致每次只能滑动一位。|
| 平均时间复杂度   | 介于 $O(n / m)$ 与 $O(m \times n)$ 之间 | 实际应用中通常远优于最坏情况，接近最好情况。|
| 预处理时间复杂度 | $O(m + \sigma)$ | 生成坏字符表和好后缀表，$\sigma$ 为字符集大小。|
| 空间复杂度     | $O(m + \sigma)$ | 需存储坏字符表（$\sigma$）和好后缀表（$m$）。|

- 其中 $n$ 为文本串长度，$m$ 为模式串长度，$\sigma$ 为字符集大小。
- 当模式串 $p$ 是非周期性的，在最坏情况下，BM 算法最多需要进行 $3n$ 次字符比较操作。

## 7. 总结

Boyer-Moore（BM）算法通过「坏字符规则」和「好后缀规则」两种启发式策略，实现模式串的高效跳跃移动，是实际应用中性能最优的单模式串匹配算法之一。

- **优点**：
   - **实际性能优异**：在大多数实际应用中，BM 算法通常比 KMP 算法快 3~5 倍
   - **跳跃能力强**：通过坏字符和好后缀规则，能够跳过大量不可能匹配的位置
   - **从右到左比较**：充分利用模式串信息，减少不必要的字符比较
   - **启发式策略**：两种规则互补，最大化跳跃距离
- **缺点**：
   - **实现复杂**：特别是好后缀规则的预处理部分，理解和实现难度较高
   - **最坏情况退化**：在特定输入下可能退化到 $O(m \times n)$ 复杂度
   - **空间开销**：需要存储坏字符表和好后缀表，空间复杂度为 $O(m + \sigma)$
   - **预处理开销**：需要预先构建两个辅助表，不适合单次匹配场景

## 练习题目

- [0028. 找出字符串中第一个匹配项的下标](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/find-the-index-of-the-first-occurrence-in-a-string.md)
- [0459. 重复的子字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/repeated-substring-pattern.md)
- [0686. 重复叠加字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/repeated-string-match.md)
- [0796. 旋转字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/rotate-string.md)
- [1408. 数组中的字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1400-1499/string-matching-in-an-array.md)
- [2156. 查找给定哈希值的子串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2100-2199/find-substring-with-given-hash-value.md)

- [单模式串匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%A8%A1%E5%BC%8F%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】柔性字符串匹配 - 中科院计算所网络信息安全研究组 译
- 【文章】[不用找了，学习 BM 算法，这篇就够了（思路+详注代码）- BoCong-Deng 的博客](https://blog.csdn.net/DBC_121/article/details/105569440)
- 【文章】[字符串匹配的 Boyer-Moore 算法 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
- 【文章】[ bm 算法好后缀 java 实现 - 长笛小号的博客 - CSDN博客](https://blog.csdn.net/weixin_29217235/article/details/114488027)
- 【文章】[BM算法详解 - 简单爱_wxg - 博客园](https://www.cnblogs.com/wxgblogs/p/5701101.html)
- 【文章】[grep 之字符串搜索算法 Boyer-Moore 由浅入深 - Alexia(minmin) - 博客园](https://www.cnblogs.com/lanxuezaipiao/p/3452579.html)
- 【文章】[字符串匹配基础（中）- 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/71525)
- 【代码】[BM算法 附有解释 - 实现 strStr() - 力扣](https://leetcode.cn/problems/implement-strstr/solution/bmsuan-fa-fu-you-jie-shi-by-wen-198/)