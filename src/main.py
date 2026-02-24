import kagglehub

# Download latest version
path = kagglehub.dataset_download("praneshmukhopadhyay/amazon-questionanswer-dataset")

print("Path to dataset files:", path)