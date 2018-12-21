
# coding: utf-8

# ### 月份效应
# 
# 月份效应（Month-of-the-Year Effect） 实证研究发现，在大多数的证券市场中存在某个或某些特定月份的平均收益率年复一年显著地异于其他各月平均收益率的现象，这种市场异象被称作“月份效应”。  
# 
# 在美国的股票市场表现为“1月效应”，即1月份的平均收益率显著高于其他月份的平均收益。该现象最早由美国学者瓦切尔(Wachte1)于1942年发现，但直到1976年罗兹弗(Rozef)和金乃尔(Kinney)系统地将这一异象揭示出来，“1月效应”才逐渐进入现代金融学者的视野，并逐渐形成一套科学严谨的“月份效应”研究体系，包括“1月效应”主要体现在小规模公司的股票上，并相应地提出了“税减假说”等理论解释。  
# 
# 张兵给出了基于资金面季节性流动规律的简要解释，总结起来有两方面：第一，资金面的季节变化，我国股市年末往往面临着各种形式的资金抽回，而来年初这些资金又会回流，这一资金运动规律决定了股市的“春涨”、“冬藏”；第二，重大利好政策往在2、3月份发布，从而引发“春涨”现象 。

# In[1]:


#先引入后面可能用到的包（package）
import pandas as pd  
import numpy as np
import tushare as ts
from datetime import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False


# In[282]:


#获取数据函数
def get_data(code,start_date):
    df=ts.get_k_data(code,start_date)
    df.index=pd.to_datetime(df.date)
    return df
#计算日对数收益率
def log_ret(df):
    logret=np.log(df/df.shift(1))[1:]
    return logret
#将日收益率转换为月收益率
def month_rate(logret):
    date=[]
    d=list(logret.index)
    for i in range(0,np.size(logret)):
        t=''.join([d[i].strftime("%Y"),d[i].strftime("%m"),"01"])
        date.append(datetime.strptime(t,"%Y%m%d"))
    y=pd.DataFrame(logret.values,date,columns=['月收益率'])   
    ret_M=y.groupby(y.index).sum()
    return ret_M

#将日收益率转换为年收益率
def annual_rate(logret):
    year=[]
    d=list(logret.index)
    for i in range(0,np.size(logret)):
        year.append(d[i].strftime("%Y"))
    y=pd.DataFrame(logret.values,year,columns=['年收益率'])
    ret_Y=np.exp(y.groupby(y.index).sum())-1
    return ret_Y


# In[283]:


#获取数据
df=get_data('sh','1993-01-01')
#对数收益率
logret=log_ret(df.close)
#月收益率
ret_M=month_rate(logret)
#年收益率
ret_Y=annual_rate(logret)


# ### 查看K线图
# 使用pyecharts画狂拽酷炫的K线图（cmd上先安装：pip install pyecharts）

# In[478]:


from pyecharts import Kline
v1=list(df.loc[:,['open','close','low','high']].values)
v0=list(df.date)
kline = Kline("上证指数K线图",title_pos='center',title_text_size=15)
kline.add("", v0, v1,is_datazoom_show=True,mark_line=["average"],
         mark_point=["max", "min"],mark_point_symbolsize=80,
         mark_line_valuedim=['highest', 'lowest'] )
#kline.render("上证指数图.html")
kline


# ### 年收益率情况

# In[480]:


from pyecharts import Bar
attr = list(ret_Y.index)
v = list((ret_Y['年收益率']*100).round(2))
bar = Bar("上证指数历年收益率(%)",title_text_size=15,title_pos='center')
bar.add("", attr, v,is_label_show=True, is_datazoom_show=True)
bar


# In[120]:


ret_Y.describe().T


# In[150]:


ret_Y.sort_values('年收益率')[:5].T


# In[151]:


ret_Y.sort_values('年收益率',ascending=False)[:5].T


# In[122]:


ratio=int(ret_Y[ret_Y['年收益率']>0].count().values)/len(ret_Y)
print(f'上涨年份占比{ratio*100}%')


# 从1993年至2018年共26年，上证指数有13年是下跌的，另外13年是上涨的，很fair哦，看来上证指数是属天秤座的。其中，跌幅最大的五年分别为：2008年（-65.39%），1994年（-22.30%），2018年（-21.85%），2011年（-21.68%），2001年（-20.62%）；涨幅最大的五年分别为：2006年（130.43%），2007年（96.66%），2009年（79.98%），1996年（65.14%），2014（52.87%）。平均收益率35.12%，标准差为135.24%，可见，尽管A股市场波动性非常大，特别是前十年，但是整体上来看，并没有大家口中说的那么糟糕。但是为啥赚钱的永远是少数人呢？本质上是因为“知情者”总是是少数的，而财富遵循“幂律分布”（二八法则），此处不详细展开。

# ### 月份效应检验
# 所谓“月份效应”，主要是指股票市场中存在某个或某些特定月份的平均收益率年复一年显著地异于其他各月平均收益率的现象。有实证研究表明，美国股票市场表现为“1月效应”，即1月份的平均收益率为正，且显著高于其他月份的平均收益。该现象最早由Wachte1（1942）发现，但直到1976年Rozef和Kinney系统地将这一异象揭示出来，“1月效应”才引起金融界的注意。美国等发达国家对“月份效应”的讨论和研究已走向成熟，但是由于A股运行时间较短，并且由于文化差异（节假日安排）导致的交易时间不一致，其“月份效应”特征可能异于我国，因此仍有必要进一步挖掘和探讨。  
# 检验思路：（1）将数据分成两组：m月份和其他月份；（2）检验两组数据的平均值是否相等

# In[172]:


#每年不同月份收益率
df_m=pd.DataFrame()
for i in range (1,13):
    ret=ret_M[ret_M.index.month==i]
    df_m[str(i)+'月份']=ret['月收益率'].values
df_m.describe().round(3)


# In[155]:


#除了某一年剩余年份收益率
df_exm=pd.DataFrame()
for i in range (1,13):
    ret=ret_M[ret_M.index.month!=i]
    df_exm['ex'+str(i)]=ret['月收益率'].values


# In[152]:


t1,p1=stats.ttest_1samp(df_m,0.0)
t2,p2=stats.ttest_ind(df_m,df_exm,equal_var=False)


# In[154]:


l=np.array([t1,p1,t2,p2]).T
df=pd.DataFrame(l,index=range(1,13),columns=['单样本t检验_t值',
    '单样本t检验_p值','双样本t检验_t值','双样本t检验_p值'])
df


# In[475]:


pro=[]
al=len(df_m)
for i in df_m.columns:
    up=df_m[df_m[i]>0][i].count()
    r=round((up/al)*100,2)
    pro.append(r)


# In[482]:


from pyecharts import Overlap, Bar, Line, Grid
grid = Grid()
attr = df_m.columns
v1 = pro
v2 = df_m.describe().loc['mean'].values
v2=(v2*100).round(2)
bar = Bar(title="上证指数各月上涨情况",title_text_size=15)
bar.add("各月上涨次数占比%", attr, v1,yaxis_max=80,is_label_show=True)

line = Line()
line.add("各月收益率均值%", attr, v2,is_label_show=True)
overlap = Overlap()
overlap.add(bar)
overlap.add(line, is_add_yaxis=True, yaxis_index=1)

grid.add(overlap, grid_right="17%")
grid


# In[443]:


from pyecharts import Gauge
gauge = Gauge("上证指数二月份上涨情况",title_text_size=15,title_pos='center')
gauge.add("", "1993-2018年\n二月份上涨占比", 69.23)
gauge


# In[484]:


import seaborn as sns
import matplotlib.pyplot as plt
def plot_corr(df):
    dfData = df.corr()
    plt.subplots(figsize=(9, 9)) 
    sns.heatmap(dfData, annot=True, vmax=1, square=True,cmap='Reds')
    plt.savefig('相关系数热力图.png')
    plt.show()


# In[485]:


plot_corr(df_m)


# ### 其他指数情况

# In[254]:


codes=['sh','sz','hs300','sz50','zxb','cyb']


# In[256]:


zs=pd.DataFrame()
for code in codes:
    zs[code]=get_data(code,'2011-01-01')['close']


# In[259]:


zs.head()


# In[277]:


def date_trans(date):
    d=[]
    for i in range(0,len(date)):
        d.append(''.join([date[i].strftime("%Y"),
                         date[i].strftime("%m")
                         ,date[i].strftime("%d")]))
    return d

from pyecharts import Line
date=date_trans(zs.index)
v1=list(zs['sh'].values)
v2=list(zs['sz'].values)
v3=list(zs['hs300'].values)
v4=list(zs['sz50'].values)
v5=list(zs['zxb'].values)
v6=list(zs['cyb'].values)

line = Line(title="")
line.add("上证指数",date,v1,line_width=2)
line.add("深证指数",date,v2,line_width=2)
line.add("沪深300",date,v3,line_width=2)
line.add("上证50",date,v4,line_width=2)
line.add("中小板",date,v5,line_width=2)
line.add("创业板",date,v6,line_width=2)

line


# In[342]:


#对数收益率
zs_log=log_ret(zs)
d={'sh':'上证综指','sz':'深证综指','hs300':'沪深300','sz50':'上证50','zxb':'中小板','cyb':'创业板'}
zs_log.rename(columns=d,inplace=True)


# In[343]:


zs_log.head()


# In[487]:


import seaborn as sns
import matplotlib.pyplot as plt
def plot_corr(df):
    dfData = df.corr()
    plt.subplots(figsize=(9, 9)) 
    sns.heatmap(dfData, annot=True, vmax=1, square=True,cmap='Blues')
    plt.savefig('7相关系数热力图.png')
    plt.show()
plot_corr(zs_log)


# In[319]:


#将日收益率转换为年收益率
def annual_rate(logret):
    year=[]
    d=list(logret.index)
    for i in range(0,len(logret)):
        year.append(d[i].strftime("%Y"))
    y=pd.DataFrame(logret.values,year)
    ret_Y=np.exp(y.groupby(y.index).sum())-1
    return ret_Y


# In[345]:


zs_Y=annual_rate(zs_log)
d={0:'上证综指',1:'深证综指',2:'沪深300',3:'上证50',4:'中小板',5:'创业板'}
zs_Y.rename(columns=d,inplace=True)


# In[337]:


zs_Y.describe().T


# In[351]:


bar = Bar(" ")

attr = list(zs_Y.index)
v1 = list(((zs_Y['上证综指'].values)*100).round(2))
v2 = list(((zs_Y['深证综指'].values)*100).round(2))
v3 = list(((zs_Y['沪深300'].values)*100).round(2))
v4 = list(((zs_Y['上证50'].values)*100).round(2))
v5 = list(((zs_Y['中小板'].values)*100).round(2))
v6 = list(((zs_Y['创业板'].values)*100).round(2))

bar.add("上证综指(%)", attr, v1,)
bar.add("深证综指(%)", attr, v2, )
bar.add("沪深300(%)", attr, v3,)
bar.add("上证50(%)", attr, v4, )
bar.add("中小板(%)", attr, v5,)
bar.add("创业板(%)", attr, v6, )
bar


# In[416]:


dec=zs_Y.describe().T
dec


# In[442]:


from pyecharts import Line,EffectScatter,Overlap
attr = list(dec.index)
v2=dec['std'].values*100
#假设无风险收益率为2%
v1 = dec['mean'].values*100-2
v=((v1/v2)*100).round(2)
line = Line('各指数夏普比率(%)',title_text_size=15,title_pos='center')
line.add('',attr,v)
es = EffectScatter()
es.add('',attr,v,effect_scale=6)  

overlop = Overlap()
overlop.add(line)                   
overlop.add(es)
overlop


# In[352]:


zs_2=zs_M[zs_M.index.month==2]
zs_ex2=zs_M[zs_M.index.month==2]


# In[357]:


cyb_df=get_data('cyb','2011-01-01')
#对数收益率
cyb_logret=log_ret(cyb_df.close)
#月收益率
cyb_ret_M=month_rate(cyb_logret)
#年收益率
cyb_ret_Y=annual_rate(cyb_logret)


# In[382]:


cyb_2=cyb_ret_M[cyb_ret_M.index.month==2]
cyb_ex2=cyb_ret_M[cyb_ret_M.index.month!=2]


# In[383]:


up=cyb_2[cyb_2['月收益率']>0].count()
al=len(cyb_2)
up/al


# In[411]:


def up_ratio(code,m):
    df=get_data(code,'2011-01-01')
    logret=log_ret(df.close)
    ret_M=month_rate(logret)
    ret_2=ret_M[ret_M.index.month==m]
    up=ret_2[ret_2['月收益率']>0].count()
    al=len(ret_2)
    return up/al


# In[412]:


ratio=[]
for code in codes:
    r=up_ratio(code,2)
    ratio.append(r)
ratio


# In[410]:


from pyecharts import Pie

pie = Pie('二月份上涨统计概率',"基于2011-2018年", title_pos='center',title_text_size=15)
pie.add("上证", ["上证综指\n上涨", "下跌"], [62.5, 37.5], center=[30, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None, )
pie.add("深证", ["深证综指\n上涨", "下跌"], [50, 50], center=[50, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("沪深300", ["沪深300\n上涨", "下跌"], [50, 50], center=[70, 30], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("上证50", ["上证50\n上涨", "下跌"], [50, 50], center=[30, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("中小板", ["中小板\n上涨", "下跌"], [75, 25], center=[50, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None)
pie.add("创业板", ["创业板\n上涨", "下跌"], [75, 25], center=[70, 70], radius=[18, 24],
        label_pos='center', is_label_show=True, label_text_color=None,is_legend_show=False)

pie

