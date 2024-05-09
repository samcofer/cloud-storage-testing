from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import adjustText as adjust_text
from sklearn.datasets import load_iris
import plotnine as p9
import io
import base64
import json

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
'gfs-ent-ssd' 
]

io_perf_data = {
    'ioping-linear-async-read': ["requests-count","requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-count","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
    "ioping-linear-async-write": ["requests-count","requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-count","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
    "ioping-ping": ["requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
    "ioping-large-ping": ["requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
}

r_perf_data = {'R - fsbench': [
    'Install MASS', 'Install lattice', 'Install BH', 'Write CSV, 10KB', 'Write CSV, 1MB', 
    'Write CSV, 100MB', 'Write CSV, 1GB', 'Read CSV, 10KB', 'Read CSV, 1MB', 'Read CSV, 100MB', 
    'Read CSV, 1GB', 'DD write, 1GB, 2 Parallel Ops', 'DD write, 1GB, 4 Parallel Ops', 
    'DD write, 1GB, 8 Parallel Ops', 'DD write, 1GB, 16 Parallel Ops', 'DD read, 1GB, 2 Parallel Ops', 
    'DD read, 1GB, 4 Parallel Ops', 'DD read, 1GB, 8 Parallel Ops', 'DD read, 1GB, 16 Parallel Ops', 
    'Write CSV, 100MB over 10 files', 'Read CSV, 100MB over 10 files', 'Write CSV, 100MB over 100 files', 
    'Read CSV, 100MB over 100 files', 'Write CSV, 100MB over 1000 files', 'Read CSV, 100MB over 1000 files', 
    'Write CSV, 100MB over 10000 files', 'Read CSV, 100MB over 10000 files', 
    'DD write, 10MB over 1000 files, 2 Parallel Ops', 'DD write, 10MB over 1000 files, 4 Parallel Ops', 
    'DD write, 10MB over 1000 files, 8 Parallel Ops', 'DD write, 10MB over 1000 files, 16 Parallel Ops', 
    'DD read, 10MB over 1000 files, 2 Parallel Ops', 'DD read, 10MB over 1000 files, 4 Parallel Ops', 
    'DD read, 10MB over 1000 files, 8 Parallel Ops', 'DD read, 10MB over 1000 files, 16 Parallel Ops', 
    'FST random reads, 100MB over 10*10MB reads', 'FST random reads, 100MB over 100*1MB reads', 
    'FST random reads, 100MB over 1000*100KB reads', 'FST random reads, 100MB over 10000*10KB reads', 
    'Read 14 days of CRAN logs with fread', 'Sample 5000 rows from each of 14 CRAN logs with vroom'
]}

python_perf_data = {
    "PIP venv Pytorch Install": ["venv-creation(ms)","pip-update(ms)","pytorch-install(ms)","cleanup(ms)"]
}

app_perf_data = {
    "acl-and-lock-testing": ["extended-acl-support","linkbased-file-locks"]
}

concatenated_data = {}
concatenated_data.update(io_perf_data)
concatenated_data.update(r_perf_data)
concatenated_data.update(python_perf_data)
concatenated_data.update(app_perf_data)

def filesystem_sorter(column):
    """Sort function"""
    correspondence = {team: order for order, team in enumerate(all_order)}
    return column.map(correspondence)


def generate_scatterplot(data, x_feature, y_feature, order):
    sns.set(style="whitegrid")
    fig=plt.figure(figsize=(10, 6), layout="tight")
    data = data.sort_values(by='filesystem', key=filesystem_sorter)
    sns.scatterplot(data=data, x=x_feature, y=y_feature, s=100, alpha=0.7, hue_order=order)
    plt.title(f"Scatterplot of {x_feature} vs {y_feature}")
    # Add labels and title
    plt.xlabel(x_feature)
    plt.ylabel(y_feature + '(ms)')


    plt.ylim(0, max(data[y_feature])+(.1*max(data[y_feature]))) 
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

def generate_plotnine(data, x_feature, y_feature, order):
    
    data = data.sort_values(by='filesystem', key=filesystem_sorter)
    data['filesystem'] = pd.Categorical(data.filesystem, categories=pd.unique(data.filesystem))

    graph = p9.ggplot(data=data,
            mapping=p9.aes(x=y_feature,
                            y=x_feature)) +\
                                p9.geom_point() +\
                                p9.theme(figure_size=(10, 6)) +\
                                p9.ggtitle(f"Scatterplot of {x_feature} vs {y_feature}") +\
                                p9.geom_text(mapping=p9.aes(label=data[y_feature]), nudge_x=0, adjust_text={'expand':(2, 2),'arrowprops':{'arrowstyle':'-','color':'red'} })


    # Save plot to a BytesIO object
    buf = io.BytesIO()
    graph.save(buf, format='png') 
    buf.seek(0)

    # Encode plot as base64 string
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')

    return plot_data

@app.route('/')
def index():
    df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')
    # df = df.sort_values(by=['cloud','filesystem'])
    x_feature = 'filesystem'
    test_name = df['test-name'].unique().tolist()
    y_features = concatenated_data
    cloud_list = df['cloud'].unique().tolist()
    cloud_list.insert(0, "All")

    return render_template('index.html', x_feature=x_feature, y_features=y_features, cloud_filter=cloud_list, test_name=test_name)

@app.route('/scatterplot', methods=['POST'])
def scatterplot():
    df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')
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
    df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')
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

    plot_data = generate_plotnine(filtered_df, x_feature, y_feature, sort_order)

    return jsonify({'plot_data': plot_data})   

if __name__ == "__main__":
    app.run(debug=True)