import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(user_skills, user_education, user_exp):
    df = pd.read_csv("data/jobs.csv")

    user_text = f"{user_skills} {user_education} {user_exp}"

    df["combined"] = df["skills"] + " " + df["education"] + " " + df["experience"].astype(str)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(df["combined"].tolist() + [user_text])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    df["score"] = similarity[0]

    return df.sort_values(by="score", ascending=False).head(5)[
        ["job_title", "score"]
    ]
