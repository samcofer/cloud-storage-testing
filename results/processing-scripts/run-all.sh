#!/bin/bash

# ## declare an array variable
# declare -a arr=("azure" "aws")

# ## now loop through the above array
# for i in "${arr[@]}"
# do
#     python ./results/processing-scripts/python-parsing.py \
#     ./results/raw-data/$i/python-testing/ \
#     ./results/processed/$i-python-result.csv
#     python ./results/processing-scripts/ioping-parsing.py \
#     ./results/raw-data/$i/io-testing/ \
#     ./results/processed/$i-io-result.csv 
#     python ./results/processing-scripts/r-parsing.py \
#     ./results/raw-data/$i/r-testing/ \
#     ./results/processed/$i-r-result.csv 
#     python ./results/processing-scripts/app-parsing.py \
#     ./results/raw-data/$i/app-testing/ \
#     ./results/processed/$i-app-result.csv 

# done



python ./results/processing-scripts/parque-conversion.py \
./results/processed/ \
./results/reports/storage-results.parquet