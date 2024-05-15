

# %% 
import pandas as pd
import matplotlib.pyplot as plt


def manipulate_avg(row, y_field):
    if 'ms' in row[y_field]:
        # Manipulate the value for milliseconds
        value = float(row[y_field].replace('ms', ''))
        return value
    elif 'us' in row[y_field]:
        # Manipulate the value for microseconds
        value = round(float(row[y_field].replace('us', '')) / 1000,3)
        return value
    else:
        return row[y_field]


df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')


filtered_df = df[(df['test-name'] == 'ioping-linear-async-read') & (df['cloud'] == 'AZURE')]

x_field = 'filesystem'
y_field = 'avg'

#filtered_df[y_field] = filtered_df[y_field].str.replace(r' ms', '')

# filtered_df[y_field] = filtered_df.apply(manipulate_avg, y_field=y_field,axis=1)


filtered_df[y_field] = pd.to_numeric(filtered_df[y_field])


print(filtered_df.head())

plt.scatter(filtered_df[x_field], filtered_df[y_field])

plt.xticks(rotation=270)


# Annotate each point with its value
for i, (xi, yi) in enumerate(zip(filtered_df[x_field], filtered_df[y_field])):
    plt.annotate(f'{yi}', (xi, yi), textcoords="offset points", xytext=(0,10), ha='center')


# Add labels and title
plt.xlabel(x_field)
plt.ylabel(y_field + '(ms)')
plt.title(x_field + '-' + y_field)

plt.ylim(0, max(filtered_df[y_field])+(.1*max(filtered_df[y_field])))  # Replace x_min and x_max with your desired limits

# Show the plot
plt.show()

# %%
import pandas as pd
import plotnine as p9

def filesystem_sorter(column):
    """Sort function"""
    correspondence = {team: order for order, team in enumerate(all_order)}
    return column.map(correspondence)

df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')


filtered_df = df[(df['filesystem'] == 'efs-single-zone')]

unique_elements = filtered_df['test-name'].tolist()

for element in unique_elements:
    print(f'"{element}"')

x_field = 'filesystem'
y_field = 'avg'
# %%


import pandas as pd
import plotnine as p9
# Example DataFrame
data = {
    'group': ['A', 'A', 'B', 'B', 'B'],
    'test-name': ['test1', 'PIP venv Pytorch Install', 'test2', 'PIP venv Pytorch Install', 'PIP venv Pytorch Install'],
    'value1': [10, 20, 30, 40, 50],
    'value2': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Group by multiple columns and calculate the mean for the desired rows
result = df[df['test-name'] == 'PIP venv Pytorch Install'].groupby(['group', 'test-name']).mean().reset_index()

print(result)
# %%
import pandas as pd
import plotnine as p9
import adjustText as adjust_text


all_order = ['ebs-local-storage',
'rhel8-nfs-same-subnet', 
'same-az-lustre', 
'cross-az-lustre', 
'same-az-zfs', 
'same-az-ontap', 
'efs-single-zone', 
'efs-regional', 
's3-bucket-mountpoint', 
'mdisk-premium-ssd-lrs', 
'netapp-ultra', 
'netapp-premium', 
'netapp-standard', 
'storage-acct-azure-files', 
'elastic-san-same-zone', 
'ssd-persistent-disk',
'gfs-basic-ssd',
'gfs-zonal-ssd', 
'gfs-ent-ssd']

def filesystem_sorter(column):
    """Sort function"""
    correspondence = {team: order for order, team in enumerate(all_order)}
    return column.map(correspondence)

data = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')

data = data[data['test-name'] == 'ioping-ping']

data = data[data['cloud'] == 'AWS']

data = data.sort_values(by='filesystem', key=filesystem_sorter).reset_index(drop = True)

data['filesystem'] = pd.Categorical(data.filesystem, categories=pd.unique(data.filesystem))

x_feature = 'filesystem'
y_feature = 'avg (ms)'

print(data['avg (ms)'].index.tolist())


# # data = data.sort_values(by='filesystem', key=all_order)
# graph = p9.ggplot(data=data,mapping=p9.aes(x=x_feature)) +\
#                     p9.geom_point(p9.aes(y="min (ms)", color="min (ms)")) +\
#                     p9.geom_point(p9.aes(y="avg (ms)", color="avg (ms)")) +\
#                     p9.geom_point(p9.aes(y="max (ms)", color="max (ms)")) +\
#                     p9.theme(figure_size=(10, 6), axis_text_x=p9.element_text(angle = 90)) +\
#                     p9.ggtitle(f"Scatterplot of {x_feature} vs latency") +\
#                     p9.geom_text(mapping=p9.aes(y="min (ms)",label=data["min (ms)"]), nudge_x=0.2, adjust_text={'expand':(1.5, 1.1),'arrowprops':{'arrowstyle':'-','color':'red'} }) +\
#                     p9.geom_text(mapping=p9.aes(y="avg (ms)",label=data["avg (ms)"]), nudge_x=0.2, adjust_text={'expand':(1.5, 1.1),'arrowprops':{'arrowstyle':'-','color':'red'} }) +\
#                     p9.geom_text(mapping=p9.aes(y="max (ms)",label=data["max (ms)"]), nudge_x=0.2, adjust_text={'expand':(1.5, 1.1),'arrowprops':{'arrowstyle':'-','color':'red'} }) +\
#                     p9.scale_colour_gradient(low = "green", high = "red") +\
#                     p9.scale_y_log10() +\
#                     p9.ylab("latency (ms)")

# graph.save("temp.png", format='png')


                

# %%
