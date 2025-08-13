## 1. LeetCode 是什么

**「LeetCode」** 是一个在线编程评测平台，主要包含算法、数据库、Shell、多线程等题目，其中以算法题目为主。LeetCode 上有 $3000+$ 道编程问题，支持 $16+$ 种编程语言，还有一个活跃的社区用于技术交流。我们可以通过解决 LeetCode 题库中的问题来练习编程技能，以及提高算法能力。

许多知名互联网公司在面试时会考察 LeetCode 题目，要求面试者分析问题、编写代码，并分析算法的时间复杂度和空间复杂度。通过 LeetCode 刷题，充分准备算法知识，对获得好的工作机会很有帮助。

## 2. LeetCode 新手入门

### 2.1 LeetCode 注册

1. 打开 LeetCode 中文主页，链接：[力扣（LeetCode）官网](https://leetcode.cn/)。
2. 输入手机号，获取验证码。
3. 输入验证码之后，点击「登录 / 注册」，就注册好了。

![LeetCode 注册页面](https://qcdn.itcharge.cn/images/20210901155409.png)

### 2.2 LeetCode 题库

「[题库](https://leetcode.cn/problemset/algorithms/)」是 LeetCode 上最直接的练习入口，在这里可以根据题目的标签、难度、状态进行刷题。也可以按照随机一题开始刷题。

![LeetCode 题库页面](https://qcdn.itcharge.cn/images/20210901155423.png)

#### 2.2.1 题目标签

LeetCode 的题目涉及了许多算法和数据结构。有贪心，搜索，动态规划，链表，二叉树，哈希表等等，可以通过选择对应标签进行专项刷题，同时也可以看到对应专题的完成度情况。

![LeetCode 题目标签](https://qcdn.itcharge.cn/images/20210901155435.png)

#### 2.2.2 题目列表

LeetCode 提供了题目的搜索过滤功能。可以筛选相关题单、不同难易程度、题目完成状态、不同标签的题目。还可以根据题目编号、题解数目、通过率、难度、出现频率等进行排序。

![LeetCode 题目列表](https://qcdn.itcharge.cn/images/20210901155450.png)

#### 2.2.3 当前进度

当前进度提供了一个直观的进度展示。在这里可以看到自己的练习概况。进度会自动展现当前的做题情况。也可以点击「[进度设置](https://leetcode.cn/session/)」创建新的进度，在这里还可以修改、删除相关的进度。

![LeetCode 当前进度](https://qcdn.itcharge.cn/images/20210901155500.png)

#### 2.2.4 题目详情

从题目列表点击进入，就可以看到这道题目的内容描述和代码编辑器。在这里还可以查看相关的题解和自己的提交记录。

![LeetCode 题目详情](https://qcdn.itcharge.cn/images/20210901155529.png)

### 2.3 LeetCode 刷题语言

面试时考察的是算法基本功，对于语言的选择没有限制。建议使用熟悉的语言或语法简洁的语言刷题。

相对于 Python 而言，C、C++ 语法比较复杂，在做题的时候除了要思考思路，还得考虑语法，不太利于刷题。Python 等语言更简洁，能让你专注于算法思路本身，提高刷题效率。当然，算法竞赛选手通常使用 C++，已经成为传统了。

> 人生苦短，我用 Python。

### 2.4 LeetCode 刷题流程

在「2.2.1 题目标签」中我们介绍了题目的相关情况。

![LeetCode 题目详情](https://qcdn.itcharge.cn/images/20210901155529.png)

可以看到左侧区域为题目内容描述区域，还可以看到题目的内容描述和一些示例数据。而右侧是代码编辑区域，代码编辑区域里边默认显示了待实现的方法。

我们需要在代码编辑器中根据方法给定的参数实现对应的算法，并返回题目要求的结果。然后还要经过「执行代码」测试结果，点击「提交」后，显示执行结果为「**通过**」时，才算完成一道题目。

![LeetCode 提交记录](https://qcdn.itcharge.cn/images/20210901155545.png)

总结一下我们的刷题流程为：

1. 在 LeetCode 题库中选择一道自己想要解决的题目。
2. 查看题目左侧的题目描述，理解题目要求。
3. 思考解决思路，并在右侧代码编辑区域实现对应的方法，并返回题目要求的结果。
4. 如果实在想不出解决思路，可以查看题目相关的题解，努力理解他人的解题思路和代码。
5. 点击「执行代码」按钮测试结果。
   - 如果输出结果与预期结果不符，则回到第 3 步重新思考解决思路，并改写代码。
6. 如果输出结果与预期符合，则点击「提交」按钮。
   - 如果执行结果显示「编译出错」、「解答错误」、「执行出错」、「超出时间限制」、「超出内存限制」等情况，则需要回到第 3 步重新思考解决思路，或者思考特殊数据，并改写代码。
7. 如果执行结果显示「通过」，恭喜你通过了这道题目。

接下来我们将通过「[2235. 两整数相加 - 力扣（LeetCode）](https://leetcode.cn/problems/add-two-integers/)」这道题目来讲解如何在 LeetCode 上刷题。

### 2.5 LeetCode 第一题

#### 2.5.1 题目链接

- [2235. 两整数相加 - 力扣（LeetCode）](https://leetcode.cn/problems/add-two-integers/)

#### 2.5.2 题目大意

**描述**：给定两个整数 $num1$ 和 $num2$。

**要求**：返回这两个整数的和。

**说明**：

- $-100 \le num1, num2 \le 100$。

**示例**：

- 示例 1：

```python
输入：num1 = 12, num2 = 5
输出：17
解释：num1 是 12，num2 是 5，它们的和是 12 + 5 = 17，因此返回 17。
```

- 示例 2：

```python
输入：num1 = -10, num2 = 4
输出：-6
解释：num1 + num2 = -6，因此返回 -6。
```

#### 2.5.3 解题思路

##### 思路 1：直接计算

1. 直接计算整数 $num1$ 与 $num2$ 的和，返回 $num1 + num2$ 即可。

##### 思路 1：代码

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。


理解了上面这道题的题意，就可以试着自己编写代码，并尝试提交通过。如果提交结果显示「通过」，那么恭喜你完成了 LeetCode 上的第一题。虽然只是一道题，但这意味着刷题计划的开始！希望你能坚持下去，得到应有的收获。

## 3. LeetCode 刷题攻略

### 3.1 LeetCode 前期准备

如果你是算法和数据结构的新手，建议在刷 LeetCode 之前先学习一下基础知识，这样刷题时会更顺利。

基础知识包括：
- **数据结构**：数组、字符串、链表、树（如二叉树）等。
- **算法**：分治、贪心、回溯、动态规划等。

这个阶段推荐看一些经典的算法基础书来进行学习。这里推荐一下我看过的感觉不错的算法书： 

- 【书籍】[算法（第 4 版）- 谢路云 译](https://book.douban.com/subject/19952400/)
- 【书籍】[大话数据结构 - 程杰 著](https://book.douban.com/subject/6424904/) 
- 【书籍】[趣学算法 - 陈小玉 著](https://book.douban.com/subject/27109832/)
- 【书籍】[算法图解 - 袁国忠 译](https://book.douban.com/subject/26979890/)
- 【书籍】[算法竞赛入门经典（第 2 版） - 刘汝佳 著](https://book.douban.com/subject/25902102/)
- 【书籍】[数据结构与算法分析 - 冯舜玺 译](https://book.douban.com/subject/1139426/)
- 【书籍】[算法导论（原书第 3 版） - 殷建平 / 徐云 / 王刚 / 刘晓光 / 苏明 / 邹恒明 / 王宏志 译](https://book.douban.com/subject/20432061/)

当然，也可以直接看我写的「算法通关手册」，欢迎指正和提出建议，万分感谢。

- 「算法通关手册」GitHub 地址：[https://github.com/itcharge/AlgoNote](https://github.com/itcharge/AlgoNote)
- 「算法通关手册」电子书网站地址：[https://algo.itcharge.cn](https://algo.itcharge.cn)

### 3.2 LeetCode 刷题顺序

讲个笑话，从前有个人以为 LeetCode 的题目是按照难易程度排序的，所以他从 [1. 两数之和](https://leetcode.cn/problems/two-sum) 开始刷题，结果他卡在了 [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays) 这道困难题上。

LeetCode 的题目序号并不是按难易程度排序的，不建议按序号顺序刷题。新手建议从「简单」难度开始，熟练后再刷中等难度题目，最后考虑面试题或难题。

其实 LeetCode 官方网站上就有整理好的题目不错的刷题清单。链接为：[https://leetcode.cn/leetbook/](https://leetcode.cn/leetbook/)。可以先刷这里边的题目卡片。我这里也做了一个整理。

推荐刷题顺序和目录如下：

[1. 初级算法](https://leetcode.cn/leetbook/detail/top-interview-questions-easy/)、[2. 数组类算法](https://leetcode.cn/leetbook/detail/all-about-array/)、[3. 数组和字符串](https://leetcode.cn/leetbook/detail/array-and-string/)、[4. 链表类算法](https://leetcode.cn/leetbook/detail/linked-list/)、[5. 哈希表](https://leetcode.cn/leetbook/detail/hash-table/)、[6. 队列 & 栈](https://leetcode.cn/leetbook/detail/queue-stack/)、[7. 递归](https://leetcode.cn/leetbook/detail/recursion/)、[8. 二分查找](https://leetcode.cn/leetbook/detail/binary-search/)、[9. 二叉树](https://leetcode.cn/leetbook/detail/data-structure-binary-tree/)、[10. 中级算法](https://leetcode.cn/leetbook/detail/top-interview-questions-medium/)、[11. 高级算法](https://leetcode.cn/leetbook/detail/top-interview-questions-hard/)、[12. 算法面试题汇总](https://leetcode.cn/leetbook/detail/top-interview-questions/)。

当然还可以通过官方推出的「[学习计划 - 力扣](https://leetcode.cn/study-plan/)」按计划每天刷题。

或者直接按照我整理的分类刷题列表进行刷题：

- LeetCode 分类刷题列表：[点击打开「LeetCode 分类刷题列表」](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md)

正在准备面试、没有太多时间刷题的小伙伴，可以按照我总结的「LeetCode 面试最常考 100 题」、「LeetCode 面试最常考 200 题」进行刷题。

> **说明**：「LeetCode 面试最常考 100 题」、「LeetCode 面试最常考 200 题」是笔者根据「[CodeTop 企业题库](https://codetop.cc/home)」按频度从高到低进行筛选，并且去除了一部分 LeetCode 上没有的题目和重复题目后得到的题目清单。

- [LeetCode 面试最常考 100 题](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_07_interview_100_list.md)
- [LeetCode 面试最常考 200 题](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_08_interview_200_list.md)

### 3.3 LeetCode 刷题技巧

下面分享一下我在刷题过程中用到的刷题技巧。简单来说，可以分为 $5$ 条：

> 1. 五分钟思考法
> 2. 重复刷题
> 3. 按专题分类刷题
> 4. 写解题报告
> 5. 坚持刷题

#### 3.3.1 五分钟思考法

> **五分钟思考法**：如果一道题如果 $5$ 分钟之内有思路，就立即动手写代码解题。如果 $5$ 分钟之后还没有思路，就直接去看题解。然后根据题解的思路，自己去实现代码。如果发现自己看了题解也无法实现代码，就认真阅读题解的代码，并理解代码的逻辑。

其实，刷算法题的过程和背英语单词很相似。

刚开始学英语时，先从最基础的字母学起，不必纠结每个字母的由来。接着学习简单的单词，也不用深究单词的含义，先记住再说。掌握了基础词汇后，再逐步学习词组、短句、长句，最后阅读文章。

背单词不是看一遍就能记住，而是需要不断重复练习、反复记忆来加深印象。

刷算法题也是如此。零基础时，不要纠结为什么自己想不出解法，或者为什么没想到更高效的方法。遇到没有思路的题目时，直接去看题解区的高赞解答，尽快积累经验，帮助自己快速入门。

#### 3.3.2 重复刷题

> **重复刷题**：遇见不会的题，多刷几遍，不断加深理解。

刷算法题经常是做完一遍后，隔一段时间就忘记了，看到之前做过的题目也未必能立刻想起解题思路。所以，刷题并不是做完一遍就结束了，还需要定期回顾和复习。

此外，一道题往往有多种解法和不同的优化思路。第一次做时可能只想到一种方法，等到第二遍、第三遍时，可能会发现新的解法或更优的实现。

因此，建议对不会的题目多刷几遍，通过反复练习不断加深理解和记忆。

#### 3.3.3 按专题分类刷题

> **按专题分类刷题**：按照不同专题分类刷题，既可以巩固刚学完的算法知识，还可以提高刷题效率。

按专题分类刷题有两个好处：

1. **巩固知识**：刚学完某个算法时，可能对里边的相关知识理解的不够透彻，或者说可能会遗漏一些关键知识点，这时候可以通过刷对应题目的方式来帮助我们巩固刚学完的算法知识。
2. **提高效率**：同类题目所用到的算法知识其实是相同或者相似的，同一种解题思路可以运用到多道题目中。通过不断求解同一类算法专题下的题目，可以大大的提升我们的刷题速度。

####  3.3.4 写解题报告

> **写解题报告**：如果能够用简洁清晰的语言让别人听懂这道题目的思路，那就说明你真正理解了这道题的解法。

写解题报告是很有用的技巧。如果你能用通俗易懂的语言写出解题思路，说明你真正理解了这道题。这相当于「费曼学习法」，也能减少重复刷题的时间。

#### 3.3.5 坚持刷题

> **坚持刷题**：算法刷题没有捷径，只有不断的刷题、总结，再刷题，再总结。

千万不要相信「3天精通数据结构」这类速成学习宣传。学习算法需要不断积累，反复理解算法思想，并通过刷题来应用知识。

根据我的个人经验，能坚持每天刷题并掌握基础算法知识的人总是少数。但如果你选择了学习算法，希望在达成目标前能坚持下去，通过「刻意练习」把刷题变成兴趣。

## 4. 总结

LeetCode 是一个在线编程练习平台，主要用于提升算法和编程能力。新手可以从简单题目开始，逐步学习数据结构和算法。

刷题技巧包括：五分钟思考法、重复刷题、按专题分类刷题、写解题报告、坚持刷题。最重要的是坚持，通过不断练习和总结来掌握算法知识。

## 练习题目

- [2235. 两整数相加](https://github.com/itcharge/AlgoNote/tree/main/docs/solutions/2200-2299/add-two-integers.md)
- [1929. 数组串联](https://github.com/itcharge/AlgoNote/tree/main/docs/solutions/1900-1999/concatenation-of-array.md)

## 参考资料

- 【文章】[What is LeetCode? - Quora](https://www.quora.com/What-is-Leetcode)
- 【文章】[LeetCode 帮助中心 - 力扣（LeetCode）](https://support.leetcode-cn.com/hc/)
- 【回答】[刷 leetcode 使用 python 还是 c++？ - 知乎](https://www.zhihu.com/question/319448129)
- 【回答】[刷完 LeetCode 是什么水平？能拿到什么水平的 offer？ - 知乎](https://www.zhihu.com/question/32019460)

