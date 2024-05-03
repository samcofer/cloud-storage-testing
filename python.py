from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import io
import base64
import json
import os
import pandas as pd


filter_type = "sepal"

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

if filter_type == 'sepal':
    iris_df = iris_df[[col for col in iris_df.columns if 'sepal' in col]]
elif filter_type == 'petal':
    iris_df = iris_df[[col for col in iris_df.columns if 'petal' in col]]

print("messages here")
print(iris_df.columns)
