import statsmodels.api as sm
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/jayantabasak/python/main/1wayANOVA.csv')
df.head()
a=df['A']
b=df['B']
model=sm.OLS(b,a).fit()
mod_pre=model.predict(a)
mod_details=model.summary()
print(mod_details)