import chromadb
import pandas as pd 

def build_vector_store(faq_path='data/faq_small.csv'):
    # load data
    df = pd.read_csv(faq_path)

    # initialize ChromaDB client
    client = chromadb.PersistentClient(path="data/chroma_db")

    # delete collection if it already exists (to avoid duplicates)
    try:
        client.delete_collection(name="faq")
        print("Cleared existing collection")
    except:
        pass

    # create collection
    collection = client.create_collection(name="faq")

    # add in batches of 100 to avoid memory issues
    batch_size = 100
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i+batch_size]
        collection.add(
            documents=batch['Question'].tolist(),
            metadatas=[{"answer": a} for a in batch['Answer'].tolist()],
            ids=[str(j) for j in range(i, i+len(batch))]
        )
        print(f"Stored batch {i//batch_size + 1}")

    print(f"Successfully stored {len(df)} FAQ pairs in ChromaDB")
    return collection

if __name__ == "__main__":
    build_vector_store()