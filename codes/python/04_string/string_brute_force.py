def bruteForce(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    i, j = 0, 0                     # i 表示文本串 T 的当前位置，j 表示模式串 p 的当前位置
    while i < n and j < m:          # i 或 j 其中一个到达尾部时停止搜索
        if T[i] == p[j]:            # 如果相等，则继续进行下一个字符匹配
            i += 1
            j += 1
        else:
            i = i - (j - 1)         # 如果匹配失败则将 i 移动到上次匹配开始位置的下一个位置
            j = 0                   # 匹配失败 j 回退到模式串开始位置

    if j == m:
        return i - j                # 匹配成功，返回匹配的开始位置
    else:
        return -1                   # 匹配失败，返回 -1
        
print(bruteForce("abcdeabc", "bcd"))