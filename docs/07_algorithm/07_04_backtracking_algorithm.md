## 1. 回溯算法简介

> **回溯算法（Backtracking）**：一种能避免不必要搜索的穷举式的搜索算法。采用试错的思想，在搜索尝试过程中寻找问题的解，当探索到某一步时，发现原先的选择并不满足求解条件，或者还需要满足更多求解条件时，就退回一步（回溯）重新选择，这种走不通就退回再走的技术称为「回溯法」，而满足回溯条件的某个状态的点称为「回溯点」。

简单来说，回溯算法采用了一种 **「走不通就回退」** 的算法思想。

回溯算法通常用简单的递归方法来实现，在进行回溯过程中更可能会出现两种情况：

1. 找到一个可能存在的正确答案；
2. 在尝试了所有可能的分布方法之后宣布该问题没有答案。

## 2. 从全排列问题开始理解回溯算法

以求解 $[1, 2, 3]$ 的全排列为例，我们来讲解一下回溯算法的过程。

1. 选择以 $1$ 为开头的全排列。
   1. 选择以 $2$ 为中间数字的全排列，则最后数字只能选择 $3$。即排列为：$[1, 2, 3]$。
   2. 撤销选择以 $3$ 为最后数字的全排列，再撤销选择以 $2$ 为中间数字的全排列。然后选择以 $3$ 为中间数字的全排列，则最后数字只能选择 $2$，即排列为：$[1, 3, 2]$。
2. 撤销选择以 $2$ 为最后数字的全排列，再撤销选择以 $3$ 为中间数字的全排列，再撤销选择以 $1$ 为开头的全排列。然后选择以 $2$ 开头的全排列。
   1. 选择以 $1$ 为中间数字的全排列，则最后数字只能选择 $3$。即排列为：$[2, 1, 3]$。
   2. 撤销选择以 $3$ 为最后数字的全排列，再撤销选择以 $1$ 为中间数字的全排列。然后选择以 $3$ 为中间数字的全排列，则最后数字只能选择 $1$，即排列为：$[2, 3, 1]$。
3. 撤销选择以 $1$ 为最后数字的全排列，再撤销选择以 $3$ 为中间数字的全排列，再撤销选择以 $2$ 为开头的全排列，选择以 $3$ 开头的全排列。
   1. 选择以 $1$ 为中间数字的全排列，则最后数字只能选择 $2$。即排列为：$[3, 1, 2]$。
   2. 撤销选择以 $2$ 为最后数字的全排列，再撤销选择以 $1$ 为中间数字的全排列。然后选择以 $2$ 为中间数字的全排列，则最后数字只能选择 $1$，即排列为：$[3, 2, 1]$。

总结一下全排列的回溯过程：

- **按顺序枚举每一位上可能出现的数字，之前已经出现的数字在接下来要选择的数字中不能再次出现。** 
- 对于每一位，进行如下几步：
  1. **选择元素**：从可选元素列表中选择一个之前没有出现过的元素。
  2. **递归搜索**：从选择的元素出发，一层层地递归搜索剩下位数，直到遇到边界条件时，不再向下搜索。
  3. **撤销选择**：一层层地撤销之前选择的元素，转而进行另一个分支的搜索。直到完全遍历完所有可能的路径。

对于上述决策过程，我们也可以用一棵决策树来表示：

![全排列问题的决策树](https://qcdn.itcharge.cn/images/20220425102048.png)

从全排列的决策树中我们可以看出：

- 每一层中有一个或多个不同的节点，这些节点以及节点所连接的分支代表了「不同的选择」。
- 每一个节点代表了求解全排列问题的一个「状态」，这些状态是通过「不同的值」来表现的。
- 每向下递推一层就是在「可选元素列表」中选择一个「元素」加入到「当前状态」。
- 当一个决策分支探索完成之后，会逐层向上进行回溯。
- 每向上回溯一层，就是把所选择的「元素」从「当前状态」中移除，回退到没有选择该元素时的状态（或者说重置状态），从而进行其他分支的探索。

根据上文的思路和决策树，我们来写一下全排列的回溯算法代码（假设给定数组 $nums$ 中不存在重复元素）。则代码如下所示：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []    # 存放所有符合条件结果的集合
        path = []   # 存放当前符合条件的结果
        def backtracking(nums):             # nums 为选择元素列表
            if len(path) == len(nums):      # 说明找到了一组符合条件的结果
                res.append(path[:])         # 将当前符合条件的结果放入集合中
                return

            for i in range(len(nums)):      # 枚举可选元素列表
                if nums[i] not in path:     # 从当前路径中没有出现的数字中选择
                    path.append(nums[i])    # 选择元素
                    backtracking(nums)      # 递归搜索
                    path.pop()              # 撤销选择

        backtracking(nums)
        return res
```

## 3. 回溯算法的通用模板

根据上文全排列的回溯算法代码，我们可以提炼出回溯算法的通用模板，回溯算法的通用模板代码如下所示：

```python
res = []    # 存放所欲符合条件结果的集合
path = []   # 存放当前符合条件的结果
def backtracking(nums):             # nums 为选择元素列表
    if 遇到边界条件:                  # 说明找到了一组符合条件的结果
        res.append(path[:])         # 将当前符合条件的结果放入集合中
        return

    for i in range(len(nums)):      # 枚举可选元素列表
        path.append(nums[i])        # 选择元素
        backtracking(nums)          # 递归搜索
        path.pop()                  # 撤销选择

backtracking(nums)
```

## 4. 回溯算法三步走

网络上给定的回溯算法解题步骤比较抽象，这里只做一下简单介绍。

1. **根据所给问题，定义问题的解空间**：要定义合适的解空间，包括解的组织形式和显约束。
   - **解的组织形式**：将解的组织形式都规范为⼀个 $n$ 元组 ${x_1, x_2 …, x_n}$。
   - **显约束**：对解分量的取值范围的限定，可以控制解空间的大小。
2. **确定解空间的组织结构**：解空间的组织结构通常以解空间树的方式形象地表达，根据解空间树的不同，解空间分为⼦集树、排列树、$m$ 叉树等。
3. **搜索解空间**：按照深度优先搜索策略，根据隐约束（约束函数和限界函数），在解空间中搜索问题的可⾏解或最优解。当发现当 前节点不满⾜求解条件时，就回溯，尝试其他路径。
   - 如果问题只是求可⾏解，则只需设定约束函数即可，如果要求最优解，则需要设定约束函数和限界函数。

这种回溯算法的解题步骤太过于抽象，不利于我们在日常做题时进行思考。其实在递归算法知识的相关章节中，我们根据递归的基本思想总结了递归三步走的书写步骤。同样，根据回溯算法的基本思想，我们也来总结一下回溯算法三步走的书写步骤。

回溯算法的基本思想是：**以深度优先搜索的方式，根据产生子节点的条件约束，搜索问题的解。当发现当前节点已不满足求解条件时，就「回溯」返回，尝试其他的路径。**

那么，在写回溯算法时，我们可以按照这个思想来书写回溯算法，具体步骤如下：

1. **明确所有选择**：画出搜索过程的决策树，根据决策树来确定搜索路径。
2. **明确终止条件**：推敲出递归的终止条件，以及递归终止时的要执行的处理方法。
3. **将决策树和终止条件翻译成代码**：
   1. 定义回溯函数（明确函数意义、传入参数、返回结果等）。
   2. 书写回溯函数主体（给出约束条件、选择元素、递归搜索、撤销选择部分）。
   3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。

### 4.1 明确所有选择

决策树是帮助我们理清搜索过程的一个很好的工具。我们可以画出搜索过程的决策树，根据决策树来帮助我们确定搜索范围和对应的搜索路径。

### 4.2 明确终止条件

回溯算法的终止条件也就是决策树的底层，即达到无法再做选择的条件。

回溯函数的终止条件一般为给定深度、叶子节点、非叶子节点（包括根节点）、所有节点等。并且还要给出在终止条件下的处理方法，比如输出答案，将当前符合条件的结果放入集合中等等。

### 4.3 将决策树和终止条件翻译成代码

在明确所有选择和明确终止条件之后，我们就可以将其翻译成代码了。这一步也可以分为 $3$ 步来做：

1. 定义回溯函数（明确函数意义、传入参数、返回结果等）。
2. 书写回溯函数主体（给出约束条件、选择元素、递归搜索、撤销选择部分）。
3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。

#### 4.3.1 定义回溯函数

在定义回溯函数时，一定要明确递归函数的意义，也就是要明白这个问题的传入参数和全局变量是什么，最终返回的结果是要解决的什么问题。

- **传入参数和全局变量**：是由递归搜索阶段时的「当前状态」来决定的。最好是能通过传入参数和全局变量直接记录「当前状态」。

比如全排列中，`backtracking(nums)` 这个函数的传入参数是 $nums$（可选择的元素列表），全局变量是 $res$（存放所有符合条件结果的集合数组）和 $path$（存放当前符合条件的结果）。$nums$ 表示当前可选的元素，$path$ 用于记录递归搜索阶段的「当前状态」。$res$ 则用来保存递归搜索阶段的「所有状态」。

- **返回结果**：返回结果是在遇到递归终止条件时，需要向上一层函数返回的信息。

一般回溯函数的返回结果都是单个节点或单个数值，告诉上一层函数我们当前的搜索结果是什么即可。

当然，如果使用全局变量来保存「当前状态」的话，也可以不需要向上一层函数返回结果，即返回空结果。比如上文中的全排列。

#### 4.3.2 书写回溯函数主体

根据当前可选择的元素列表、给定的约束条件（例如之前已经出现的数字在接下来要选择的数字中不能再次出现）、存放当前状态的变量，我们就可以写出回溯函数的主体部分了。即：

```python
for i in range(len(nums)):          # 枚举可选元素列表
    if 满足约束条件:                  # 约束条件
        path.append(nums[i])        # 选择元素
        backtracking(nums)          # 递归搜索
        path.pop()                  # 撤销选择
```

#### 4.3.3 明确递归终止条件

这一步其实就是将「4.2 明确终止条件」章节中的递归终止条件和终止条件下的处理方法转换为代码中的条件语句和对应的执行语句。

## 5. 回溯算法的应用

### 5.1 子集

#### 5.1.1 题目链接

- [78. 子集 - 力扣（LeetCode）](https://leetcode.cn/problems/subsets/)

#### 5.1.2 题目大意

**描述**：给定一个整数数组 $nums$，数组中的元素互不相同。

**要求**：返回该数组所有可能的不重复子集。可以按任意顺序返回解集。

**说明**：

- $1 \le nums.length \le 10$。
- $-10 \le nums[i] \le 10$。
- $nums$ 中的所有元素互不相同。

**示例**：

- 示例 1：

```python
输入 nums = [1,2,3]
输出 [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

- 示例 2：

```python
输入：nums = [0]
输出：[[],[0]]
```

#### 5.1.3 解题思路

##### 思路 1：回溯算法

数组的每个元素都有两个选择：选与不选。

我们可以通过向当前子集数组中添加可选元素来表示选择该元素。也可以在当前递归结束之后，将之前添加的元素从当前子集数组中移除（也就是回溯）来表示不选择该元素。

下面我们根据回溯算法三步走，写出对应的回溯算法。

![子集的决策树](https://qcdn.itcharge.cn/images/20220425210640.png)

1. **明确所有选择**：根据数组中每个位置上的元素选与不选两种选择，画出决策树，如上图所示。
2. **明确终止条件**：
   - 当遍历到决策树的叶子节点时，就终止了。即当前路径搜索到末尾时，递归终止。
3. **将决策树和终止条件翻译成代码**：
   1. 定义回溯函数：
      - `backtracking(nums, index):` 函数的传入参数是 $nums$（可选数组列表）和 $index$（代表当前正在考虑元素是 $nums[i]$），全局变量是 $res$（存放所有符合条件结果的集合数组）和 $path$（存放当前符合条件的结果）。
      - `backtracking(nums, index):` 函数代表的含义是：在选择 $nums[index]$ 的情况下，递归选择剩下的元素。
   2. 书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。
      - 从当前正在考虑元素，到数组结束为止，枚举出所有可选的元素。对于每一个可选元素：
        - 约束条件：之前选过的元素不再重复选用。每次从 $index$ 位置开始遍历而不是从 $0$ 位置开始遍历就是为了避免重复。集合跟全排列不一样，子集中 ${1, 2}$ 和 ${2, 1}$ 是等价的。为了避免重复，我们之前考虑过的元素，就不再重复考虑了。
        - 选择元素：将其添加到当前子集数组 $path$ 中。
        - 递归搜索：在选择该元素的情况下，继续递归考虑下一个位置上的元素。
        - 撤销选择：将该元素从当前子集数组 $path$ 中移除。
    ```python
    for i in range(index, len(nums)):   # 枚举可选元素列表
        path.append(nums[i])            # 选择元素
        backtracking(nums, i + 1)       # 递归搜索
        path.pop()                      # 撤销选择
    ```
   3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
      - 当遍历到决策树的叶子节点时，就终止了。也就是当正在考虑的元素位置到达数组末尾（即 $start \ge len(nums)$）时，递归停止。
      - 从决策树中也可以看出，子集需要存储的答案集合应该包含决策树上所有的节点，应该需要保存递归搜索的所有状态。所以无论是否达到终止条件，我们都应该将当前符合条件的结果放入到集合中。

##### 思路 1：代码

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # 存放所有符合条件结果的集合
        path = []  # 存放当前符合条件的结果
        def backtracking(nums, index):          # 正在考虑可选元素列表中第 index 个元素
            res.append(path[:])                 # 将当前符合条件的结果放入集合中
            if index >= len(nums):              # 遇到终止条件（本题）
                return

            for i in range(index, len(nums)):   # 枚举可选元素列表
                path.append(nums[i])            # 选择元素
                backtracking(nums, i + 1)       # 递归搜索
                path.pop()                      # 撤销选择

        backtracking(nums, 0)
        return res
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times 2^n)$，其中 $n$ 指的是数组 $nums$ 的元素个数，$2^n$ 指的是所有状态数。每种状态需要 $O(n)$ 的时间来构造子集。
- **空间复杂度**：$O(n)$，每种状态下构造子集需要使用 $O(n)$ 的空间。

### 5.2 N 皇后

#### 5.2.1 题目链接

- [51. N 皇后 - 力扣（LeetCode）](https://leetcode.cn/problems/n-queens/)

#### 5.2.2 题目大意

**描述**：给定一个整数 $n$。

**要求**：返回所有不同的「$n$ 皇后问题」的解决方案。每一种解法包含一个不同的「$n$ 皇后问题」的棋子放置方案，该方案中的 `Q` 和 `.` 分别代表了皇后和空位。

**说明**：

- **n 皇后问题**：将 $n$ 个皇后放置在 $n \times n$ 的棋盘上，并且使得皇后彼此之间不能攻击。
- **皇后彼此不能相互攻击**：指的是任何两个皇后都不能处于同一条横线、纵线或者斜线上。
- $1 \le n \le 9$。

**示例**：

- 示例 1：

```python
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如下图所示，4 皇后问题存在 2 个不同的解法。
```

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

#### 5.2.3 解题思路

##### 思路 1：回溯算法

这道题是经典的回溯问题。我们可以按照行序来放置皇后，也就是先放第一行，再放第二行 …… 一直放到最后一行。

对于 $n \times n$ 的棋盘来说，每一行有 $n$  列，也就有 $n$ 种放法可供选择。我们可以尝试选择其中一列，查看是否与之前放置的皇后有冲突，如果没有冲突，则继续在下一行放置皇后。依次类推，直到放置完所有皇后，并且都不发生冲突时，就得到了一个合理的解。

并且在放置完之后，通过回溯的方式尝试其他可能的分支。

下面我们根据回溯算法三步走，写出对应的回溯算法。

![](https://qcdn.itcharge.cn/images/20220426095225.png)

1. **明确所有选择**：根据棋盘中当前行的所有列位置上是否选择放置皇后，画出决策树，如上图所示。    
2. **明确终止条件**：
   - 当遍历到决策树的叶子节点时，就终止了。也就是在最后一行放置完皇后时，递归终止。
3. **将决策树和终止条件翻译成代码：**
   1. 定义回溯函数：
      - 首先我们先使用一个 $n \times n$ 大小的二维矩阵 $chessboard$ 来表示当前棋盘，$chessboard$ 中的字符 `Q` 代表皇后，`.` 代表空位，初始都为 `.`。
      - 然后定义回溯函数 `backtrack(chessboard, row): ` 函数的传入参数是 $chessboard$（棋盘数组）和 $row$（代表当前正在考虑放置第 $row$ 行皇后），全局变量是 $res$（存放所有符合条件结果的集合数组）。
      - `backtrack(chessboard, row):` 函数代表的含义是：在放置好第 $row$ 行皇后的情况下，递归放置剩下行的皇后。
   2. 书写回溯函数主体（给出选择元素、递归搜索、撤销选择部分）。
      - 枚举出当前行所有的列。对于每一列位置：
        - 约束条件：定义一个判断方法，先判断一下当前位置是否与之前棋盘上放置的皇后发生冲突，如果不发生冲突则继续放置，否则则继续向后遍历判断。
        - 选择元素：选择 $row, col$ 位置放置皇后，将其棋盘对应位置设置为 `Q`。
        - 递归搜索：在该位置放置皇后的情况下，继续递归考虑下一行。
        - 撤销选择：将棋盘上 $row, col$ 位置设置为 `.`。
    ```python
    # 判断当前位置 row, col 是否与之前放置的皇后发生冲突
    def isValid(self, n: int, row: int, col: int, chessboard: List[List[str]]):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
    
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True
    ```

    ```python
    for col in range(n):                            # 枚举可放置皇后的列
       if self.isValid(n, row, col, chessboard):    # 如果该位置与之前放置的皇后不发生冲突
           chessboard[row][col] = 'Q'               # 选择 row, col 位置放置皇后
           backtrack(row + 1, chessboard)           # 递归放置 row + 1 行之后的皇后
           chessboard[row][col] = '.'               # 撤销选择 row, col 位置
    ```
   3. 明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。
      - 当遍历到决策树的叶子节点时，就终止了。也就是在最后一行放置完皇后（即 $row == n$）时，递归停止。
      - 递归停止时，将当前符合条件的棋盘转换为答案需要的形式，然后将其存入答案数组 $res$ 中即可。

##### 思路 1：代码

```python
class Solution:
    res = []
    def backtrack(self, n: int, row: int, chessboard: List[List[str]]):
        if row == n:
            temp_res = []
            for temp in chessboard:
                temp_str = ''.join(temp)
                temp_res.append(temp_str)
            self.res.append(temp_res)
            return
        for col in range(n):
            if self.isValid(n, row, col, chessboard):
                chessboard[row][col] = 'Q'
                self.backtrack(n, row + 1, chessboard)
                chessboard[row][col] = '.'

    def isValid(self, n: int, row: int, col: int, chessboard: List[List[str]]):
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if chessboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res.clear()
        chessboard = [['.' for _ in range(n)] for _ in range(n)]
        self.backtrack(n, 0, chessboard)
        return self.res
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(n!)$，其中 $n$ 是皇后数量。
- **空间复杂度**：$O(n^2)$，其中 $n$ 是皇后数量。递归调用层数不会超过 $n$，每个棋盘的空间复杂度为 $O(n^2)$，所以空间复杂度为 $O(n^2)$。

## 练习题目

- [0046. 全排列](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/permutations.md)
- [0047. 全排列 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/permutations-ii.md)
- [0022. 括号生成](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/generate-parentheses.md)
- [0017. 电话号码的字母组合](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/letter-combinations-of-a-phone-number.md)
- [0039. 组合总和](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/combination-sum.md)
- [0040. 组合总和 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/combination-sum-ii.md)
- [0078. 子集](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/subsets.md)
- [0090. 子集 II](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/subsets-ii.md)
- [0079. 单词搜索](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/word-search.md)

- [回溯算法题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E9%A2%98%E7%9B%AE)

## 参考资料

- 【题解】[回溯算法入门级详解 + 练习（持续更新） - 全排列 - 力扣](https://leetcode.cn/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/)
- 【题解】[「代码随想录」带你学透回溯算法！51. N-Queens - N 皇后 - 力扣](https://leetcode.cn/problems/n-queens/solution/dai-ma-sui-xiang-lu-51-n-queenshui-su-fa-2k32/)
- 【文章】[回溯算法详解](https://mp.weixin.qq.com/s/trILKSiN9EoS58pXmvUtUQ)
- 【文章】[回溯算法详解修订版 - labuladong](https://github.com/labuladong/fucking-algorithm/blob/master/算法思维系列/回溯算法详解修订版.md)
- 【文章】[【算法】回溯法四步走 - Nemo& - 博客园](https://www.cnblogs.com/blknemo/p/12431911.html)
