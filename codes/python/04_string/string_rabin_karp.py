# T 为文本串，p 为模式串，d 为字符集的字符种类数，q 为质数
def rabinKarp(T: str, p: str, d, q) -> int:
    n, m = len(T), len(p)
    if n < m:
        return -1
    
    hash_p, hash_t = 0, 0
    
    for i in range(m):
        hash_p = (hash_p * d + ord(p[i])) % q           # 计算模式串 p 的哈希值
        hash_t = (hash_t * d + ord(T[i])) % q           # 计算文本串 T 中第一个子串的哈希值
    
    power = pow(d, m - 1) % q                           # power 用于移除字符哈希时
    
    for i in range(n - m + 1):
        if hash_p == hash_t:                            # 检查模式串 p 的哈希值和子串的哈希值
            match = True                                # 如果哈希值相等，验证模式串和子串每个字符是否完全相同（避免哈希冲突）
            for j in range(m):
                if T[i + j] != p[j]:
                    match = False                       # 模式串和子串某个字符不相等，验证失败，跳出循环
                    break
            if match:                                   # 如果模式串和子串每个字符是否完全相同，返回匹配开始位置
                return i
        if i < n - m:                                   # 计算下一个相邻子串的哈希值
            hash_t = (hash_t - power * ord(T[i])) % q   # 移除字符 T[i]
            hash_t = (hash_t * d + ord(T[i + m])) % q   # 增加字符 T[i + m]
            hash_t = (hash_t + q) % q                   # 确保 hash_t >= 0
        
    return -1

print(rabinKarp("aaaaa", "bba", 256, 101))