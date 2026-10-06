from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff("data/Training Dataset.arff")

df = pd.DataFrame(data)

for column in df.columns:
    if df[column].dtype == object:
        df[column] = df[column].apply(
            lambda x: x.decode("utf-8") if isinstance(x, bytes) else x
        )

df.to_csv("data/dataset.csv", index=False)

print("Dataset converted successfully!")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())