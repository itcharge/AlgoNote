# KMP 匹配算法，T 为文本串，p 为模式串
def kmp(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    next = generateNext(p)                      # 生成 next 数组
    
    j = 0                                       # j 为模式串中当前匹配的位置
    for i in range(n):                          # i 为文本串中当前匹配的位置
        while j > 0 and T[i] != p[j]:           # 如果模式串匹配不成功, 将模式串进行回退, j == 0 时停止回退
            j = next[j - 1]
        if T[i] == p[j]:                        # 当前模式串前缀匹配成功，令 j += 1，继续匹配
            j += 1
        if j == m:                              # 当前模式串完全匹配成功，返回匹配开始位置
            return i - j + 1
    return -1                                   # 匹配失败，返回 -1
            
    
# 生成 next 数组
# next[j] 表示下标 j 之前的模式串 p 中，最长相等前后缀的长度
def generateNext(p: str):
    m = len(p)
    next = [0 for _ in range(m)]                # 初始化数组元素全部为 0
    
    left = 0                                    # left 表示前缀串开始所在的下标位置
    for right in range(1, m):                   # right 表示后缀串开始所在的下标位置
        while left > 0 and p[left] != p[right]: # 匹配不成功, left 进行回退, left == 0 时停止回退
            left = next[left - 1]               # left 进行回退操作
        if p[left] == p[right]:                 # 匹配成功，找到相同的前后缀，先让 left += 1，此时 left 为前缀长度
            left += 1
        next[right] = left                      # 记录前缀长度，更新 next[right], 结束本次循环, right += 1

    return next

print(kmp("abbcfdddbddcaddebc", "ABCABCD"))
print(kmp("abbcfdddbddcaddebc", "bcf"))
print(kmp("aaaaa", "bba"))
print(kmp("mississippi", "issi"))
print(kmp("ababbbbaaabbbaaa", "bbbb"))