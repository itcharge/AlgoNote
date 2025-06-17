# horspool 算法，T 为文本串，p 为模式串
def horspool(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    bc_table = generateBadCharTable(p)          # 生成后移位数表
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j > -1 and T[i + j] == p[j]:      # 进行后缀匹配，跳出循环说明出现坏字符
            j -= 1
        if j < 0:
            return i                            # 匹配完成，返回模式串 p 在文本串 T 中的位置
        i += bc_table.get(T[i + m - 1], m)      # 通过后移位数表，向右进行进行快速移动
    return -1                                   # 匹配失败

# 生成后移位数表
# bc_table[bad_char] 表示遇到坏字符可以向右移动的距离
def generateBadCharTable(p: str):
    m = len(p)
    bc_table = dict()
    
    for i in range(m - 1):                      # 迭代到 m - 2
        bc_table[p[i]] = m - 1 - i              # 更新遇到坏字符可向右移动的距离
    return bc_table

print(horspool("abbcfdddbddcaddebc", "aaaaa"))
print(horspool("abbcfdddbddcaddebc", "bcf"))
print(horspool("aaaaa", "bba"))
print(horspool("mississippi", "issi"))
print(horspool("ababbbbaaabbbaaa", "bbbb"))