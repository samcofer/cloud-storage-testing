from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
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


io_perf_data = {
    'ioping-linear-async-read': ["requests-count","requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-count","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
    "ioping-linear-async-write": ["requests-count","requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-count","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
    "ioping-ping": ["requests-count","requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-count","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
    "ioping-large-ping": ["requests-count","requests-time","requests-ops-volume","requests-iops","requests-throughput","generated-count","generated-time","generated-ops-volume","generated-iops","generated-throughput","min","avg","max","mdev"],
}

r_perf_data = {
    "Install MASS": ["elapsed"],
    "Install lattice": ["elapsed"],
    "Install BH": ["elapsed"],
    "Write CSV, 10KB": ["elapsed"],
    "Write CSV, 1MB": ["elapsed"],
    "Write CSV, 100MB": ["elapsed"],
    "Write CSV, 1GB": ["elapsed"],
    "Read CSV, 10KB": ["elapsed"],
    "Read CSV, 1MB": ["elapsed"],
    "Read CSV, 100MB": ["elapsed"],
    "Read CSV, 1GB": ["elapsed"],
    "DD write, 1GB, 2 Parallel Ops": ["elapsed"],
    "DD write, 1GB, 4 Parallel Ops": ["elapsed"],
    "DD write, 1GB, 8 Parallel Ops": ["elapsed"],
    "DD write, 1GB, 16 Parallel Ops": ["elapsed"],
    "DD read, 1GB, 2 Parallel Ops": ["elapsed"],
    "DD read, 1GB, 4 Parallel Ops": ["elapsed"],
    "DD read, 1GB, 8 Parallel Ops": ["elapsed"],
    "DD read, 1GB, 16 Parallel Ops": ["elapsed"],
    "Write CSV, 100MB over 10 files": ["elapsed"],
    "Read CSV, 100MB over 10 files": ["elapsed"],
    "Write CSV, 100MB over 100 files": ["elapsed"],
    "Read CSV, 100MB over 100 files": ["elapsed"],
    "Write CSV, 100MB over 1000 files": ["elapsed"],
    "Read CSV, 100MB over 1000 files": ["elapsed"],
    "Write CSV, 100MB over 10000 files": ["elapsed"],
    "Read CSV, 100MB over 10000 files": ["elapsed"],
    "DD write, 10MB over 1000 files, 2 Parallel Ops": ["elapsed"],
    "DD write, 10MB over 1000 files, 4 Parallel Ops": ["elapsed"],
    "DD write, 10MB over 1000 files, 8 Parallel Ops": ["elapsed"],
    "DD write, 10MB over 1000 files, 16 Parallel Ops": ["elapsed"],
    "DD read, 10MB over 1000 files, 2 Parallel Ops": ["elapsed"],
    "DD read, 10MB over 1000 files, 4 Parallel Ops": ["elapsed"],
    "DD read, 10MB over 1000 files, 8 Parallel Ops": ["elapsed"],
    "DD read, 10MB over 1000 files, 16 Parallel Ops": ["elapsed"],
    "FST random reads, 100MB over 10*10MB reads": ["elapsed"],
    "FST random reads, 100MB over 100*1MB reads": ["elapsed"],
    "FST random reads, 100MB over 1000*100KB reads": ["elapsed"],
    "FST random reads, 100MB over 10000*10KB reads": ["elapsed"],
    "Read 14 days of CRAN logs with fread": ["elapsed"],
    "Sample 5000 rows from each of 14 CRAN logs with vroom": ["elapsed"]
}

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


def generate_scatterplot(data, x_feature, y_feature):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=x_feature, y=y_feature, s=100, alpha=0.7)
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
    buf = io.BytesIO()
    plt.savefig(buf, format='png') 
    buf.seek(0)

    # Encode plot as base64 string
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()

    return plot_data

@app.route('/')
def index():
    df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')

    x_feature = 'filesystem'
    test_name = df['test-name'].unique().tolist()
    y_features = concatenated_data
    cloud_list = df['cloud'].unique().tolist()
    cloud_list.insert(0, "All")

    return render_template('index.html', x_feature=x_feature, y_features=y_features, cloud_filter=cloud_list, test_name=test_name)

@app.route('/scatterplot', methods=['POST'])
def scatterplot():
    x_feature = request.json['x_feature']
    y_feature = request.json['y_feature']
    cloud_filter = request.json['cloud_filter']
    test_name = request.json['test_name'] 
    
    df = pd.read_parquet('~/projects/cloud-storage-testing/results/reports/storage-results.parquet')

    if cloud_filter != 'All':
        df = df[df['cloud'] == cloud_filter]

    filtered_df = df[df['test-name'] == test_name]

    plot_data = generate_scatterplot(filtered_df, x_feature, y_feature)

    return jsonify({'plot_data': plot_data})   

if __name__ == "__main__":
    app.run(debug=True)