class Solution:
    def digitDP(self, n: int) -> int:
        s = str(n)
        
        @cache
        # pos: 第 pos 个数位
        # state: 之前选过的数字集合。
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        # isNum: 表示 pos 前面的数位是否填了数字。
        # 如果为真，则当前位不可跳过；如果为假，则当前位可跳过。
        def dfs(pos, state, isLimit, isNum):
            if pos == len(s):
                # isNum 为 True，则表示当前方案符合要求
                return int(isNum)
            
            ans = 0
            if not isNum:
                # 如果 isNumb 为 False，则可以跳过当前数位
                ans = dfs(pos + 1, state, False, False)
            
            # 如果前一位没有填写数字，则最小可选择数字为 0，否则最少为 1（不能含有前导 0）。
            minX = 0 if isNum else 1
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s[pos]) if isLimit else 9
            
            # 枚举可选择的数字
            for x in range(minX, maxX + 1): 
                # x 不在选择的数字集合中，即之前没有选择过 x
                if (state >> x) & 1 == 0:
                    ans += dfs(pos + 1, state | (1 << x), isLimit and x == maxX, True)
            return ans
    
        return dfs(0, 0, True, False)