import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
ds = pd.read_csv('matches.csv')

# Plotly scatter plot
fig = px.scatter(data_frame=ds, y='target_runs', x='result_margin', color='result')
fig.write_image('images/scatter_plot.png')

# Seaborn scatter plot
plt.figure(figsize=(12, 7))
sns.scatterplot(data=ds, y='target_runs', x='result_margin', hue='result', palette='rocket')
plt.savefig('images/sns_scatter_plot.png')

# Plotly histogram
fig = px.histogram(data_frame=ds, x='season', y='target_runs', color='toss_decision')
fig.write_image('images/histogram_plot.png')

# Seaborn count plot
ds2024 = ds.tail(70)
pom_count = ds2024['player_of_match'].value_counts()
mult_pom = pom_count[pom_count > 1].index
filter_pom_ds2024 = ds2024[ds2024['player_of_match'].isin(mult_pom)]
plt.figure(figsize=(20, 7))
sns.countplot(data=filter_pom_ds2024, x='player_of_match', hue='winner', palette='mako')
plt.savefig('images/count_plot.png')

# Plotly histogram for super over
super_over_count = ds['super_over'].value_counts()
mult_s_o = super_over_count[super_over_count > 1].index
filter_s_o_ds = ds[ds['super_over'].isin(mult_s_o)]
fig = px.histogram(data_frame=filter_s_o_ds, x="season", color="super_over")
fig.write_image('images/super_over_histogram.png')

# Additional plots as needed...
# Save each plot in the 'images' directory

plt.figure(figsize=(25,10))
sns.countplot(data=ds2024,x='winner',hue='season', palette='rocket')
plt.savefig('images/winner_season_countplot.png')

last_4 = ds[ds['season'].isin(['2021','2022','2023','2024'])]
plt.figure(figsize=(25,10))
sns.countplot(data=last_4,x='winner',hue='season', palette='rocket')
plt.savefig('images/last_4_season_winner_countplot.png')

Virat_POM = ds[ds['player_of_match'].isin(['V Kohli'])]
plt.figure(figsize=(10,6))
sns.scatterplot(data=Virat_POM,x='season',y='target_runs',hue='winner',palette='mako')
plt.savefig('images/virat_pom_scatterplot.png')

Dhoni_POM = ds[ds['player_of_match'].isin(['MS Dhoni'])]
plt.figure(figsize=(10,7))
sns.scatterplot(data=Dhoni_POM,x='season',y='target_runs',hue='winner',palette='mako')
plt.savefig('images/dhoni_pom_scatterplot.png')

Virat_POM_chasing = ds[ds['player_of_match'].isin(['V Kohli'])& (ds['toss_winner'] == 'Royal Challengers Bangalore')&(ds['toss_decision'] == 'field')]
fig = px.scatter(data_frame=Virat_POM_chasing,x='season',y='target_runs',color='winner',width=1200, height=700)
fig.write_image('images/virat_pom_chasing_scatter.png')
