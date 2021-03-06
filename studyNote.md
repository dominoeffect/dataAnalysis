课程概述

------------------------------------------------------------------------------

一.欢迎


1.为什么用Python进行数据分析

------------------------------------------------------------------------------

大家好，欢迎大家来学习数据分析入门课程！

在这一周的时间中，我将会带领你了解如何用 Python 进行数据分析。在这个过程中，我们也会学习到 Python 的一些基础知识。Python 是业内使用最广泛的编程语言之一，它是一门非常强大、用途广泛的语言，从网络开发到数据科学，都有它的应用身影。Python 中有一些库能够帮助我们简化数据分析过程，比如 NumPy 和 Pandas，Matplotlib，因此我们的课程中也会主要使用 Python 语言。让我们开始吧！


2.7天课程简介

------------------------------------------------------------------------------

我们需要在7天内挑战一个实战项目，了解使用Python进行数据分析的大致流程。你可能在此之前没有编程基础，但是不要担心，我们将利用最小的知识库，面向项目学习，在实际的应用中帮助你快速构建一个从提出问题到数据导入和评估、数据整理、数据筛选，再到可视化的分析全景。Learning by doing！

为了达到这个目标，我们会让你了解数据分析师工作中要解决的问题，以及数据分析的完整流程。我们也给你准备了 Python 编程的练习题，包括数据结构、循环、函数封装等，同时简单介绍一些数据分析中常用的第三方库，你可以根据需求进行练习。具体的编程内容你将会在后面的正式课程中进行更加系统地学习。

3.学习建议

------------------------------------------------------------------------------

在接下来的课程中，你会了解如何通过运用 Python 编程来解决实际问题。无论你是编程的新手，或者有其他语言的经验，这门课程都能够帮助你完成目标。

如果你是小白
如果你是编程的新手，从未接触过任何编程语言，我们强烈建议你先查看实战项目。

当你看到实战项目中的大段文字描述和代码时，不必慌张。完成该实战项目并不需要太多编程基础，你可以尝试阅读文档描述，运行代码框，观察会出现什么结果，然后再根据前面的知识进行针对性的学习。

有一定基础的同学
如果之前你有 Python 或者其他语言的编程背景，你可以完整查看前面的编程基础部分，完成对应的练习题，对之前的知识进行检测和复习。通过完成实战项目，对数据分析师的日常工作内容有所了解。

4.导师介绍

------------------------------------------------------------------------------

Charlotte Turner 和 Philip Mallory 以及 Juno Lee









首先，学习Python

------------------------------------------------------------------------------

二.数字和字符串

1.算数（从算数开始学习Python）

2.整数和浮点数

3.错误（介绍报错机制）

4.变量I

5.变量II

6.比较运算符

7.字符串I

8.内置函数（len、print...）

9.类型和类型转换

三.数据结构和循环

1.列表I

2.列表II

3.For循环I

4.For循环II

5.While循环

6.其他数据结构（集合、字典、符合数据结构暂未介绍）

四.函数和标准库

1.函数简介

2.定义函数I

3.定义函数II

4.定义函数III

5.默认参数

6.变量作用域

7.标准库（https://docs.python.org/3/library/）
每周新的模块https://pymotw.com/3/

7.1 Python 标准库的各组成部分称为 modules（模块），模块中包含的是对象（函数/类）

7.2 某些 Python 标准库中有很多模块！为了更好地管理代码，它们被分解成包（package）中的子模块（sub-module）。一个包只是一个包含子模块的模块。import可以用于导入模块中的子模块，但是不能导入函数

示例：

import os  #导入模块

import os.path #导入子模块（也就是包）

import os.path.isdir #导入子模块函数，结果是ImportError

from datetime import datetime as dt #从模块中导入类/函数并以dt用户别名


PS：对于代码运行时长的判断，我们倾向于将 timeit 用于短代码，将 cProfile 或 profile 用于较大型的工程

8.密码生成器解决方案

常用标准库模块

csv：非常方便阅读和编写 csv 文件
collections：常用数据类型的有用扩展，包括 OrderedDict、defaultdict 与 namedtuple
random：生成伪随机数，随机打乱顺序，选择随机项
string：更多的字符串功能。此模块还包含诸如 string.digits（一个包含所有有效数字字符的字符串）的有用字母集合。
re：通过正则表达式匹配字符串模式
math：一些标准的数学函数
os：与操作系统交互
os.path ：操作路径名的 os 子模块
sys：直接使用 Python 解释器
json：很适合阅读和编写 json 文件（适合网络工作）

9.第三方库
最受欢迎的第三方库（http://pypi-ranking.info/alltime）

如果 Python 本身不包含这些包，那该如何获取呢？我们可以使用 pip 来安装库，Python 3 自带的一个包管理器。Python 2 用户也使用 pip，但是 Python 2 没有自带，所以必须单独安装。如果同时安装了 Python 2 和 Python 3，每个都具有 pip，可以使用命令 pip2 和 pip3 来进行区分。

pip 是 Python 的标准包管理器，但不是唯一管理器。一个常见选择是专门为数据科学家和类似用户设计的 Anaconda。我们将讲解 pip，因为其属于一般标准。



有用的第三方包

IPython - 一个更好的交互式 Python 解释器
requests - 提供制作 Web 请求的简单方法，用于访问 Web API。
Flask - 用于制作 Web 应用程序和 API 的轻量级框架。
Django - 制作 Web 应用程序的特色框架。Django 特别适用于设计复杂、内容繁重的 Web 应用程序。
Beautiful Soup - 用于解析 HTML 并从中提取信息。尤其适用于网络抓取。
pytest - 扩展 Python 的内置断言（assertion）和 unittest 模块。
PyYAML - 用于阅读和编写 YAML 文件。
NumPy - 使用 Python 进行科学计算的基础包，除了其他功能之外，其还包含强大的 N 维数组对象和有用的线性代数功能。
pandas - 一个包含高表现力、数据结构和数据分析工具的库。尤其是：pandas 提供了 DataFrame 数据结构！
matplotlib - 一个 2D 绘图库，用于在交互式环境中生成各种硬拷贝格式的出版物质量图。
ggplot - 另一个 2D 绘图库，基于 R 的 ggplot2 库。
Pillow - Python 影像库使你的 Python 解释器新增图像处理功能。
pyglet - 用于游戏开发的跨平台应用程序框架。
Pygame - 用于编写游戏的 Python 模块集合。
pytz - Python 中的世界时区定义


requirements.txt

较大的 Python 程序可能依赖几十个第三方包。为了更容易共享这些程序，程序员通常会在一个名为 requirements.txt 的文件中列出项目的依赖项。这是一个 requirements.txt 文件的示例：

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1


大家可以使用 pip，通过以下命令一次安装项目的所有依赖项：

$ pip3 install -r requirements.txt

10.使用在线资源


然后，学习数据分析过程

------------------------------------------------------------------------------

五.数据分析过程

1.数据分析初探

我们在上面已经学习了一些Python的基础编程知识，接下来会由Juno Lee讲师给大家讲述一下数据分析师的工作和对一个数据进行分析的完整流程，以及在数据分析中常用的一些包。

2.数据分析师解决的问题

高质量的数据分析，可以使我们获得非常有价值的结果！

数据分析的应用
Facebook 博文(需科学上网) 与论文 包含不同意识形态的信息
OkCupid 博文，解释关于第一次约会时可提的最佳问题
文章，分析沃尔玛如何使用大数据分析来增加销量
维基百科页面，解释 Bill James 如何将数据分析应用于棒球
Numerate 博文，解释如何使用数据分析来设计药物

3.数据分析过程概述

我们将数据分析过程组织为五个步骤：提问、整理、探索、得出结论和传达结果。以下是关键要点的概述，但你可以选择跳过。我们将在后面的部分中演练每一步，所以你将很快熟悉整个过程。

第 1 步：提问
你要么获取一批数据，然后根据它提问，要么先提问，然后根据问题收集数据。在这两种情况下，好的问题可以帮助你将精力集中在数据的相关部分，并帮助你得出有洞察力的分析。

第 2 步：整理数据
你通过三步来获得所需的数据：收集，评估，清理。你收集所需的数据来回答你的问题，评估你的数据来识别数据质量或结构中的任何问题，并通过修改、替换或删除数据来清理数据，以确保你的数据集具有最高质量和尽可能结构化。

第 3 步：执行 EDA（探索性数据分析）
你可以探索并扩充数据，以最大限度地发挥你的数据分析、可视化和模型构建的潜力。探索数据涉及在数据中查找模式，可视化数据中的关系，并对你正在使用的数据建立直觉。经过探索后，你可以删除异常值，并从数据中创建更好的特征，这称为特征工程。

第 4 步：得出结论（或甚至是做出预测）
这一步通常使用机器学习或推理性统计来完成，不在本课程范围内，本课的重点是使用描述性统计得出结论。

第 5 步：传达结果
你通常需要证明你发现的见解及传达意义。或者，如果你的最终目标是构建系统，则通常需要分享构建的结果，解释你得出设计结论的方式，并报告该系统的性能。传达结果的方法有多种：报告、幻灯片、博客帖子、电子邮件、演示文稿，甚至对话。数据可视化总会给你呈现很大的价值。

在使用 Python 对真实数据集执行每个步骤之前，让我们来熟悉每一步！

4.数据分析过程练习

Kaggle的共享单车需求（https://www.kaggle.com/c/bike-sharing-demand）

特征	      描述
日期时间	  小时 + 时间戳
季节	      1 = 春季、2 = 夏季、3 = 秋季、4 = 冬季
假期	      该天是否为假日
工作日	  该天是否既不是周末，也不是假日
天气 *	  1、2、3、4（参见下面的描述）
温度	      摄氏度温度
环境温度	  "感觉"温度（摄氏度）
湿度	      相对湿度
风速	      风速
游客	      非注册用户所发起租赁的数量
会员	      注册用户所发起租赁的数量
总计	      总租赁数量


* 天气特征关键字
1 = 晴朗、少云、局部多云

2 = 薄雾 + 多云、薄雾 + 碎云、薄雾 + 少云、薄雾

3 = 小雪、小雨 + 雷雨 + 散云、小雨 + 散云

4 = 大雨 + 冰粒 + 雷雨 + 薄雾、雪 + 大雾	


A.提问步骤

给出上面有可能影响每小时租用自行车数量的变量数据，可以提出哪些相关问题？

1.哪些属性在预测租用自行车的数量方面最为重要？

2.如果目标是使整个星期的租用数量呈现平稳状态，共享单车公司应该在一周中的哪天开展促销活动？

B.整理步骤

在继续分析前，可以看到此 Kaggle 单车共享数据有何需要解决的潜在问题？

1.日期未采用日期格式

2.一些缺失值

3.温度值远远超出了地球上的现实范围

PS 数据类型不正确、数据丢失和数据不准确都是我们在分析数据之前需要解决的问题。

C.探索步骤

制作可视化图表

1.例图：散点图

根据图表分析

1.找出数据间的相关性，本例中确定温度可能最有助于预测自行车租赁的数量。

D.得出结论步骤

本例中通过温度预测新增租用数量，由于相关性并不那么强，所以这种预测可能会很弱。
然而，如果这个散点图是我们唯一可用的猜测工具，那么最佳拟合线将是一个好的起点。

E.传达结果步骤

你从共享单车数据中所得出结论的有效方法有哪些？

（X）温度与湿度等特征的相关性散点图
一份书面报告，详细说明了预测自行车租赁量的最重要变量
（X）不同温度的回归方程图

解释在预测自行车租赁计数时要考虑的最重要的特征，将会解决我们对该数据集提出的问题，而书面报告将是完整传达这些结果的一种方式。

5.数据分析中的常用包概述

包就是一些可导入代码的模块或Python文件的集合

你可以把包想象成充满类和函数的库

Numpy能让你使用数学函数高效处理庞大的多维数组和矩阵

Pandas像是强大灵活的Excel，能够处理大量的数据

Matplotlib则是个绘画库，通常使用几行代码就能创建极好的可视化界面

6.包概述练习





















