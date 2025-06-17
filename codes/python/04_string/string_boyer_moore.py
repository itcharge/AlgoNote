# BM 匹配算法
def boyerMoore(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    bc_table = generateBadCharTable(p)              # 生成坏字符位置表
    gs_list = generageGoodSuffixList(p)             # 生成好后缀规则后移位数表
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j > -1 and T[i + j] == p[j]:          # 进行后缀匹配，跳出循环说明出现坏字符
            j -= 1
        if j < 0:
            return i                                # 匹配完成，返回模式串 p 在文本串 T 中的位置
        bad_move = j - bc_table.get(T[i + j], -1)   # 坏字符规则下的后移位数
        good_move = gs_list[j]                      # 好后缀规则下的后移位数
        i += max(bad_move, good_move)               # 取两种规则下后移位数的最大值进行移动
    return -1
            
    
# 生成坏字符位置表
# bc_table[bad_char] 表示坏字符在模式串中最后一次出现的位置
def generateBadCharTable(p: str):
    bc_table = dict()
    
    for i in range(len(p)):
        bc_table[p[i]] = i                          # 更新坏字符在模式串中最后一次出现的位置
    return bc_table

# 生成好后缀规则后移位数表
# gs_list[j] 表示在 j 下标处遇到坏字符时，可根据好规则向右移动的距离
def generageGoodSuffixList(p: str):
    # 好后缀规则后移位数表
    # 情况 1: 模式串中有子串匹配上好后缀
    # 情况 2: 模式串中无子串匹配上好后缀，但有最长前缀匹配好后缀的后缀
    # 情况 3: 模式串中无子串匹配上好后缀，也找不到前缀匹配
    
    m = len(p)
    gs_list = [m for _ in range(m)]                 # 情况 3：初始化时假设全部为情况 3
    suffix = generageSuffixArray(p)                 # 生成 suffix 数组
    
    j = 0                                           # j 为好后缀前的坏字符位置
    for i in range(m - 1, -1, -1):                  # 情况 2：从最长的前缀开始检索
        if suffix[i] == i + 1:                      # 匹配到前缀，即 p[0...i] == p[m-1-i...m-1]
            while j < m - 1 - i:
                if gs_list[j] == m:
                    gs_list[j] = m - 1 - i          # 更新在 j 处遇到坏字符可向后移动位数
                j += 1
        
    for i in range(m - 1):                          # 情况 1：匹配到子串 p[i-s...i] == p[m-1-s, m-1]
        gs_list[m - 1 - suffix[i]] = m - 1 - i      # 更新在好后缀的左端点处遇到坏字符可向后移动位数
    return gs_list

# 生成 suffix 数组
# suffix[i] 表示为以下标 i 为结尾的子串与模式串后缀匹配的最大长度
def generageSuffixArray(p: str):
    m = len(p)
    suffix = [m for _ in range(m)]                  # 初始化时假设匹配的最大长度为 m
    for i in range(m - 2, -1, -1):                  # 子串末尾从 m - 2 开始
        start = i                                   # start 为子串开始位置
        while start >= 0 and p[start] == p[m - 1 - i + start]:
            start -= 1                              # 进行后缀匹配，start 为匹配到的子串开始位置
        suffix[i] = i - start                       # 更新以下标 i 为结尾的子串与模式串后缀匹配的最大长度
    return suffix

print(boyerMoore("abbcfdddbddcaddebc", "aaaaa"))
print(boyerMoore("", ""))