# Python金融量化
专注于分享Python在金融领域的应用，欢迎关注微信公众号Python金融量化 （id：tkfy920）

公众号“Python金融量化”已走过两个年头。这一路走来非常感谢读者的支持，尤其是知识星球圈友，你们的知识付费是我坚持走原创输出的动力。学习是一个循序渐进的过程，只有通过不断的总结才能形成系统的知识框架。通过对两年来发布的60篇原创文章进行梳理，归纳成四个大的部分，包括Python入门篇 、金融数据篇、量化分析篇和策略回测篇 ，形成了较为完整的框架体系。本公众号文章的最大特色是以金融场景+案例形式切入，分享Python在金融量化领域的应用，实战性强，为在校经管类学生和金融从业者提供了丰富的实践分析案例。


01Python入门篇


这一部分主要是关于Python金融量化入门学习路径、量化资源，以及numpy、pandas、matplotlib等量化常用库的入门和应用。Python的编译软件有很多，个人建议安装Anaconda，自带Jupyter notebook和Spyder，其中Jupyter在交互式编程与数据分析上功能十分强大，公众号上所有文章都是基于Jupyter写的。

首先，结合个人经验分享Python金融量化的学习路径，以及分享Python从入门、进阶、到高阶的学习资料，以及金融投资相关书籍（PDF）。

1.1【Python金融量化】零基础如何开始学？

1.2【推荐收藏】倾心整理的Python量化资源大合集

其次，关于Numpy（数组矩阵）、Pandas（数据处理分析）、Matplotlib（可视化）、Seaborn（可视化）、Sklearn（机器学习）等金融量化常用库的入门和应用。

1.3【手把手教你】玩转Python量化金融工具之NumPy

1.4【手把手教你】玩转Python金融量化利器之Pandas

1.5【建议收藏】Matplotlib可视化最有价值的50张图

1.6【手把手教你】Seaborn在金融数据可视化中的应

1.7【手把手教你】玩转机器学习 Sklearn

02金融数据篇


本部分主要是使用Python获取股票行情、上市公司基本面、宏观经济以及财经新闻等数据，对其进行可视化分析，以及使用Postgresql （sqlite3）搭建本地量化分析数据库。

2.1【手把手教你】Python获取交易数据

2.2【Python金融量化】上市公司知多少？

2.3 Python量化选股初探

2.4 2018你不可不知的十大关键词

2.5【手把手教你】Python获取财经数据和可视化分析

2.6【文本挖掘】Python带你笑看江湖

2.7【Python金融量化】财经新闻文本分析

2.8【手把手教你】搭建自己的量化分析数据库

2.9【手把手教你】Python面向对象编程入门及股票数据管理应用实例

03量化分析篇


本部分涉及内容比较多，包括使用Python做金融统计分析、蒙特卡洛模拟，时间序列建模，Talib技术分析、投资组合以及多因子模型分析等。

A股数据探索性分析：

3.1【Python量化】股票分析入门

3.2 A股指数图谱：是否有月份效应？

3.3【Python金融量化】A股沉浮启示录

3.4【宏观量化】股市趋势与拐点如何看？

3.5 2005-2020年A股数据挖掘：谁是最大的牛股？【附Python分析源码】

3.6 机器学习刻画股票市场结构和可视化——以上证50成分股为例

时间序列专题：

3.7【手把手教你】时间序列之日期处理

3.8【Python量化基础】时间序列的自相关性与平稳性

3.9【手把手教你】使用Python玩转金融时间序列模型

3.10 Python玩转金融时间序列之ARCH与GARCH模型

3.11 资产收益率的非平稳性——为何机器学习预测效果不佳？

3.12 基于Markov区制转换模型的股票波动分析

3.13【手把手教你】使用Python实现统计套利

TA-Lib与股票技术分析：

3.14 【手把手教你】股市技术分析利器之TA-Lib（一）

3.15 【手把手教你】股市技术分析利器之TA-Lib（二）

3.16 【手把手教你】量价关系分析与Python实现

3.17 【手把手教你】Python量化股票市场情绪指标ARBR

3.18 【手把手教你】动量指标的Python量化回测

3.19 【Python量化】如何利用欧奈尔的RPS寻找强势股？

3.20 【手把手教你】Python实现量价形态选股

3.21 牛股价量探索性分析与趋势指标可视化

3.22【手把手教你】使用Python对股价的Heikin Ashi蜡烛图进行可视化

投资组合分析与多因子模型 ：

3.23 什么是多因子量化选股模型？

3.24【手把手教你】Python量化Fama-French三因子模型

3.25 单因子测试框架分享

3.26 如何对选股因子进行量化回测？

债券与期权衍生品之QuantLib入门与应用：

3.27【手把手教你】固定收益和衍生品分析利器QuantLib入门

3.28【手把手教你】使用QuantLib进行债券估值和期权定价分析

04策略回测篇


本部分主要是使用Python分析量化策略的评价指标，指数定投策略、机器学习、海龟交易法则和均值回归策略等，以及专题介绍backtrader回测系统的运用。

量化交易策略概述及评价指标：

4.1 【干货分享】一文讲透量化投资方法论体系

4.2 【量化回测】如何规避陷阱及评价策略？

4.3 【手把手教你】Python量化策略风险指标

4.4 【手把手教你】使用pyfinance进行证券收益分析

4.5 【手把手教你】Python实现基于事件驱动的量化回测

构建交易策略并进行简单的量化回测：

4.6 Python数说指数定投策略

4.7【Python量化】怎么在基金定投上实现收益最大化

4.8【手把手教你】使用Logistic回归、LDA和QDA模型预测指数涨跌

4.9 【手把手教你】使用RNN深度学习预测股票价格

4.10  手把手教你用Python搭建自己的量化回测框架【均值回归策略】

4.11【手把手教你】用Python量化海龟交易法则

4.12 A股存在月份效应吗？构建月度择时策略【附Python源码】

4.13 北向资金能预示大盘涨跌？【附Python源码】

开源回测框架backtrader专题系列：

4.14 【手把手教你】入门量化回测最强神器backtrader（一）

4.15【手把手教你】入门量化回测最强神器backtrader（二） 

4.16【手把手教你】入门量化回测最强神器backtrader（三）

4.17 backtrader如何加载股票因子数据？以换手率、市盈率为例进行回测【附Python代码】

4.18 如何用backtrader对股票组合进行量化回测？

4.19【手把手教你】用backtrader量化回测海龟交易策略

4.20 backtrader股票技术指标自定义与量化回测
