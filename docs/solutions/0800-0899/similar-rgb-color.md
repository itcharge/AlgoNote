# [0800. 相似 RGB 颜色](https://leetcode.cn/problems/similar-rgb-color/)

- 标签：数学、字符串、枚举
- 难度：简单

## 题目链接

- [0800. 相似 RGB 颜色 - 力扣](https://leetcode.cn/problems/similar-rgb-color/)

## 题目大意

**描述**：RGB 颜色 `"#AABBCC"` 可以简写成 `"#ABC"` 。例如，`"#1155cc"` 可以简写为 `"#15c"`。现在给定一个按 `"#ABCDEF"` 形式定义的字符串 `color` 表示 RGB 颜色。

**要求**：返回一个与 `color` 相似度最大并且可以简写的颜色。

**说明**：

- 两个颜色 `"#ABCDEF"` 和 `"#UVWXYZ"` 的相似度计算公式为：$-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2$。

**示例**：

- 示例 1：

```python
输入 color = "#09f166"
输出 "#11ee66"
解释： 因为相似度计算得出 -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73，这是所有可以简写的颜色中与 color 最相似的颜色
```

## 解题思路

### 思路 1：枚举算法

所有可以简写的颜色范围是 `"#000"` ~ `"#fff"`，共 $16^3 = 4096$ 种颜色。因此，我们可以枚举这些可以简写的颜色，并计算出其与 $color$的相似度，从而找出与 $color$ 最相似的颜色。具体做法如下：

- 将  $color$ 转换为十六进制数，即 `hex_color = int(color[1:], 16)`。
- 三重循环遍历 $R$、$G$、$B$ 三个通道颜色，每一重循环范围为 $0 \sim 15$。
- 计算出每一种可以简写的颜色对应的十六进制，即 $17 \times R \times (1 << 16) + 17 \times G \times (1 << 8) + 17 \times B$，$17$ 是 $0x11 = 16 + 1 = 17$，$(1 << 16)$ 为 $R$ 左移的位数，$17 \times R \times (1 << 16)$ 就表示 $R$ 通道上对应的十六进制数。$(1 << 8)$ 为 $G$ 左移的位数，$17 \times G \times (1 << 8)$ 就表示 $G$ 通道上对应的十六进制数。$17 \times B$ 就表示 $B$ 通道上对应的十六进制数。
- 然后我们根据 $color$ 的十六进制数，与每一个可以简写的颜色对应的十六进制数，计算出相似度，并找出大相似对应的颜色。将其转换为字符串，并输出。

### 思路 1：枚举算法代码

```python
class Solution:
    def similar(self, hex1, hex2):
        r1, g1, b1 = hex1 >> 16, (hex1 >> 8) % 256, hex1 % 256
        r2, g2, b2 = hex2 >> 16, (hex2 >> 8) % 256, hex2 % 256
        return - (r1 - r2) ** 2 - (g1 - g2) ** 2 - (b1 - b2) ** 2

    def similarRGB(self, color: str) -> str:
        ans = 0
        hex_color = int(color[1:], 16)
        for r in range(16):
            for g in range(16):
                for b in range(16):
                    hex_cur = 17 * r * (1 << 16) + 17 * g * (1 << 8) + 17 * b
                    if self.similar(hex_color, hex_cur) > self.similar(hex_color, ans):
                        ans = hex_cur
        
        return "#{:06x}".format(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(16^3)$。
- **空间复杂度**：$O(1)$。
