# [0271. 字符串的编码与解码](https://leetcode.cn/problems/encode-and-decode-strings/)

- 标签：设计、数组、字符串
- 难度：中等

## 题目链接

- [0271. 字符串的编码与解码 - 力扣](https://leetcode.cn/problems/encode-and-decode-strings/)

## 题目大意

**要求**：

设计一个算法，可以将一个「字符串列表」编码成为一个「字符串」。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
1 号机（发送方）有如下函数：

```C++
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

2 号机（接收方）有如下函数：

```C++
vector<string> decode(string s) {
  //... your code
  return strs;
}
```

1 号机（发送方）执行：

```C++
string encoded_string = encode(strs);
```

2 号机（接收方）执行：

```C++
vector<string> strs2 = decode(encoded_string);
```

此时，2 号机（接收方）的 $strs2$ 需要和 1 号机（发送方）的 $strs$ 相同。

请你来实现这个 $encode$ 和 $decode$ 方法。

不允许使用任何序列化方法解决这个问题（例如 eval）。

**说明**：

- $1 \le strs.length \le 200$。
- $0 \le strs[i].length \le 200$。
- $strs[i]$ 包含 $256$ 个有效 ASCII 字符中的任何可能字符。

- 进阶：你能编写一个通用算法来处理任何可能的字符集吗？

**示例**：

- 示例 1：

```python
输入：dummy_input = ["Hello","World"]
输出：["Hello","World"]
解释：
1 号机：
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

2 号机：
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

- 示例 2：

```python
输入：dummy_input = [""]
输出：[""]
```

## 解题思路

### 思路 1：长度前缀编码

这是一个典型的设计问题。我们需要将字符串列表编码成单个字符串，然后能够正确解码。

**核心问题**：如何区分不同的字符串？由于字符串可能包含任何 ASCII 字符，包括分隔符，我们需要一种方法来明确标识每个字符串的边界。

**解决方案**：使用长度前缀编码。对于每个字符串 $str_i$，我们将其长度 $len_i$ 和字符串内容连接起来，格式为 $len_i + ":" + str_i$。

**算法步骤**：

1. **编码过程**：
   - 遍历字符串列表 $strs$。
   - 对于每个字符串 $str_i$，计算其长度 $len_i$。
   - 将 $len_i + ":" + str_i$ 添加到结果字符串中。

2. **解码过程**：
   - 使用指针 $i$ 遍历编码后的字符串。
   - 找到冒号 `:` 的位置，提取长度信息 $len_i$。
   - 根据长度 $len_i$ 提取对应的字符串内容。
   - 将提取的字符串加入结果列表，继续处理下一个字符串。

**关键点**：

- 冒号 `:` 作为长度和内容的分隔符。
- 长度信息确保我们能够准确提取每个字符串。
- 这种方法可以处理包含任何 ASCII 字符的字符串。

### 思路 1：代码

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        
        Args:
            strs: 字符串列表
            
        Returns:
            编码后的字符串
        """
        encoded = ""
        for s in strs:
            # 将每个字符串的长度和内容用冒号分隔
            encoded += str(len(s)) + ":" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        
        Args:
            s: 编码后的字符串
            
        Returns:
            解码后的字符串列表
        """
        decoded = []
        i = 0
        
        while i < len(s):
            # 找到冒号的位置，提取长度信息
            colon_pos = s.find(":", i)
            length = int(s[i:colon_pos])
            
            # 根据长度提取字符串内容
            start = colon_pos + 1
            end = start + length
            decoded.append(s[start:end])
            
            # 更新指针位置
            i = end
            
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 编码：$O(n)$，其中 $n$ 是所有字符串的总长度。
  - 解码：$O(n)$，需要遍历整个编码字符串一次。
- **空间复杂度**：$O(n)$，存储编码后的字符串。
