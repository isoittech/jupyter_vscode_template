#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%%
# Pandasのデータフレームとしてデータをロード
df = pd.read_csv("../data/iris.csv" )
df.head()
# %%
# 種別ごとのSepalLengthのヒストグラム
# Nameのの種別ごとに、SepalLengthのヒストグラムを描画する
# sharex、shareyは各ヒストグラムのx、y軸は同じスケールを扱うことを示す
df.hist(by="species", column="sepal_length", sharex=True, sharey=True)
#%%
sns.pairplot(df, hue='species')