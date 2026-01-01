# [0535. TinyURL 的加密与解密](https://leetcode.cn/problems/encode-and-decode-tinyurl/)

- 标签：设计、哈希表、字符串、哈希函数
- 难度：中等

## 题目链接

- [0535. TinyURL 的加密与解密 - 力扣](https://leetcode.cn/problems/encode-and-decode-tinyurl/)

## 题目大意

**描述**：

TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的 URL http://tinyurl.com/4e9iAk。

**要求**：

请你设计一个类来加密与解密 TinyURL。

加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL，并且这个 TinyURL 可以用解密方法恢复成原本的 URL。

实现 Solution 类：

- `Solution()` 初始化 TinyURL 系统对象。
- `String encode(String longUrl)` 返回 $longUrl$ 对应的 TinyURL。
- `String decode(String shortUrl)` 返回 $shortUrl$ 原本的 URL。题目数据保证给定的 $shortUrl$ 是由同一个系统对象加密的。

**说明**：

- $1 \le url.length \le 10^{4}$。
- 题目数据保证 url 是一个有效的 URL。

**示例**：

- 示例 1：

```python
输入：url = "https://leetcode.com/problems/design-tinyurl"
输出："https://leetcode.com/problems/design-tinyurl"

解释：
Solution obj = new Solution();
string tiny = obj.encode(url); // 返回加密后得到的 TinyURL 。
string ans = obj.decode(tiny); // 返回解密后得到的原本的 URL 。
```

## 解题思路

### 思路 1：哈希表 + 自增 ID

使用哈希表存储长 URL 和短 URL 的映射关系，使用自增 ID 生成短 URL。

核心思路：

1. 使用两个哈希表：
   - $long\_to\_short$：存储长 URL 到短 URL 的映射。
   - $short\_to\_long$：存储短 URL 到长 URL 的映射。

2. 编码（encode）：
   - 检查长 URL 是否已编码过，如果是则直接返回对应的短 URL。
   - 否则，使用自增 ID 生成新的短 URL，格式为 `http://tinyurl.com/{id}`。
   - 将映射关系存入两个哈希表。

3. 解码（decode）：
   - 从短 URL 中提取 ID，通过哈希表查找对应的长 URL。

### 思路 1：代码

```python
class Codec:

    def __init__(self):
        self.long_to_short = {}  # 长 URL -> 短 URL
        self.short_to_long = {}  # 短 URL -> 长 URL
        self.id = 0  # 自增 ID
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # 如果已经编码过，直接返回
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        
        # 生成短 URL
        self.id += 1
        short_url = self.base_url + str(self.id)
        
        # 存储映射关系
        self.long_to_short[longUrl] = short_url
        self.short_to_long[short_url] = longUrl
        
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # 从哈希表中查找长 URL
        return self.short_to_long[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `encode`：$O(1)$，哈希表插入操作。
  - `decode`：$O(1)$，哈希表查询操作。
- **空间复杂度**：$O(n)$，其中 $n$ 为编码的 URL 数量。
