import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# 忽略警告信息
warnings.filterwarnings('ignore')

df = pd.read_csv('./population-and-demography.csv')
# 重命名列
df = df.rename(columns={'Population - Sex: all - Age: all - Variant: estimates': 'Population'})

print(df.head())

# 排除非国家的数据
country_population = df[~df['Entity'].isin([
    'World',
    'Africa (UN)',
    'Asia (UN)',
    'Americas (UN)',
    'Americas(UN)',
    'Europe (UN)',
    'Oceania (UN)',
    'Latin America and the Caribbean (UN)',
    'Northern America (UN)',
    'High-income countries',
    'Upper-middle-income countries',
    'Lower-middle-income countries',
    'Low-income countries',
    'More developed countries',
    'Least developed countries',
    'Land-locked developing countries (LLDC)',
    'Small island developing states (SIDS)',
    'More developed regions',
    'Less developed regions',
    'Less developed regions, excluding least developed countries',
    'Less developed regions, excluding China',
])]

# 重置索引
country_population.reset_index(inplace=True)
print(country_population)

# 保留国家、代码、年份、人口，并按人口降序排列
country_population = country_population[['Entity', 'Code', 'Year', 'Population']].sort_values(by='Population',
                                                                                              ascending=False)
country_population.reset_index(inplace=True)
print(country_population)

# 按年份和人口排序。选取每年人口最多的前10
top_pop_by_year = country_population.sort_values(by=['Year', 'Population'], ascending=[False, False])
top_pop_by_year = top_pop_by_year.groupby('Year').head(10)
top_pop_by_year.reset_index(inplace=True)
top_pop_by_year = top_pop_by_year.drop(columns=['level_0', 'index'], axis=1)
print(top_pop_by_year)

plt.figure(figsize=(18, 10))
plt.subplot(2, 2, 1)
sns.set_style('darkgrid')
ax = sns.barplot(data=top_pop_by_year[:10], x='Population', y='Entity', palette='magma', edgecolor='black', errwidth=0)
plt.title('Most Population 2023')
plt.xlabel('Population (billion)')
plt.ylabel('Country')

plt.subplot(2, 2, 2)
ax = sns.barplot(data=top_pop_by_year[10:20], x='Population', y='Entity', palette='magma', edgecolor='black',
                 errwidth=0)
plt.title('Most Population 2022')
plt.xlabel('Population (billion)')
plt.ylabel('Country')

plt.subplot(2, 2, 3)
sns.set_style('darkgrid')
ax = sns.barplot(data=top_pop_by_year[20:30], x='Population', y='Entity', palette='magma', edgecolor='black',
                 errwidth=0)
plt.title('Most Population 2021')
plt.xlabel('Population (billion)')
plt.ylabel('Country')

plt.subplot(2, 2, 4)
sns.set_style('darkgrid')
ax = sns.barplot(data=top_pop_by_year[30:40], x='Population', y='Entity', palette='magma', edgecolor='black',
                 errwidth=0)
plt.title('Most Population 2020')
plt.xlabel('Population (billion)')
plt.ylabel('Country')

plt.tight_layout()
plt.show()

# 按年份和人口排序，选取每年人口最少的前10
bot_pop_by_year = country_population.sort_values(by=['Year', 'Population'], ascending=[False, True])
bot_pop_by_year = bot_pop_by_year.groupby('Year').head(10)
bot_pop_by_year.reset_index(inplace=True)
bot_pop_by_year = bot_pop_by_year.drop(columns=['level_0', 'index'], axis=1)
print(bot_pop_by_year)

plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
sns.set_style('darkgrid')
ax = sns.barplot(data=bot_pop_by_year[:10], x='Population', y='Entity', palette='icefire', errwidth=0)
plt.title('Least Population 2023')
plt.xlabel('Population')
plt.ylabel('Country')

# 在条形图上显示具体数据值
ax.bar_label(ax.containers[0])

plt.subplot(2, 2, 2)
ax = sns.barplot(data=bot_pop_by_year[10:20], x='Population', y='Entity', palette='icefire', errwidth=0)
plt.title('Least Population 2022')
plt.xlabel('Population')
plt.ylabel('Country')

ax.bar_label(ax.containers[0])

plt.subplot(2, 2, 3)
sns.set_style('darkgrid')
ax = sns.barplot(data=bot_pop_by_year[20:30], x='Population', y='Entity', palette='icefire', errwidth=0)
plt.title('Least Population 2021')
plt.xlabel('Population')
plt.ylabel('Country')

ax.bar_label(ax.containers[0])

plt.subplot(2, 2, 4)
sns.set_style('darkgrid')
ax = sns.barplot(data=bot_pop_by_year[30:40], x='Population', y='Entity', palette='icefire', errwidth=0)
plt.title('Least Population 2020')
plt.xlabel('Population')
plt.ylabel('Country')

ax.bar_label(ax.containers[0])

plt.tight_layout()
plt.show()

# 使用loc函数通过索引提取行数据，如（取‘index’为‘A’的行），这里选择不同的大陆/地区数据
df.set_index('Entity', inplace=True)
continent_population = df.loc[[
    'World',
    'Africa (UN)',
    'Asia (UN)',
    'Americas (UN)',
    'Europe (UN)',
    'Oceania (UN)',
    'Latin America and the Caribbean (UN)',
    'Northern America (UN)',
]]
# 重置索引
continent_population = continent_population.rename_axis('Entity').reset_index()
print(continent_population.head(30))

# 世界人口随时间变化曲线图
plt.figure(figsize=(16, 8))
sns.set_style('darkgrid')
world_population = df.query("Entity == 'World'")
sns.lineplot(data=world_population, x='Year', y='Population', marker='o')
plt.title('World Population over years')
plt.xlabel('Year')
plt.ylabel('Population (billion)')
plt.tight_layout()
plt.show()

continent = continent_population.sort_values(by=['Year', 'Population'], ascending=[False, False])
continent = continent.groupby('Year').head(10)
continent.reset_index(inplace=True)
continent = continent.drop(columns=['index', 'Code'], axis=1)
print(continent.loc[350:400])

plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
sns.set_style('darkgrid')
ax = sns.barplot(data=continent[:8], x='Population', y='Entity', palette='dark', edgecolor='black', errwidth=0)
plt.title('Continent Population 2023')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.subplot(2, 2, 2)
ax = sns.barplot(data=continent[8:16], x='Population', y='Entity', palette='dark', edgecolor='black', errwidth=0)
plt.title('Continent Population 2022')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.subplot(2, 2, 3)
sns.set_style('darkgrid')
ax = sns.barplot(data=continent[16:24], x='Population', y='Entity', palette='dark', edgecolor='black', errwidth=0)
plt.title('Continent Population 2021')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.subplot(2, 2, 4)
sns.set_style('darkgrid')
ax = sns.barplot(data=continent[24:32], x='Population', y='Entity', palette='dark', edgecolor='black', errwidth=0)
plt.title('Continent Population 2020')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.tight_layout()
plt.show()

plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
sns.set_style('darkgrid')
ax = sns.barplot(data=continent[584:591], x='Population', y='Entity', palette='bright', edgecolor='black', errwidth=0)
plt.title('Continent Population 1950')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.subplot(2, 2, 2)
ax = sns.barplot(data=continent[384:391], x='Population', y='Entity', palette='bright', edgecolor='black', errwidth=0)
plt.title('Continent Population 1975')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.subplot(2, 2, 3)
sns.set_style('darkgrid')
ax = sns.barplot(data=continent[184:191], x='Population', y='Entity', palette='bright', edgecolor='black', errwidth=0)
plt.title('Continent Population 2000')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.subplot(2, 2, 4)
sns.set_style('darkgrid')
ax = sns.barplot(data=continent[:8], x='Population', y='Entity', palette='bright', edgecolor='black', errwidth=0)
plt.title('Continent Population 2023')
plt.xlabel('Population (billion)')
plt.ylabel('Continent')

plt.tight_layout()
plt.show()

plt.figure(figsize=(22, 11))
sns.set_style('darkgrid')
sns.lineplot(data=continent, x='Year', y='Population', hue='Entity', marker='X', lw=3)
plt.title('Continent Population over years')
plt.xlabel('Year')
plt.ylabel('Population (billion)')
plt.show()

# 重置索引，设置索引为Entity
df = df.rename_axis('Entity').reset_index()
df.set_index('Entity', inplace=True)
income_population = df.loc[[
    'High-income countries',
    'Upper-middle-income countries',
    'Lower-middle-income countries',
    'Low-income countries'
]]

income_population = income_population.rename_axis('Entity').reset_index()
print(income_population.head(50))

# 按年份和人口排序，并选取每年人口最多的前10收入层级
income = income_population.sort_values(by=['Year', 'Population'], ascending=[False, False])
income = income.groupby('Year').head(10)
income.reset_index(inplace=True)
income = income.drop(columns=['index', 'Code'], axis=1)
print(income)

# 随时间变化的各收入层级人口折线图
plt.figure(figsize=(22, 11))
sns.set_style('darkgrid')
sns.lineplot(data=income, x='Year', y='Population', hue='Entity', marker='X', lw=3)
plt.title('Several Income Layers Population over years')
plt.xlabel('Year')
plt.ylabel('Population (billion)')
plt.show()

# https://www.kaggle.com/datasets/benitoitelewuver/population-and-demography-dataset/data
