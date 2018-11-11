import pandas as pd
import matplotlib
import scipy.stats as stats
datafile="PlantGrowth.csv"
data=pd.read_csv(datafile)
ctrl=data['weight'][data.group=='ctrl']
data.boxplot('weight',by='group', figsize=(12,8))
grps=pd.unique(data.group.values)
d_data={grp:data['weight'][data.group==grp] for grp in grps}
k=len(pd.unique(data.group))#Number of conditions
N=len(data.values)#conditions times participants
n=data.groupby('group').size()[0]#participant in each condition
#One way Anonva
f,p=stats.f_oneway(d_data['ctrl'],d_data['trt1'],d_data['trt2'])
print('Fvalue is:',f)
#f value = 4.846087
print('Pvalue is:',p)
#p value = 0.01590