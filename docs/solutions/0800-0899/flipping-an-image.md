# [0832. 翻转图像](https://leetcode.cn/problems/flipping-an-image/)

- 标签：数组、双指针、矩阵、模拟
- 难度：简单

## 题目链接

- [0832. 翻转图像 - 力扣](https://leetcode.cn/problems/flipping-an-image/)

## 题目大意

给定一个二进制矩阵 `A` 代表图像，先将矩阵进行水平翻转，再进行翻转（将 0 变为 1，1 变为 0）。

## 解题思路

两重 for 循环，第二层 for 循环遍历到一半即可。对于 `image[i][j]`、`image[i][n-1-j]` 先水平翻转操作，再进行翻转。

## 代码

```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range((n+1)//2):
                image[i][j], image[i][n-1-j] = image[i][n-1-j], image[i][j]
                image[i][j] = 0 if image[i][j] == 1 else 1
                if j != n-1-j:
                    image[i][n-1-j] = 0 if image[i][n-1-j] == 1 else 1
        return image
```

