# sunday 算法，T 为文本串，p 为模式串
def sunday(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    bc_table = generateBadCharTable(p)          # 生成后移位数表
    
    i = 0
    while i <= n - m:
        j = 0
        if T[i: i + m] == p:
            return i                            # 匹配完成，返回模式串 p 在文本串 T 的位置
        if i + m >= n:
            return -1
        i += bc_table.get(T[i + m], m + 1)      # 通过后移位数表，向右进行进行快速移动
    return -1                                   # 匹配失败

# 生成后移位数表
# bc_table[bad_char] 表示遇到坏字符可以向右移动的距离
def generateBadCharTable(p: str):
    m = len(p)
    bc_table = dict()
    
    for i in range(m):                      # 迭代到最后一个位置 m - 1
        bc_table[p[i]] = m - i              # 更新遇到坏字符可向右移动的距离
    return bc_table

print(sunday("abbcfdddbddcaddebc", "aaaaa"))
print(sunday("abbcfdddbddcaddebc", "bcf"))
print(sunday("aaaaa", "bba"))
print(sunday("mississippi", "issi"))
print(sunday("ababbbbaaabbbaaa", "bbbb"))