import os 
import pandas as pd 
path = "/Users/shmoi/.cache/kagglehub/datasets/praneshmukhopadhyay/amazon-questionanswer-dataset/versions/1"

df = pd.read_csv(path + "/single_qna.csv")

print(df.columns.tolist())