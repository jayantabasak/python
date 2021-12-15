import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
myDf=pd.read_csv('1.csv')
model=ols('A~B', data=myDf).fit()
anov_res=sm.stats.anova_lm(model, typ=2)
print(anov_res)



import statsmodels.api as sm
import pandas as pd
df=pd.read_csv('csv-filename.csv')
df.head()

a=df['sales']
b=df['profit']
model=sm.OLS(b,a).fit()
mod_pre=model.predict(a)
mod_details=model.summary()
print(mod_details)