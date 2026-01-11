# [0157. 用 Read4 读取 N 个字符](https://leetcode.cn/problems/read-n-characters-given-read4/)

- 标签：数组、交互、模拟
- 难度：简单

## 题目链接

- [0157. 用 Read4 读取 N 个字符 - 力扣](https://leetcode.cn/problems/read-n-characters-given-read4/)

## 题目大意

**描述**：

给定一个文件，并且该文件只能通过给定的 `read4` 方法来读取，请实现一个方法使其能够读取 $n$ 个字符。

`read4` 方法：

- API `read4` 可以从文件中读取 4 个连续的字符，并且将它们写入缓存数组 `buf4` 中。
- 返回值为实际读取的字符个数。
- 注意 `read4()` 自身拥有文件指针，很类似于 C 语言中的 `FILE *fp`。

`read4` 的定义：

```python
参数类型: char[] buf4
返回类型: int
```

注意: `buf4[]` 是目标缓存区不是源缓存区，`read4` 的返回结果将会复制到 `buf4[]` 当中。

下列是一些使用 `read4` 的例子：

```python
File file("abcde"); // 文件名为 "abcde"，初始文件指针 (fp) 指向 'a'
char[] buf4 = new char[4]; // 创建一个缓存区使其能容纳足够的字符
read4(buf4); // read4 返回 4。现在 buf4 = "abcd"，fp 指向 'e'
read4(buf4); // read4 返回 1。现在 buf4 = "e"，fp 指向文件末尾
read4(buf4); // read4 返回 0。现在 buf4 = ""，fp 指向文件末尾
```

`read` 方法：

- 通过使用 `read4` 方法，实现 `read` 方法。该方法可以从文件中读取 $n$ 个字符并将其存储到缓存数组 `buf` 中。您 **不能** 直接操作文件。
- 返回值为实际读取的字符。

`read` 的定义：

```python
参数类型: `char[] buf`, `int n`
返回类型: `int`
```

注意: `buf[]` 是目标缓存区不是源缓存区，你需要将结果写入 `buf[]` 中。

**要求**：返回实际读取的字符数。

**说明**：

- 你 **不能** 直接操作该文件，文件只能通过 `read4` 获取而 **不能** 通过 `read`。
- `read` 函数只在每个测试用例调用一次。
- 你可以假定目标缓存数组 `buf` 保证有足够的空间存下 $n$ 个字符。

**示例**：

- 示例 1：

```python
输入：file = "abc", n = 4
输出：3
解释：当执行你的 read 方法后，buf 需要包含 "abc"。文件一共 3 个字符，因此返回 3。注意 "abc" 是文件的内容，不是 buf 的内容，buf 是你需要写入结果的目标缓存区。
```

- 示例 2：

```python
输入：file = "abcde", n = 5
输出：5
解释：当执行你的 read 方法后，buf 需要包含 "abcde"。文件共 5 个字符，因此返回 5。
```

- 示例 3：

```python
输入：file = "abcdABCD1234", n = 12
输出：12
解释：当执行你的 read 方法后，buf 需要包含 "abcdABCD1234"。文件一共 12 个字符，因此返回 12。
```

- 示例 4：

```python
输入：file = "leetcode", n = 5
输出：5
解释：当执行你的 read 方法后，buf 需要包含 "leetc"。文件中一共 5 个字符，因此返回 5。
```

## 解题思路

### 思路 1：模拟 + 循环调用 read4

#### 思路 1：算法描述

这道题的核心是使用 `read4` API 来实现读取 $n$ 个字符的功能。

**算法步骤**：

1. 创建一个临时缓冲区 $buf4$，用于存储每次 `read4` 读取的 4 个字符。
2. 循环调用 `read4`，每次最多读取 4 个字符。
3. 将读取的字符复制到目标缓冲区 $buf$ 中，但不能超过 $n$ 个字符。
4. 如果 `read4` 返回的字符数少于 4，说明文件已读完，提前结束。
5. 返回实际读取的字符总数。

**关键点**：

- 每次调用 `read4` 最多读取 4 个字符，但实际可能少于 4 个（文件末尾）。
- 需要控制总共读取的字符数不超过 $n$。
- 使用变量 $total$ 记录已读取的字符总数。

#### 思路 1：代码

```python
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        total = 0  # 已读取的字符总数
        buf4 = [''] * 4  # 临时缓冲区
        
        while total < n:
            # 调用 read4 读取最多 4 个字符
            count = read4(buf4)
            
            # 如果读到文件末尾，提前结束
            if count == 0:
                break
            
            # 计算本次应该复制的字符数（不能超过剩余需要读取的字符数）
            copy_count = min(count, n - total)
            
            # 将字符复制到目标缓冲区
            for i in range(copy_count):
                buf[total] = buf4[i]
                total += 1
        
        return total
```

#### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是需要读取的字符数。最多需要调用 $\lceil n / 4 \rceil$ 次 `read4`。
- **空间复杂度**：$O(1)$，只使用了固定大小的临时缓冲区 $buf4$。
