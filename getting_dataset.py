import json
import os
import urllib.request
import pandas as pd

def load_amazon_data(category="Electronics", split_size=10000, save_dir="huggignfacedataset"):
    """
    Fetches reviews from McAuley-Lab/Amazon-Reviews-2023 dataset on Hugging Face
    via streaming for the specified category, sorts them chronologically, and saves locally.
    """
    print(f"Downloading Amazon Reviews 2023 ({category}) data (Limit: {split_size})...")
    url = f"https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023/resolve/main/raw/review_categories/{category}.jsonl"
    
    records = []
    req = urllib.request.urlopen(url)
    try:
        for _ in range(split_size):
            line = req.readline()
            if not line:
                break
            data = json.loads(line)
            records.append({
                'text': data.get('text', ''),
                'timestamp': data.get('timestamp', 0),
                'rating': data.get('rating', 0.0)
            })
    finally:
        req.close()
    
    # Create DataFrame
    processed_df = pd.DataFrame(records)
    
    # Chronological sorting (To prevent data leakage and ensure temporal awareness)
    processed_df = processed_df.sort_values('timestamp').reset_index(drop=True)
    
    # Create directory and save file
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, f"amazon_reviews_{category}.csv")
        processed_df.to_csv(save_path, index=False, encoding='utf-8')
        print(f"Dataset successfully saved to '{save_path}'.")
    
    print(f"Successfully loaded and chronologically sorted {len(processed_df)} reviews.")
    return processed_df

if __name__ == "__main__":
    df_train = load_amazon_data("Electronics", 5000)
    print("\nLoaded Dataset Summary:")
    print(df_train.info())
    print("\nFirst 5 Rows:")
    print(df_train.head())

