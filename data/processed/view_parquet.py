# import pandas as pd

# df = pd.read_parquet("data/processed/market_tweets.parquet")
# print(df.head())
# print(df.columns)
# print(len(df))
import pandas as pd

df = pd.read_parquet("market_tweets.parquet")
df.to_csv("market_tweets_preview.csv", index=False)