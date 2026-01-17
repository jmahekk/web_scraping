from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(texts):
    vectorizer = TfidfVectorizer(
        max_features=5000,
        min_df=2,
        stop_words="english"
    )
    matrix = vectorizer.fit_transform(texts)
    return matrix, vectorizer
