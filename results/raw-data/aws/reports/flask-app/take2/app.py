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



def generate_scatterplot(data, x_feature, y_feature):
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x=x_feature, y=y_feature, hue="species", palette="Set2", s=100, alpha=0.7)
    plt.title(f"Scatterplot of {x_feature} vs {y_feature}")
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    plt.legend(title='Species', loc='upper right')

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
    iris = load_iris()
    features = iris.feature_names
    # Separate sepal and petal features for the filter
    sepal_features = [feat for feat in features if 'sepal' in feat.lower()]
    petal_features = [feat for feat in features if 'petal' in feat.lower()]

    return render_template('index.html', x_features=features, y_features=features, sepal_features=sepal_features, petal_features=petal_features)

@app.route('/scatterplot', methods=['POST'])
def scatterplot():
    x_feature = request.json['x_feature']
    y_feature = request.json['y_feature']
    filter_type = request.json['filter_type']

    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target
    iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    if filter_type == 'sepal':
        iris_df = iris_df[[col for col in iris_df.columns if ('sepal' in col.lower() or col == 'species')]]
    elif filter_type == 'petal':
        iris_df = iris_df[[col for col in iris_df.columns if ('petal' in col.lower() or col == 'species')]]

    plot_data = generate_scatterplot(iris_df, x_feature, y_feature)

    return jsonify({'plot_data': plot_data}) 

if __name__ == "__main__":
    app.run(debug=True)