# [1472. 设计浏览器历史记录](https://leetcode.cn/problems/design-browser-history/)

- 标签：栈、设计、数组、链表、数据流
- 难度：中等

## 题目链接

- [1472. 设计浏览器历史记录 - 力扣](https://leetcode.cn/problems/design-browser-history/)

## 题目大意

**描述**：实现一个 `BrowserHistory` 类，支持：
- `BrowserHistory(homepage)` 初始化，访问 $homepage$。
- `visit(url)` 访问 $url$，清除前进历史。
- `back(steps)` 后退 $steps$ 步，返回当前页面。
- `forward(steps)` 前进 $steps$ 步，返回当前页面。

**示例**：

- 示例 1：

```python
示例：

输入：
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
输出：
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

解释：
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // 你原本在浏览 "leetcode.com" 。访问 "google.com"
browserHistory.visit("facebook.com");     // 你原本在浏览 "google.com" 。访问 "facebook.com"
browserHistory.visit("youtube.com");      // 你原本在浏览 "facebook.com" 。访问 "youtube.com"
browserHistory.back(1);                   // 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
browserHistory.back(1);                   // 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
browserHistory.forward(1);                // 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
browserHistory.visit("linkedin.com");     // 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
browserHistory.forward(2);                // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
browserHistory.back(2);                   // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
browserHistory.back(7);                   // 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"
```

## 解题思路

### 思路 1：双栈（或数组 + 指针）

#### 1. 核心思想

用两个栈（或一个数组加一个指针）维护历史记录。前进栈在 $visit$ 时清空。

用列表 $history$ 存储所有访问过的页面，$pos$ 表示当前页面索引。

- `visit(url)`：截断 $pos+1$ 之后的历史，加入新 $url$，$pos$ 指向新位置。
- `back(steps)`：$pos = \max(0, pos - steps)$。
- `forward(steps)`：$pos = \min(len(history)-1, pos + steps)$。

#### 2. 举例说明

`BrowserHistory("leetcode.com")`
`visit("google.com")` → $["leetcode","google"], pos=1$
`visit("facebook.com")` → $["leetcode","google","facebook"], pos=2$
`back(1)` → $pos=1$, 返回 "google"
`back(1)` → $pos=0$, 返回 "leetcode"
`forward(1)` → $pos=1$, 返回 "google"
`visit("twitter.com")` → 截断，$["leetcode","google","twitter"], pos=2$
`back(2)` → $pos=0$, 返回 "leetcode"
`forward(2)` → $pos=2$, 返回 "twitter"

### 思路 1：代码

```python
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        # 清除前进历史
        self.history = self.history[:self.pos + 1]
        self.history.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(len(self.history) - 1, self.pos + steps)
        return self.history[self.pos]
```

### 思路 1：复杂度分析

- **时间复杂度**：$visit$ $O(n)$（截断复制），$back$ 和 $forward$ $O(1)$。用链表可实现 $visit$ $O(1)$。
- **空间复杂度**：$O(n)$。

---

### 思路 2：双向链表

用双向链表实现，$visit$ 时不需要截断复制：

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = node

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
```
