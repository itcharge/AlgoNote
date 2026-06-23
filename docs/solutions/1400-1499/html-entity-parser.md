# [1410. HTML 实体解析器](https://leetcode.cn/problems/html-entity-parser/)

- 标签：哈希表、字符串
- 难度：中等

## 题目链接

- [1410. HTML 实体解析器 - 力扣](https://leetcode.cn/problems/html-entity-parser/)

## 题目大意

**描述**：给定一个字符串 $text$，将其中的 HTML 实体字符替换为对应的字符。

HTML 实体映射：
- `&quot;` → `"`
- `&apos;` → `'`
- `&amp;` → `&`
- `&gt;` → `>`
- `&lt;` → `<`
- `&frasl;` → `/`

**要求**：返回替换后的字符串。

**示例**：

- 示例 1：

```python
输入：text = "&amp; is an HTML entity but &ambassador; is not."
输出："& is an HTML entity but &ambassador; is not."
解释：解析器把字符实体 &amp; 用 & 替换


示例 2：


输入：text = "and I quote: &quot;...&quot;"
输出："and I quote: \"...\""


示例 3：


输入：text = "Stay home! Practice on Leetcode :)"
输出："Stay home! Practice on Leetcode :)"


示例 4：


输入：text = "x &gt; y &amp;&amp; x &lt; y is always false"
输出："x > y && x < y is always false"


示例 5：


输入：text = "leetcode.com&frasl;problemset&frasl;all"
输出："leetcode.com/problemset/all"
```

- 示例 2：

```python
输入：
输出：
```

## 解题思路

### 思路 1：顺序替换

#### 1. 核心思想

用哈希表建立实体到字符的映射。遍历字符串，检查当前位置是否是 `&`，然后尝试匹配映射中的实体。

注意：`&amp;` 的替换可能影响其他实体，因为其他实体名称中包含 `&`。需要先替换长的实体（或逐字符扫描匹配）。

逐字符扫描法：
- 遍历每个字符，如果遇到 `&`，从该位置开始尝试匹配最长可能的实体。
- 匹配成功则替换，指针跳转到实体后；否则原样保留。

#### 2. 具体步骤

**第 1 步**：建立实体字典。

**第 2 步**：遍历字符串：
- 如果当前字符是 `&`，从 $i+1$ 开始找最近的 `;`。
- 截取子串，在字典中查找。
- 匹配则替换，指针移动。
- 不匹配则原样输出。

**第 3 步**：返回结果。

#### 3. 举例说明

输入：`"&amp; is an HTML entity but &ambassador; is not."`

匹配 `&amp;` → 替换为 `&`。
`&ambassador;` 不在映射中 → 保留原样。

输出：`"& is an HTML entity but &ambassador; is not."`

### 思路 1：代码

```python
class Solution:
    def entityParser(self, text: str) -> str:
        entities = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }

        ans = []
        i, n = 0, len(text)
        while i < n:
            if text[i] == '&':
                # 找最近的分号
                j = text.find(';', i + 1)
                if j != -1:
                    entity = text[i:j + 1]
                    if entity in entities:
                        ans.append(entities[entity])
                        i = j + 1
                        continue
            ans.append(text[i])
            i += 1

        return ''.join(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，每个字符遍历一次。
- **空间复杂度**：$O(n)$，存储结果字符串。
