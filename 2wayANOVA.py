import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
#create DataFrame in Pandas
df=pd.DataFrame({'water': np.repeat(['daily', 'weekly'], 15),
'sun': np.tile(np.repeat(['low', 'med', 'high'], 5),2), 'height':[6,6,6,5,6,5,5,6,4,5,6,6,7,8,7,3,4,4,4,5,4,4,4,4,4,5,6,6,7,8]})
print(df)
#perform 2 way ANOVA
model=ols('height ~ C(water) + C(sun) + C(water):C(sun)', data=df).fit()
anov_res=sm.stats.anova_lm(model, typ=2)
print(anov_res)