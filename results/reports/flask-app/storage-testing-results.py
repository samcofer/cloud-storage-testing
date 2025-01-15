from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import adjustText as adjust_text
import plotnine as p9
import io
import base64
import json
import os

app = Flask(__name__)

import os
# When running in Posit Workbench, apply ProxyFix middleware
# See: https://flask.palletsprojects.com/en/2.2.x/deploying/proxy_fix/ 
if 'RS_SERVER_URL' in os.environ and os.environ['RS_SERVER_URL']:
	from werkzeug.middleware.proxy_fix import ProxyFix
	app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)

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

azure_order = [
'mdisk-premium-ssd-lrs', 
'netapp-ultra', 
'netapp-premium', 
'netapp-standard', 
'storage-acct-azure-files', 
'elastic-san-same-zone'
]

aws_order = [
'rhel8-nfs-same-subnet', 
'ebs-local-storage', 
'same-az-lustre', 
'cross-az-lustre', 
'same-az-zfs', 
'same-az-ontap', 
'efs-single-zone', 
'efs-regional', 
's3-bucket-mountpoint', 
]

gcp_order = [
'ssd-persistent-disk',
'gfs-basic-ssd',
'gfs-zonal-ssd',
'gfs-regional-ssd',
'gfs-ent-ssd' 
]

io_perf_data = {
    "ioping-ping": ["latency (ms)","iops"],
    "ioping-large-ping": ["latency (ms)","iops"],
    'ioping-linear-async-read': ["latency (ms)","count","volume (GiB)","iops","throughput (MiB/s)"],
    "ioping-linear-async-write": ["latency (ms)","count","volume (GiB)","iops","throughput (MiB/s)"],
}

r_perf_data = {'R - fsbench': [
    'Install MASS (s)', 'Install lattice (s)', 'Install BH (s)', 'Write CSV, 10KB (s)', 'Write CSV, 1MB (s)', 
    'Write CSV, 100MB (s)', 'Write CSV, 1GB (s)', 'Read CSV, 10KB (s)', 'Read CSV, 1MB (s)', 'Read CSV, 100MB (s)', 
    'Read CSV, 1GB (s)', 'DD write, 1GB, 2 Parallel Ops (s)', 'DD write, 1GB, 4 Parallel Ops (s)', 
    'DD write, 1GB, 8 Parallel Ops (s)', 'DD write, 1GB, 16 Parallel Ops (s)', 'DD read, 1GB, 2 Parallel Ops (s)', 
    'DD read, 1GB, 4 Parallel Ops (s)', 'DD read, 1GB, 8 Parallel Ops (s)', 'DD read, 1GB, 16 Parallel Ops (s)', 
    'Write CSV, 100MB over 10 files (s)', 'Read CSV, 100MB over 10 files (s)', 'Write CSV, 100MB over 100 files (s)', 
    'Read CSV, 100MB over 100 files (s)', 'Write CSV, 100MB over 1000 files (s)', 'Read CSV, 100MB over 1000 files (s)', 
    'Write CSV, 100MB over 10000 files (s)', 'Read CSV, 100MB over 10000 files (s)', 
    'DD write, 10MB over 1000 files, 2 Parallel Ops (s)', 'DD write, 10MB over 1000 files, 4 Parallel Ops (s)', 
    'DD write, 10MB over 1000 files, 8 Parallel Ops (s)', 'DD write, 10MB over 1000 files, 16 Parallel Ops (s)', 
    'DD read, 10MB over 1000 files, 2 Parallel Ops (s)', 'DD read, 10MB over 1000 files, 4 Parallel Ops (s)', 
    'DD read, 10MB over 1000 files, 8 Parallel Ops (s)', 'DD read, 10MB over 1000 files, 16 Parallel Ops (s)', 
    'FST random reads, 100MB over 10*10MB reads (s)', 'FST random reads, 100MB over 100*1MB reads (s)', 
    'FST random reads, 100MB over 1000*100KB reads (s)', 'FST random reads, 100MB over 10000*10KB reads (s)', 
    'Read 14 days of CRAN logs with fread (s)', 'Sample 5000 rows from each of 14 CRAN logs with vroom (s)'
]}

python_perf_data = {
    "PIP venv Pytorch Install": ["pytorch-install(ms)"]
}

# app_perf_data = {
#     "acl-and-lock-testing": ["extended-acl-support","linkbased-file-locks"]
# }

concatenated_data = {}
concatenated_data.update(io_perf_data)
concatenated_data.update(r_perf_data)
concatenated_data.update(python_perf_data)
# concatenated_data.update(app_perf_data)

def filesystem_sorter(column):
    """Sort function"""
    correspondence = {team: order for order, team in enumerate(all_order)}
    return column.map(correspondence)

def ioplot(data,x_feature,y_feature,columns,sort_col, label_factor=0.1,descending="asc"):

    if not label_factor:
        label_factor = .2
    if descending=="desc":
        sort_order = "False"
    else:
        sort_order = "True"

    print(f'reorder(x={x_feature}, y={sort_col}, ascending={sort_order})')

    if len(columns) == 2:
        graph = p9.ggplot(data=data,mapping=p9.aes(x=f'reorder(x={x_feature}, y={sort_col}, ascending={sort_order})', shape="cloud")) +\
                                p9.geom_point(p9.aes(y=columns[0], color="cloud")) +\
                                p9.geom_point(p9.aes(y=columns[1], color="cloud")) +\
                                p9.theme(figure_size=(10, 8), axis_text_x=p9.element_text(angle = 90)) +\
                                p9.ggtitle(f"Scatterplot of {x_feature} vs {y_feature}") +\
                                p9.geom_text(mapping=p9.aes(y=data[columns[0]] +-1*label_factor*data[columns[0]],label=data[columns[0]])) +\
                                p9.geom_text(mapping=p9.aes(y=data[columns[1]] +label_factor*data[columns[1]],label=data[columns[1]])) +\
                                p9.ylab(y_feature) +\
                                p9.labs(color = f"{y_feature}\n") +\
                                p9.xlab(x_feature)
    else:
        adjust_text_props = {'force_text':(1, 1),'expand':(1.5, 2), "min_arrow_len":.1, 'arrowprops':{'arrowstyle':'-','color':'red'}}

        graph = p9.ggplot(data=data,mapping=p9.aes(x=f'reorder(x={x_feature}, y={sort_col}, ascending={sort_order})', shape="cloud")) +\
                                p9.geom_point(p9.aes(y=columns[0], color="cloud"),size=4) +\
                                p9.theme(figure_size=(10, 8), axis_text_x=p9.element_text(angle = 90)) +\
                                p9.ggtitle(f"Scatterplot of {x_feature} vs {y_feature}") +\
                                p9.geom_text(mapping=p9.aes(y=data[columns[0]],label=data[columns[0]]), adjust_text=adjust_text_props) +\
                                p9.ylab(y_feature) +\
                                p9.labs(color = f"{y_feature}\n") +\
                                p9.xlab(x_feature) 

             # p9.geom_text(mapping=p9.aes(y=data[columns[0]] +-1*label_factor*data[columns[0]].median(),label=data[columns[0]]), adjust_text=adjust_text_props) +\


    return graph


def generate_scatterplot(data, x_feature, y_feature, order):
    sns.set(style="whitegrid")
    fig=plt.figure(figsize=(10, 6), layout="tight")
    data = data.sort_values(by='filesystem', key=filesystem_sorter)
    sns.scatterplot(data=data, x=x_feature, y=y_feature, s=100, alpha=0.7, hue_order=order)
    plt.title(f"Scatterplot of {x_feature} vs {y_feature}")
    # Add labels and title
    plt.xlabel(x_feature)
    plt.ylabel(y_feature + '(ms)')


    plt.ylim(0, max (ms)(data[y_feature])+(.1*max (ms)(data[y_feature]))) 
    # plt.legend(title='Filesystem Performance', loc='upper right')
    plt.xticks(rotation=270)

    # Annotate each point with its value
    for i, (xi, yi) in enumerate(zip(data[x_feature], data[y_feature])):
        plt.annotate(f'{yi}', (xi, yi), textcoords="offset points", xytext=(0,10), ha='center')


    # Save plot to a BytesIO object
    buf1 = io.BytesIO()
    plt.savefig(buf1, format='png') 
    buf1.seek(0)

    # Encode plot as base64 string
    plot_data = base64.b64encode(buf1.getvalue()).decode('utf-8')
    plt.close()

    return plot_data

def generate_plotnine(data, x_feature, y_feature,test_name, order):
    
    data = data.sort_values(by='filesystem', key=filesystem_sorter)
    data['filesystem'] = pd.Categorical(data.filesystem, categories=pd.unique(data.filesystem))

    if not y_feature:
        y_feature = "latency (ms)" 

    data['label_pos'] = [1 if i % 2 == 0 else -1 for i in range(len(data))]

    if "latency (ms)" in y_feature:
        data["avg"] = data["avg (ms)"]
        adjust_text_props = {'expand':(1.5, 2), "min_arrow_len":.1, 'arrowprops':{'arrowstyle':'-','color':'red'}}
        graph = p9.ggplot(data=data,mapping=p9.aes(x=f'reorder({x_feature}, avg)', shape="cloud")) +\
                            p9.geom_line(p9.aes(y="avg (ms)", group=1)) +\
                            p9.geom_point(p9.aes(y="min (ms)", color="min (ms)"), size=1.5) +\
                            p9.geom_point(p9.aes(y="avg (ms)", color="avg (ms)"), size=4) +\
                            p9.geom_point(p9.aes(y="max (ms)", color="max (ms)"), size=1.5) +\
                            p9.labs(color = f"{y_feature}\n") +\
                            p9.theme(figure_size=(10, 8), axis_text_x=p9.element_text(angle = 90)) +\
                            p9.ggtitle(f"Scatterplot of {x_feature} vs latency(ms)") +\
                            p9.geom_text(mapping=p9.aes(y=data["avg (ms)"],label=data["avg (ms)"]), adjust_text=adjust_text_props) +\
                            p9.scale_colour_gradient(low = "#447099", high = "#EE6331", trans="log10") +\
                            p9.scale_y_log10() +\
                            p9.ylab("latency (ms)") +\
                            p9.xlab(x_feature)

                            #p9.geom_text(mapping=p9.aes(y=data["min (ms)"] +-1*.3*data["min (ms)"],label=data["min (ms)"])) +\
                            #p9.geom_text(mapping=p9.aes(y=data["max (ms)"] +.3*data["max (ms)"],label=data["max (ms)"])) +\
    elif "time (s)" in y_feature:
        data["time"] = data["requests-time (s)"]
        label_factor = .2
        sort_order = "desc"
        graph = ioplot(data=data, x_feature=x_feature, y_feature=y_feature, columns=["requests-time (s)","generated-time (s)"], sort_col="time",label_factor=label_factor, descending=sort_order)   
    elif "volume (GiB)" in y_feature:
        data["volume"] = data["requests-ops-volume (GiB)"]
        label_factor = .2
        sort_order = "desc"
        graph = ioplot(data=data, x_feature=x_feature, y_feature=y_feature, columns=["requests-ops-volume (GiB)","generated-ops-volume (GiB)"], sort_col="volume",label_factor=label_factor, descending=sort_order)   
    elif "count" in y_feature:
        data["count"] = data["requests-count (count)"]
        label_factor = .2
        sort_order = "desc"
        graph = ioplot(data=data, x_feature=x_feature, y_feature=y_feature, columns=["requests-count (count)"], sort_col="count",label_factor=label_factor, descending=sort_order)   
    elif "throughput (MiB/s)" in y_feature:
        data["throughput"] = data["requests-throughput (MiB/s)"]
        label_factor = .2
        sort_order = "desc"
        graph = ioplot(data=data, x_feature=x_feature, y_feature=y_feature, columns=["requests-throughput (MiB/s)"], sort_col="throughput",label_factor=label_factor, descending=sort_order)   
    elif "iops" in y_feature:
        data["iops"] = data["requests-iops (iops)"]
        label_factor = .2
        sort_order = "desc"
        graph = ioplot(data=data, x_feature=x_feature, y_feature=y_feature, columns=["requests-iops (iops)"], sort_col="iops", label_factor=label_factor, descending=sort_order)   
    elif "PIP" in test_name:
        y_feature_short=y_feature.replace('(ms)','').replace('-','')
        data[y_feature_short] = data[y_feature]
        data = data[data['filesystem']!='elastic-san-same-zone']

        data_long = data.melt(id_vars=['filesystem','test-name'], value_vars=["venv-creation(ms)","pip-update(ms)","pytorch-install(ms)","cleanup(ms)"], var_name='python_test', value_name='timing')
        category_sum = data_long.groupby('filesystem')['timing'].sum().reset_index()
        category_sum = category_sum.sort_values(by='timing', ascending=True)
        category_order = category_sum['filesystem'].tolist()

        data_long['filesystem'] = pd.Categorical(data_long['filesystem'], categories=category_order, ordered=True)


        graph = p9.ggplot(data=data_long,mapping=p9.aes(x='filesystem', y='timing', fill='python_test')) +\
                        p9.theme(figure_size=(12, 8), axis_text_x=p9.element_text(angle = 90)) +\
                        p9.ggtitle(f"Stacked Bar Plot of {x_feature} vs Python Pytorch Install") +\
                        p9.scale_color_discrete(limits=["cleanup(ms)","pytorch-install(ms)","pip-update(ms)","venv-creation(ms)"]) +\
                        p9.scale_fill_manual(values=[ '#EE6331', '#419599','#447099','#404041']) +\
                        p9.labs(color = f"Process") +\
                        p9.ylab("Timing") +\
                        p9.xlab('Filesystem') +\
                        p9.geom_bar(stat='identity')
        # graph = p9.ggplot(data=data,mapping=p9.aes(x=f'reorder({x_feature}, {y_feature_short})', y=y_feature, shape="cloud")) +\
        #                         p9.geom_point(p9.aes(color=y_feature), size=4) +\
        #                         p9.theme(figure_size=(12, 8), axis_text_x=p9.element_text(angle = 90)) +\
        #                         p9.ggtitle(f"Scatterplot of {x_feature} vs {y_feature}") +\
        #                         p9.labs(color = f"{y_feature}\n") +\
        #                         p9.geom_text(mapping=p9.aes(y=data[y_feature]+0.1*data['label_pos']*data[y_feature],label=data[y_feature]) ) +\
        #                         p9.scale_colour_gradient(low = "#447099", high = "#EE6331", trans="log10") +\
        #                         p9.scale_y_log10() +\
        #                         p9.ylab(y_feature) +\
        #                         p9.xlab(x_feature.capitalize())
    else:
        graph = p9.ggplot(data=data,mapping=p9.aes(x=f'reorder({x_feature}, {y_feature})', y=y_feature, shape="cloud")) +\
                                p9.geom_point(p9.aes(color=y_feature), size=4) +\
                                p9.theme(figure_size=(12, 8), axis_text_x=p9.element_text(angle = 90)) +\
                                p9.ggtitle(f"Scatterplot of {x_feature} vs {test_name}") +\
                                p9.labs(color = f"{test_name}\n") +\
                                p9.geom_text(mapping=p9.aes(y=data[y_feature]+0.1*data['label_pos']*data[y_feature],label=data[y_feature]) ) +\
                                p9.scale_colour_gradient(low = "#447099", high = "#EE6331", trans="log10") +\
                                p9.scale_y_log10() +\
                                p9.ylab("seconds") +\
                                p9.xlab(x_feature.capitalize())

        # graph = p9.ggplot(data=data,mapping=p9.aes(x=f'reorder({x_feature}, {y_feature})', y=y_feature, shape="cloud")) +\
        #                         p9.geom_point(p9.aes(color=y_feature), size=4) +\
        #                         p9.theme(figure_size=(12, 8), axis_text_x=p9.element_text(angle = 90)) +\
        #                         p9.ggtitle(f"Scatterplot of {x_feature} vs {test_name}") +\
        #                         p9.labs(color = f"{test_name}\n") +\
        #                         p9.geom_text(mapping=p9.aes(y=data[y_feature]+0.1*data['label_pos']*data[y_feature],label=data[y_feature]) ) +\
        #                         p9.scale_colour_gradient(low = "#447099", high = "#EE6331", trans="log10") +\
        #                         p9.scale_y_log10() +\
        #                         p9.ylab("seconds") +\
        #                         p9.xlab(x_feature.capitalize())


    # Save plot to a BytesIO object
    buf = io.BytesIO()
    graph.save(buf, format='png') 
    buf.seek(0)

    # Encode plot as base64 string
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')

    return plot_data

@app.route('/')
def index():
    parquet_path = os.path.join(os.path.dirname(__file__), "storage-results.parquet")
    df = pd.read_parquet(parquet_path)
    # df = df.sort_values(by=['cloud','filesystem'])
    x_feature = 'filesystem'
    test_name = list(concatenated_data.keys()) #df['test-name'].unique().tolist()
    y_features = concatenated_data
    cloud_list = df['cloud'].unique().tolist()
    cloud_list.insert(len(cloud_list), "All")

    return render_template('index.html', x_feature=x_feature, y_features=y_features, cloud_filter=cloud_list, test_name=test_name)

@app.route('/scatterplot', methods=['POST'])
def scatterplot():
    parquet_path = os.path.join(os.path.dirname(__file__), "storage-results.parquet")
    df = pd.read_parquet(parquet_path)
    # df = df.sort_values(by=['cloud','filesystem'])
    x_feature = request.json['x_feature']
    y_feature = request.json['y_feature']
    cloud_filter = request.json['cloud_filter']
    test_name = request.json['test_name']
    sort_order = all_order
    
    if cloud_filter != 'All':
        df = df[df['cloud'] == cloud_filter]
        if cloud_filter == 'AWS':
            sort_order = aws_order
        elif cloud_filter == 'AZURE':
            sort_order = azure_order
        elif cloud_filter == 'GCP':
            sort_order = gcp_order
        

    filtered_df = df[df['test-name'] == test_name]

    plot_data = generate_scatterplot(filtered_df, x_feature, y_feature, sort_order)

    return jsonify({'plot_data': plot_data})   

@app.route('/plotnine', methods=['POST'])
def plotnine():
    parquet_path = os.path.join(os.path.dirname(__file__), "storage-results.parquet")
    df = pd.read_parquet(parquet_path)
    # df = df.sort_values(by=['cloud','filesystem'])
    x_feature = request.json['x_feature']
    y_feature = request.json['y_feature']
    cloud_filter = request.json['cloud_filter']
    test_name = request.json['test_name']
    sort_order = all_order
    
    if cloud_filter != 'All':
        df = df[df['cloud'] == cloud_filter]
        if cloud_filter == 'AWS':
            sort_order = aws_order
        elif cloud_filter == 'AZURE':
            sort_order = azure_order
        elif cloud_filter == 'GCP':
            sort_order = gcp_order

    if y_feature in r_perf_data["R - fsbench"]:
        test_name = y_feature.replace(" (s)","")
        y_feature = "elapsed"
    
    # if y_feature in python_perf_data["PIP venv Pytorch Install"]:
    #     test_name = y_feature.replace("(ms)","")
        

    filtered_df = df[df['test-name'] == test_name]

    plot_data = generate_plotnine(filtered_df, x_feature, y_feature, test_name, sort_order)

    return jsonify({'plot_data': plot_data})   

if __name__ == "__main__":
    app.run(debug=True)