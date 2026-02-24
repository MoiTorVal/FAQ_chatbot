import pandas as pd 
import os
import kagglehub

def load_faq_data(category="Electronics", max_rows=1000):
    # Auto download from kaggle
    path = kagglehub.dataset_download("praneshmukhopadhyay/amazon-questionanswer-dataset")
    full_path = os.path.join(path, "single_qna.csv")
    
    df = pd.read_csv(full_path)

    # Filter category
    df = df[df['Category'] == category]

    # Keep only question and answers
    df = df[['Question', 'Answer']].dropna()

    # Limit rows
    df = df.head(max_rows)

    print(f"Loaded {len(df)} FAQ pairs for category: {category}")

    return df

if __name__ == "__main__":
    df = load_faq_data()
    print(df.head())

    # Create directory if not exists
    os.makedirs("data", exist_ok=True)

    # Save filtered data
    df.to_csv('data/faq_small.csv', index=False)
    print("Saved filtered data to data/faq_small.csv")