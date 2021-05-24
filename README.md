![扫码_搜索联合传播样式-标准色版](https://user-images.githubusercontent.com/24394838/119312678-3e8d3780-bca5-11eb-8b8e-41832426b435.png)
# Python金融量化
专注于分享Python在金融领域的应用，欢迎关注微信公众号Python金融量化 （id：tkfy920）

[Python金融量化合辑](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&amp;mid=2247485222&amp;idx=1&amp;sn=2dea3290b617f0f84410bd4da21e0221&amp;chksm=f9e3c1ccce9448da6bc1dad87c014749c507466b07d2fcf9086d84674b4c4ce9bce748bc6469&token=1911472750&lang=zh_CN#rd)

公众号“Python金融量化”已走过两个年头。这一路走来非常感谢读者的支持，尤其是知识星球圈友，你们的知识付费是我坚持走原创输出的动力。学习是一个循序渐进的过程，只有通过不断的总结才能形成系统的知识框架。通过对两年来发布的60篇原创文章进行梳理，归纳成四个大的部分，包括Python入门篇 、金融数据篇、量化分析篇和策略回测篇 ，形成了较为完整的框架体系。本公众号文章的最大特色是以金融场景+案例形式切入，分享Python在金融量化领域的应用，实战性强，为在校经管类学生和金融从业者提供了丰富的实践分析案例。


01Python入门篇


这一部分主要是关于Python金融量化入门学习路径、量化资源，以及numpy、pandas、matplotlib等量化常用库的入门和应用。Python的编译软件有很多，个人建议安装Anaconda，自带Jupyter notebook和Spyder，其中Jupyter在交互式编程与数据分析上功能十分强大，公众号上所有文章都是基于Jupyter写的。

首先，结合个人经验分享Python金融量化的学习路径，以及分享Python从入门、进阶、到高阶的学习资料，以及金融投资相关书籍（PDF）。

[1.1【Python金融量化】零基础如何开始学？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483886&idx=1&sn=9a420312aff2bb9b8cbb549a54cc876c&chksm=f9e3c704ce944e1238b291937a7184658d5fcba35041f8857b674ff719b81e6b6ef5d8427e1f&scene=21#wechat_redirect)

[1.2【推荐收藏】倾心整理的Python量化资源大合集](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484656&idx=1&sn=7692a9c0f342e59e6c62c9ce3d003d94&chksm=f9e3c21ace944b0c784f3a1a7660b6cb2e0f9b31a9912869a03efc7a55ca0249d7bd27acd92d&scene=21#wechat_redirect)

其次，关于Numpy（数组矩阵）、Pandas（数据处理分析）、Matplotlib（可视化）、Seaborn（可视化）、Sklearn（机器学习）等金融量化常用库的入门和应用。

[1.3【手把手教你】玩转Python量化金融工具之NumPy](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483785&idx=1&sn=19b21a941561194730c063153e236e96&chksm=f9e3c763ce944e75da102b54c313c33af2e96c78c388c1de76c88aac09e231977721b9b7c860&scene=21#wechat_redirect)

[1.4【手把手教你】玩转Python金融量化利器之Pandas](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483803&idx=1&sn=c219250c2a988b21fd75f56830f3e33d&chksm=f9e3c771ce944e6716906dddb068e0e4acafef2d50d1104b060347e7eedeb14a800b07332ca6&scene=21#wechat_redirect)

[1.5【建议收藏】Matplotlib可视化最有价值的50张图](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484293&idx=1&sn=d12edaac5afdd4a018eb8f3749d5f378&chksm=f9e3c56fce944c795de903f801a291ab7be978e6be4847b942709e5b8f3df9f24ea6d01a454b&scene=21#wechat_redirect)

[1.6【手把手教你】Seaborn在金融数据可视化中的应](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484262&idx=1&sn=a36a18ebde9b70e5a618c02591613ca4&chksm=f9e3c58cce944c9a65c9e7a21872d3c705d35fb175cb7993d9df74b492aac3645fba3a3dc44c&token=68143561&lang=zh_CN&scene=21#wechat_redirect)

[1.7【手把手教你】玩转机器学习 Sklearn](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484299&idx=1&sn=448e38f2d15612afd4493d087b40de82&chksm=f9e3c561ce944c7727ef51f82e7945f7c5d71999b450093f782217ecb4b815769307e367e632&scene=21#wechat_redirect)

02金融数据篇


本部分主要是使用Python获取股票行情、上市公司基本面、宏观经济以及财经新闻等数据，对其进行可视化分析，以及使用Postgresql （sqlite3）搭建本地量化分析数据库。

[2.1【手把手教你】Python获取交易数据](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483952&idx=1&sn=a75c73726126993c0875ae957c1c5523&chksm=f9e3c4dace944dcc11ecb0ec94faa8e1244e5783ec59c6593a391e0ca1778296987a88ee9a20&scene=21#wechat_redirect)

[2.2【Python金融量化】上市公司知多少？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483910&idx=1&sn=c9df94b47d968adae6caff887fa56039&chksm=f9e3c4ecce944dfa7c0c1cca6bb346837280355de7ec66935638d22b23debc7d83a96781b7e4&scene=21#wechat_redirect)

[2.3 Python量化选股初探](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483914&idx=1&sn=fd05f39b8933dd0c048d7906d2f31ab7&chksm=f9e3c4e0ce944df6eab464f74d560bf7c63c6ec46a04693a9be89e504e549120240ce2081c01&token=579087029&lang=zh_CN&scene=21#wechat_redirect)

[2.4 2018你不可不知的十大关键词](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483943&idx=1&sn=16c2f8767db5653fbc43e7584c815496&chksm=f9e3c4cdce944ddbc5059235593c59badd43f2e74ac34baf17e1f60bed05525ce01568e03a5c&scene=21#wechat_redirect)

[2.5【手把手教你】Python获取财经数据和可视化分析](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483756&idx=1&sn=86e085866ce4faa03994a2c6c9cf349d&chksm=f9e3c786ce944e90917e2e903901e09e7c8dbea8795ed3c345c34bfc5aaa889666609a7180ba&scene=21#wechat_redirect)

[2.6【文本挖掘】Python带你笑看江湖](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483849&idx=1&sn=61651fb472097280bb26fb9e29db33c4&chksm=f9e3c723ce944e35f4131f5b8ac3dd28399a7edc1633fa5fdf491bb9c124460094825442ca92&scene=21#wechat_redirect)

[2.7【Python金融量化】财经新闻文本分析](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483882&idx=1&sn=e5e95ec19eca42e5247cdde60c12316f&chksm=f9e3c700ce944e169315b1c59f8cadbf912d8ab39c86963261babe8f529ba1fdf125d4d0fb20&scene=21#wechat_redirect)

[2.8【手把手教你】搭建自己的量化分析数据库](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484113&idx=1&sn=f25004ae4bc5c585218ae43b55ed28ee&chksm=f9e3c43bce944d2dac37afcc8ef28fbcfba26e827f4a60a3368c1594bc52327772264d87f475&scene=21#wechat_redirect)

[2.9【手把手教你】Python面向对象编程入门及股票数据管理应用实例](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484675&idx=1&sn=358adcd9df64874df7cdff3433a16d0e&chksm=f9e3c3e9ce944affec7937788b02c4af4cbc90c5eb42c22cd0d5d9a3b125c9d22cc0e8e5cf43&scene=21#wechat_redirect)

03量化分析篇


本部分涉及内容比较多，包括使用Python做金融统计分析、蒙特卡洛模拟，时间序列建模，Talib技术分析、投资组合以及多因子模型分析等。

A股数据探索性分析：

[3.1【Python量化】股票分析入门](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483868&idx=1&sn=61e911d9e33aa8d0b41e7342a0fc3c79&chksm=f9e3c736ce944e200b3cc4f52e690068f07b8dd00f7b2e909fcd59d146e83f117e70615af3e1&scene=21#wechat_redirect)

[3.2 A股指数图谱：是否有月份效应？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483920&idx=1&sn=ad5ad8182714aa3bbf8e39234be0b435&chksm=f9e3c4face944dec0eb39ce5e272365858d265c53f410cdb6bdc2d0489abb11ad6f0e2b952d9&scene=21#wechat_redirect)

[3.3【Python金融量化】A股沉浮启示录](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483874&idx=1&sn=5780ecd0bdbcd9f721218abd265dfa63&chksm=f9e3c708ce944e1e40e8d2d3468b9dea37a7d44f6f7a854e575da07dfd6725542a95280bfa18&scene=21#wechat_redirect)

[3.4【宏观量化】股市趋势与拐点如何看？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483997&idx=1&sn=a3a8e64990eb768a692cea55cd018601&chksm=f9e3c4b7ce944da1b0d70c2908ec8155e9a7d7946ac6580728ac0e1f3a060bbc25409d80a101&scene=21#wechat_redirect)

[3.5 2005-2020年A股数据挖掘：谁是最大的牛股？【附Python分析源码】](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484757&idx=1&sn=c6adf0849accf1e31b6dae0923d82be6&chksm=f9e3c3bfce944aa92a23a08b208e132952963ac3da03df917995bb56b159e2123cbcbb09f336&scene=21#wechat_redirect)

[3.6 机器学习刻画股票市场结构和可视化——以上证50成分股为例](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485190&idx=1&sn=cd1a7a63312e5ea094ebb1acaa61aa5f&chksm=f9e3c1ecce9448fa59664f3e524519613bb46dc8ddc8ed2488fec841da3e6ec8b96882b2af5c&scene=21#wechat_redirect)

时间序列专题：

[3.7【手把手教你】时间序列之日期处理](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483957&idx=1&sn=814ebd7be8703cb39a0c6b1286f89c63&chksm=f9e3c4dfce944dc956835f25fe143a9ab7ae2dcbc20d8da99fc15d2717457cbc4947f15ca713&scene=21#wechat_redirect)

[3.8【Python量化基础】时间序列的自相关性与平稳性](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484407&idx=1&sn=8fc25868bb19c0aad6920064d8abab9b&chksm=f9e3c51dce944c0be68362763c57ead3365315647b48213b8dd7ef6ca735bdac2992389b626f&scene=21#wechat_redirect)

[3.9【手把手教你】使用Python玩转金融时间序列模型](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484446&idx=1&sn=887ae14a361ee1de1c30a5a8b46f4237&chksm=f9e3c2f4ce944be252fb824b5bfdca840e677efdd92230a24803fb075c076ad8e7ba2fe7f2b1&scene=21#wechat_redirect)

[3.10 Python玩转金融时间序列之ARCH与GARCH模型](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484468&idx=1&sn=fda45e2534f22a97ebaf215c8c150aef&chksm=f9e3c2dece944bc8316e7017d1e199fea60fe3e7a417ab1205bc8044da5037be70e31ce63730&scene=21#wechat_redirect)

[3.11 资产收益率的非平稳性——为何机器学习预测效果不佳？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485150&idx=1&sn=e1a926051d1935f7b00a128fc128265a&chksm=f9e3c034ce944922a1ffe598832a2fdb011b12a0c058713bf7e6d16c10e84f55272a6dbd26ba&scene=21#wechat_redirect)

[3.12 基于Markov区制转换模型的股票波动分析](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484920&idx=1&sn=e00e226a3cae40cf82b924963f3f62c5&chksm=f9e3c312ce944a04847db4cb2000d801377bb1c28a133fc4cd90db9fc11f99e960189b666a84&scene=21#wechat_redirect)

[3.13【手把手教你】使用Python实现统计套利](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484303&idx=1&sn=9cc094fe20a73fdf8b9e5d5316426985&chksm=f9e3c565ce944c73fe3268c42d580423d99ad50450529fdefb1808de9282a1aff555354e146f&scene=21#wechat_redirect)

TA-Lib与股票技术分析：

[3.14 【手把手教你】股市技术分析利器之TA-Lib（一）](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484013&idx=1&sn=0599de6b805a1e76a61935be9c44871f&chksm=f9e3c487ce944d9179f2e16e78ba7e7cff8353b2c669c331e97a8cf70779a8e76eaf706db5c8&scene=21#wechat_redirect)

[3.15 【手把手教你】股市技术分析利器之TA-Lib（二）](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484021&idx=1&sn=e5c0399e92465a2e73329ed69df4d268&chksm=f9e3c49fce944d89e9c2edda178b5cee725291d8019bd7bd5bc2d8cac904030ae2e97f452594&scene=21#wechat_redirect)

[3.16 【手把手教你】量价关系分析与Python实现](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484052&idx=1&sn=91fdb8556f135d80f8946f5f6df1f81f&chksm=f9e3c47ece944d68ba91b8fe563f80fb83457822fa016a52c73f6168ca62de0511ae8c71c446&scene=21#wechat_redirect)

[3.17 【手把手教你】Python量化股票市场情绪指标ARBR](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484070&idx=1&sn=b4418dc3fe6289a9f417951d344c6669&chksm=f9e3c44cce944d5a21a8a0c1249768ba7d08a4f49501c1b53c94888f8651bbc15e4e6e13ef29&scene=21#wechat_redirect)

[3.18 【手把手教你】动量指标的Python量化回测](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484084&idx=1&sn=98928a4b2ef5ad8d1a1ef7282c386875&chksm=f9e3c45ece944d4843c85563c87e80fb4ae90cd5c88cb0bdedf2f3b9ad53320eaf596d5be1a0&scene=21#wechat_redirect)

[3.19 【Python量化】如何利用欧奈尔的RPS寻找强势股？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484048&idx=1&sn=5de797f473369f3aebeb3be0a0de36d6&chksm=f9e3c47ace944d6c5251426f04f29338bfb7f193b281927db90eabd7e01fbe3d6115b87eb79d&scene=21#wechat_redirect)

[3.20 【手把手教你】Python实现量价形态选股](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484723&idx=1&sn=86a08b287215b7848def0d2a09a80943&chksm=f9e3c3d9ce944acfed6f33a9d71091229bb86a1698f7acbaf7e613398d0a6ce46f8ad56f9421&scene=21#wechat_redirect)

[3.21 牛股价量探索性分析与趋势指标可视化](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&amp;mid=2247485130&amp;idx=1&amp;sn=13890cbab55191e3fe1bfae385a9a231&amp;chksm=f9e3c020ce9449364587a95561fd35cdc095e10dfe62e8ee20ea025f85aa9e097d17714f7bd8&token=1911472750&lang=zh_CN#rd)

[3.22【手把手教你】使用Python对股价的Heikin Ashi蜡烛图进行可视化](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484569&idx=1&sn=5e08729f109f1ed4b40323d4ffc24737&chksm=f9e3c273ce944b65d5cb7ae41aa63738ae3ed41e3d0951621ced2a7b4c66cff943fab998bde1&scene=21#wechat_redirect)

投资组合分析与多因子模型 ：

[3.23 什么是多因子量化选股模型？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484149&idx=1&sn=5a1506ed26e5bd5a35a6f152f0aa956c&chksm=f9e3c41fce944d092df86b3df4ef73c3fdd8743a764ce4641e48e43e59ea2512818ad4cec565&scene=21#wechat_redirect)

[3.24【手把手教你】Python量化Fama-French三因子模型](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484215&idx=1&sn=bd21f98f0d24f47d08064c263770c88a&chksm=f9e3c5ddce944ccb9e7cff5d5a000ff25205de50257e2ee36e31741a44f1de5872a968aca88e&scene=21#wechat_redirect)

[3.25 单因子测试框架分享](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484080&idx=1&sn=65d9c12162a57c13b37323c0797856d6&chksm=f9e3c45ace944d4cdf3936a93ef66be41245973721eb7f1c6336443638d474f47af1f3f173d8&scene=21#wechat_redirect)

[3.26 如何对选股因子进行量化回测？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484238&idx=1&sn=47a7611bf690e3abfaede04238fac910&chksm=f9e3c5a4ce944cb260f86ff266d8d8a11f14bd8074f19fdc5b38bfd3d4073b414343fd89dafa&scene=21#wechat_redirect)

债券与期权衍生品之QuantLib入门与应用：

[3.27【手把手教你】固定收益和衍生品分析利器QuantLib入门](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485162&idx=1&sn=7f40e7fd0ef31efb4174dcf0fb4f3f6c&chksm=f9e3c000ce9449161f5c08c438473613d2aba84a49b514d8e4f3c8ef8747dece5413add82d97&scene=21#wechat_redirect)

[3.28【手把手教你】使用QuantLib进行债券估值和期权定价分析](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485180&idx=1&sn=739ea8acd5d93a7660321c8129940ae9&chksm=f9e3c016ce944900ca8af5795b27e941c359c186f8265f9ab06c26ca55f9c67ca447d4ec0955&scene=21#wechat_redirect)

04策略回测篇


本部分主要是使用Python分析量化策略的评价指标，指数定投策略、机器学习、海龟交易法则和均值回归策略等，以及专题介绍backtrader回测系统的运用。

量化交易策略概述及评价指标：

[4.1 【干货分享】一文讲透量化投资方法论体系](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484037&idx=1&sn=8b6677542257ac09b662f02d8464330e&chksm=f9e3c46fce944d79ad63f07d57c385e12098afb9f12eea479433e5f09bad0b58fa8686fe2a54&scene=21#wechat_redirect)

[4.2 【量化回测】如何规避陷阱及评价策略？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484263&idx=1&sn=c96ced2bbe52bde4c61977e86867502f&chksm=f9e3c58dce944c9be1d727fb5dfb4a289d4804ae0ae0ca1aa73778a69cfb9bd5c9e9f730168c&scene=21#wechat_redirect)

[4.3 【手把手教你】Python量化策略风险指标](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483991&idx=1&sn=7e2a54011706fd88ff7cef2007f840d8&chksm=f9e3c4bdce944daba8cdd20fa7ca26704381779159f2aa25e66a2d1f527590e29c906df9a697&scene=21#wechat_redirect)

[4.4 【手把手教你】使用pyfinance进行证券收益分析](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485075&idx=1&sn=539b9a3ebfa5ca07928e1143bb3ab4f6&chksm=f9e3c079ce94496fcf120906c634b73642989f0823f4e1763999b41232686da93f7c574a58fa&scene=21#wechat_redirect)

[4.5 【手把手教你】Python实现基于事件驱动的量化回测](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484793&idx=1&sn=bf9b003b5d926e3fb4e383f572f9487e&chksm=f9e3c393ce944a85e3cc2fee6538cbbe221ec17cbaaa98304d331678275a7669088188c1d8dd&scene=21#wechat_redirect)

构建交易策略并进行简单的量化回测：

[4.6 Python数说指数定投策略](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247483936&idx=1&sn=d5c041d3f959a6d42742fed49c066de9&chksm=f9e3c4cace944ddc9a4961610f24d9eb904bce2b740dc948251f99f948f358190c5a77755fa0&scene=21#wechat_redirect)

[4.7【Python量化】怎么在基金定投上实现收益最大化](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484246&idx=1&sn=ce86c3f7fe1ab219942ef872f0abbb7b&chksm=f9e3c5bcce944caa1a70ecf21e9c32470dfeb04e69d0e3e0a18a1f60534dbee89b7a850d11e4&scene=21#wechat_redirect)

[4.8【手把手教你】使用Logistic回归、LDA和QDA模型预测指数涨跌](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484650&idx=1&sn=f93e9a786ee5d2d27254bf49d4a40de0&chksm=f9e3c200ce944b1620104a6a2109969d1cec3a115cf1e4e7b0670129bb997cb55f89dd02f4f7&scene=21#wechat_redirect)

[4.9 【手把手教你】使用RNN深度学习预测股票价格](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484611&idx=1&sn=8863bce3989cd574b310196b7f15e875&chksm=f9e3c229ce944b3fe9843395930102011484b0b591e96f550641de57afd63bf9bcdc92b382b4&scene=21#wechat_redirect)

[4.10  手把手教你用Python搭建自己的量化回测框架【均值回归策略】](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484580&idx=1&sn=ba6b2a4646f59f45577d12b81d745d01&chksm=f9e3c24ece944b58f3f2ee965c8498492751617eaab0559a1c537ac247b17aad13a8b56f781f&scene=21#wechat_redirect)

[4.11【手把手教你】用Python量化海龟交易法则](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484277&idx=1&sn=83cb004ebc7be3f6535b0433cbd81f65&chksm=f9e3c59fce944c899c3d7236c1918c612b53764cd0e6388d87efa4400bb50a5d3bf1e41eee4c&scene=21#wechat_redirect)

[4.12 A股存在月份效应吗？构建月度择时策略【附Python源码】](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485101&idx=1&sn=f6ebf692eaab157d16bba14e95c1e9ce&chksm=f9e3c047ce944951e61b4752ddfb9e3467e5ef9d3f967ddb5913e0b762134d338437a571e14e&scene=21#wechat_redirect)

[4.13 北向资金能预示大盘涨跌？【附Python源码】](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485004&idx=1&sn=ae89dbe3d78ab465b193409f94ce4173&chksm=f9e3c0a6ce9449b05d4022634957993defbf14302f6a386fa0a97e6b410bb48ec2ed95e1d993&scene=21#wechat_redirect)

开源回测框架backtrader专题系列：

[4.14 【手把手教你】入门量化回测最强神器backtrader（一）](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484803&idx=1&sn=59502204fb39d150c98e9951a1614ec0&chksm=f9e3c369ce944a7f9f8e83a7fc4aa9b1450ec98a41eefffda3158f75f824af88117f85be69ca&scene=21#wechat_redirect)

[4.15【手把手教你】入门量化回测最强神器backtrader（二）](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484807&idx=1&sn=6eac4a86ee0e0f2ec06f5dfb4c9192a2&chksm=f9e3c36dce944a7b67986f0b8adef4b0fc02bdcb6d88bdd33662ef9c2e713262dc60477523fe&scene=21#wechat_redirect)

[4.16【手把手教你】入门量化回测最强神器backtrader（三）](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484821&idx=1&sn=21df9cef8351529ac9712fc0c61dc5df&chksm=f9e3c37fce944a69b193aac92f21f3c214b7454881a90edf111627637ac5f21942775171b92d&scene=21#wechat_redirect)

[4.17 backtrader如何加载股票因子数据？以换手率、市盈率为例进行回测【附Python代码】](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484832&idx=1&sn=9d282abb397a4459c7b2a372d635cfb8&chksm=f9e3c34ace944a5c85070e7289812ca8b87c4003f190da336a2f831c74de263b1d65d54c46e5&scene=21#wechat_redirect)

[4.18 如何用backtrader对股票组合进行量化回测？](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484855&idx=1&sn=1e55ba64b1b6ba5739d31fa91d87ca2e&chksm=f9e3c35dce944a4b3f2653e39266d6896e668249f44d6244d2028b9724b2813a29f4017c7bc7&scene=21#wechat_redirect)

[4.19【手把手教你】用backtrader量化回测海龟交易策略](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484953&idx=1&sn=0768af4bf8c011e25e9784feb4503e66&chksm=f9e3c0f3ce9449e5437f534de0ecbeb5309972deee43f96f352ba900d3614b9601838077335f&scene=21#wechat_redirect)

[4.20 backtrader股票技术指标自定义与量化回测](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247485043&idx=1&sn=7be7e7641c524472c1977a474a7109d6&chksm=f9e3c099ce94498fd6a038495e6e373328dae7651e412327cfb53477bde37ae0a6b1c162735d&scene=21#wechat_redirect)

更多干货请关注微信公众号：Python金融量化
