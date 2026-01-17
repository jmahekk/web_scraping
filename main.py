import pandas as pd
from processing.cleaner import clean_text
from processing.vectorizer import build_tfidf
from analysis.signals import generate_composite_signal
from analysis.visualize import plot_signal


df = pd.read_csv("data/raw/stock_tweets.csv")


keywords = "nifty|sensex|banknifty|intraday"
df = df[df["Tweet"].str.contains(keywords, case=False, na=False)]


df["cleaned_tweet"] = df["Tweet"].apply(clean_text)
df = df[df["cleaned_tweet"] != ""]


df = df.drop_duplicates(subset=["cleaned_tweet"])


df.to_parquet("data/processed/market_tweets.parquet", index=False)


tfidf_matrix, _ = build_tfidf(df["cleaned_tweet"])
signal, low_ci, high_ci = generate_composite_signal(tfidf_matrix)


plot_signal(signal, low_ci, high_ci)

print("Qode assignment pipeline executed successfully.")
