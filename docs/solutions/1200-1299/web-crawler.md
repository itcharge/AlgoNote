# [1236. 网络爬虫](https://leetcode.cn/problems/web-crawler/)

- 标签：深度优先搜索、广度优先搜索、字符串、交互
- 难度：中等

## 题目链接

- [1236. 网络爬虫 - 力扣](https://leetcode.cn/problems/web-crawler/)

## 题目大意

**描述**：给定一个起始 URL $startUrl$ 和一个网页爬虫接口 $HtmlParser$（提供 $getUrls(url)$ 方法，返回该页面包含的所有 URL）。

**要求**：抓取所有与 $startUrl$ 同主机名的网页。使用单线程完成。返回抓取到的所有 URL 列表。

**说明**：

- URL 格式为 `http://hostname/path`。
- 同一个 URL 不应重复抓取。
- 不同主机名的 URL 不抓取。

**示例**：

- 示例 1：

```python
输入：urls = ["http://news.yahoo.com",
             "http://news.yahoo.com/news",
             "http://news.yahoo.com/news/topics/",
             "http://news.google.com"],
      startUrl = "http://news.yahoo.com/news/topics/"
输出：["http://news.yahoo.com/news/topics/",
      "http://news.yahoo.com",
      "http://news.yahoo.com/news"]
```

## 解题思路

### 思路 1：BFS

#### 1. 核心思想

标准的 BFS（或 DFS）遍历。从起始 URL 开始，获取当前页面的所有链接，如果与目标主机名相同且未访问过，加入队列继续遍历。

#### 2. 建图、遍历、标记、收集

- **建图**：网页间的链接构成隐式图，通过 $getUrls$ 动态获取邻居。
- **遍历**：BFS 或 DFS 均可。BFS 用队列，DFS 用栈。
- **标记**：集合记录已访问的 URL。
- **收集**：所有访问过的 URL 即为结果。

#### 3. 具体步骤

**第 1 步**：解析 $startUrl$ 的主机名。

**第 2 步**：初始化队列、已访问集合。

**第 3 步**：BFS 循环：
- 从队列中取出 URL。
- 通过 $htmlParser.getUrls(url)$ 获取所有链接。
- 对每个链接，如果与目标主机名相同且未访问过，加入队列和已访问集合。

**第 4 步**：返回已访问集合。

#### 4. 结合示例走一遍

$startUrl = \text{"http://news.yahoo.com/news/topics/"}$, 主机名 = $\text{"news.yahoo.com"}$

```
队列: ["http://news.yahoo.com/news/topics/"]
visited: {"http://news.yahoo.com/news/topics/"}

取出 "http://news.yahoo.com/news/topics/", 获取其链接:
  - "http://news.yahoo.com" → 同主机名, 未访问 → 入队, visited
  - "http://news.yahoo.com/news" → 同主机名, 未访问 → 入队, visited
  - "http://news.google.com" → 不同主机名 → 跳过

取出 "http://news.yahoo.com", 获取其链接:
  - "http://news.yahoo.com/news" → 已访问 → 跳过
  - "http://news.yahoo.com/news/topics/" → 已访问 → 跳过

取出 "http://news.yahoo.com/news", 获取其链接:
  - ... (已访问, 跳过)

队列为空，结束。
```

### 思路 1：代码

```python
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # 提取主机名
        hostname = startUrl.split('/')[2]
        visited = set([startUrl])
        q = deque([startUrl])

        while q:
            url = q.popleft()
            for next_url in htmlParser.getUrls(url):
                # 检查是否同主机名
                if next_url.startswith('http://' + hostname) or \
                   next_url.startswith('https://' + hostname):
                    if next_url not in visited:
                        visited.add(next_url)
                        q.append(next_url)

        return list(visited)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(N)$，其中 $N$ 是抓取的页面数。每个页面通过 $getUrls$ 获取一次链接。
- **空间复杂度**：$O(N)$，存储已访问集合和队列。
