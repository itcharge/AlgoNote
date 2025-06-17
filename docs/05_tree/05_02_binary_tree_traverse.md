## 1. 二叉树的遍历简介

> **二叉树的遍历**：指的是从根节点出发，按照某种次序依次访问二叉树中所有节点，使得每个节点被访问一次且仅被访问一次。

在二叉树的一些实际问题中，经常需要按照一定顺序对二叉树中每个节点逐个进行访问一次，用以查找具有某一特点的节点或者全部节点，然后对这些满足要求的节点进行处理。这里所说的「访问」就是指对该节点进行某种操作，例如：依次输出节点的数据信息、统计满足某条件的节点总数等等。

回顾二叉树的递归定义可以知道，二叉树是由根节点和左子树、右子树构成的。因此，如果能依次遍历这 $3$ 个部分，就可以遍历整个二叉树。

如果利用深度优先搜索的方式，并且根据访问顺序次序的不同，我们可以分为 $6$ 种遍历方式，而如果限制先左子树后右子树的遍历顺序，则总共有 $3$ 种遍历方式：分别为 **「二叉树的前序遍历」**、**「二叉树的中序遍历」** 和 **「二叉树的后续遍历」**。

而如果使用广度优先搜索的方式，则可以按照层序方式（按照层次从上至下，每一层从左至右）对二叉树进行遍历，这种方式叫做 **「二叉树的层序遍历」**。

## 2. 二叉树的前序遍历

> 二叉树的前序遍历规则为：
>
> - 如果二叉树为空，则返回。
> - 如果二叉树不为空，则：
>   1. 访问根节点。
>   2. 以前序遍历的方式遍历根节点的左子树。
>   3. 以前序遍历的方式遍历根节点的右子树。

从二叉树的前序遍历规则可以看出：前序遍历过程是一个递归过程。在遍历任何一棵子树时仍然是按照先访问根节点，然后遍历子树根节点的左子树，最后再遍历子树根节点的右子树的顺序进行遍历。

如下图所示，该二叉树的前序遍历顺序为：$A - B - D - H - I - E - C - F - J - G - K$。

![二叉树的前序遍历](https://qcdn.itcharge.cn/images/20240511171628.png)

### 2.1 二叉树的前序遍历递归实现

二叉树的前序遍历递归实现步骤为：

1. 判断二叉树是否为空，为空则直接返回。
2. 先访问根节点。
3. 然后递归遍历左子树。
4. 最后递归遍历右子树。

二叉树的前序遍历递归实现代码如下：

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res
```

### 2.2 二叉树的前序遍历显式栈实现

二叉树的前序遍历递归实现的过程，实际上就是调用系统栈的过程。我们也可以使用一个显式栈 $stack$ 来模拟递归的过程。

前序遍历的顺序为：根节点 - 左子树 - 右子树，而根据栈的「先入后出」特点，所以入栈的顺序应该为：先放入右子树，再放入左子树。这样可以保证最终遍历顺序为前序遍历顺序。 

二叉树的前序遍历显式栈实现步骤如下：

1. 判断二叉树是否为空，为空则直接返回。
2. 初始化维护一个栈，将根节点入栈。
3. 当栈不为空时：
   1. 弹出栈顶元素 $node$，并访问该元素。
   2. 如果 $node$ 的右子树不为空，则将 $node$ 的右子树入栈。
   3. 如果 $node$ 的左子树不为空，则将 $node$ 的左子树入栈。

 二叉树的前序遍历显式栈实现代码如下：

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                        # 二叉树为空直接返回
            return []
            
        res = []
        stack = [root]

        while stack:                        # 栈不为空
            node = stack.pop()              # 弹出根节点
            res.append(node.val)            # 访问根节点
            if node.right:
                stack.append(node.right)    # 右子树入栈
            if node.left:
                stack.append(node.left)     # 左子树入栈

        return res
```

## 3. 二叉树的中序遍历

> 二叉树的中序遍历规则为：
>
> - 如果二叉树为空，则返回。
> - 如果二叉树不为空，则：
>   1. 以中序遍历的方式遍历根节点的左子树。
>   2. 访问根节点。
>   3. 以中序遍历的方式遍历根节点的右子树。

从二叉树的中序遍历规则可以看出：中序遍历过程也是一个递归过程。在遍历任何一棵子树时仍然是按照先遍历子树根节点的左子树，然后访问根节点，最后再遍历子树根节点的右子树的顺序进行遍历。

如下图所示，该二叉树的中序遍历顺序为：$H - D - I - B - E - A - F - J - C - K - G$。

![二叉树的中序遍历](https://qcdn.itcharge.cn/images/20240511171643.png)

### 3.1 二叉树的中序遍历递归实现

二叉树的中序遍历递归实现步骤为：

1. 判断二叉树是否为空，为空则直接返回。
2. 先递归遍历左子树。
3. 然后访问根节点。
4. 最后递归遍历右子树。

二叉树的中序遍历递归实现代码如下：

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
```

### 3.2 二叉树的中序遍历显式栈实现

我们可以使用一个显式栈 $stack$ 来模拟二叉树的中序遍历递归的过程。

与前序遍历不同，访问根节点要放在左子树遍历完之后。因此我们需要保证：**在左子树访问之前，当前节点不能提前出栈**。

我们应该从根节点开始，循环遍历左子树，不断将当前子树的根节点放入栈中，直到当前节点无左子树时，从栈中弹出该节点并进行处理。

然后再访问该元素的右子树，并进行上述循环遍历左子树的操作。这样可以保证最终遍历顺序为中序遍历顺序。

二叉树的中序遍历显式栈实现步骤如下：

1. 判断二叉树是否为空，为空则直接返回。
2. 初始化维护一个空栈。
3. 当根节点或者栈不为空时：
   1. 如果当前节点不为空，则循环遍历左子树，并不断将当前子树的根节点入栈。
   1. 如果当前节点为空，说明当前节点无左子树，则弹出栈顶元素 $node$，并访问该元素，然后尝试访问该节点的右子树。

 二叉树的中序遍历显式栈实现代码如下：

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:                # 二叉树为空直接返回
            return []
        
        res = []
        stack = []

        while root or stack:        # 根节点或栈不为空
            while root:             
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left    # 找到最左侧节点
            
            node = stack.pop()      # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            res.append(node.val)    # 访问该节点
            root = node.right       # 尝试访问该节点的右子树
        return res
```

## 4. 二叉树的后序遍历

> 二叉树的后序遍历规则为：
>
> - 如果二叉树为空，则返回。
> - 如果二叉树不为空，则：
>   1. 以后序遍历的方式遍历根节点的左子树。
>   2. 以后序遍历的方式遍历根节点的右子树。
>   3. 访问根节点。

从二叉树的后序遍历规则可以看出：后序遍历过程也是一个递归过程。在遍历任何一棵子树时仍然是按照先遍历子树根节点的左子树，然后遍历子树根节点的右子树，最后再访问根节点的顺序进行遍历。

如下图所示，该二叉树的后序遍历顺序为：$H - I - D - E - B - J - F - K - G - C - A$。

![二叉树的后序遍历](https://qcdn.itcharge.cn/images/20240511171658.png)

### 4.1 二叉树的后序遍历递归实现

二叉树的后序遍历递归实现步骤为：

1. 判断二叉树是否为空，为空则直接返回。
2. 先递归遍历左子树。
3. 然后递归遍历右子树。
4. 最后访问根节点。

二叉树的后序遍历递归实现代码如下：

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res
```

### 4.2 二叉树的后序遍历显式栈实现

我们可以使用一个显式栈 $stack$ 来模拟二叉树的后序遍历递归的过程。

与前序、中序遍历不同，在后序遍历中，根节点的访问要放在左右子树访问之后。因此，我们要保证：**在左右孩子节点访问结束之前，当前节点不能提前出栈**。

我们应该从根节点开始，先将根节点放入栈中，然后依次遍历左子树，不断将当前子树的根节点放入栈中，直到遍历到左子树最左侧的那个节点，从栈中弹出该元素，并判断该元素的右子树是否已经访问完毕，如果访问完毕，则访问该元素。如果未访问完毕，则访问该元素的右子树。

二叉树的后序遍历显式栈实现步骤如下：

1. 判断二叉树是否为空，为空则直接返回。
2. 初始化维护一个空栈，使用 $prev$ 保存前一个访问的节点，用于确定当前节点的右子树是否访问完毕。
3. 当根节点或者栈不为空时，从当前节点开始：
   1. 如果当前节点有左子树，则不断遍历左子树，并将当前根节点压入栈中。
   2. 如果当前节点无左子树，则弹出栈顶元素 $node$。
   2. 如果栈顶元素 $node$ 无右子树（即 `not node.right`）或者右子树已经访问完毕（即 `node.right == prev`），则访问该元素，然后记录前一节点，并将当前节点标记为空节点。
   2. 如果栈顶元素有右子树，则将栈顶元素重新压入栈中，继续访问栈顶元素的右子树。

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev = None                 # 保存前一个访问的节点，用于确定当前节点的右子树是否访问完毕
        
        while root or stack:        # 根节点或栈不为空
            while root:
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left    # 继续访问左子树，找到最左侧节点

            node = stack.pop()      # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出

            # 如果当前节点无右子树或者右子树访问完毕
            if not node.right or node.right == prev:
                res.append(node.val)# 访问该节点
                prev = node         # 记录前一节点
                root = None         # 将当前根节点标记为空
            else:
                stack.append(node)  # 右子树尚未访问完毕，将当前节点重新压回栈中
                root = node.right   # 继续访问右子树
                
        return res
```

## 5. 二叉树的层序遍历

> 二叉树的层序遍历规则为：
>
> - 如果二叉树为空，则返回。
> - 如果二叉树不为空，则：
>   1. 先依次访问二叉树第 $1$ 层的节点。
>   2. 然后依次访问二叉树第 $2$ 层的节点。
>   3. ……
>   4. 依次下去，最后依次访问二叉树最下面一层的节点。

从二叉树的层序遍历规则可以看出：遍历过程是一个广度优先搜索过程。在遍历的时候是按照第 $1$ 层、第 $2$ 层、…… 最后一层依次遍历的，而同一层节点则是按照从左至右的顺序依次访问的。

如下图所示，该二叉树的后序遍历顺序为：$A - B - C - D - E - F - G - H - I - J - K$。

![二叉树的层序遍历](https://qcdn.itcharge.cn/images/20240511175431.png)

二叉树的层序遍历是通过队列来实现的。具体步骤如下：

1. 判断二叉树是否为空，为空则直接返回。
2. 令根节点入队。
3. 当队列不为空时，求出当前队列长度 $s_i$。
4. 依次从队列中取出这 $s_i$ 个元素，并对这 $s_i$ 个元素依次进行访问。然后将其左右孩子节点入队，然后继续遍历下一层节点。
5. 当队列为空时，结束遍历。

二叉树的层序遍历代码实现如下：

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        order = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if level:
                order.append(level)
        return order
```

## 参考资料

1. 【书籍】数据结构教程 第 3 版 - 唐发根 著
2. 【书籍】大话数据结构 程杰 著
3. 【书籍】算法训练营 陈小玉 著
3. 【题解】[LeetCode 二叉树前序遍历（递归法 + 非递归法）- 二叉树的前序遍历 - 力扣](https://leetcode.cn/problems/binary-tree-preorder-traversal/solution/acm-xuan-shou-tu-jie-leetcode-er-cha-shu-pqpz/)
3. 【题解】[二叉树遍历通解（递归和迭代解法）- 完全模拟递归 - 二叉树的后序遍历 - 力扣](https://leetcode.cn/problems/binary-tree-postorder-traversal/solution/bian-li-tong-jie-by-long_wotu/)
3. 【题解】[迭代后序遍历 - 二叉树的后序遍历 - 力扣](https://leetcode.cn/problems/binary-tree-postorder-traversal/solution/die-dai-hou-xu-bian-li-by-wang-mo-ji-98ob/)
