
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
file_path = "dataset/twitter_training.csv"

df = pd.read_csv(file_path)

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# Clean column names
df.columns = ["id", "entity", "sentiment", "text"]

# Remove missing values
df = df.dropna(subset=["sentiment", "entity"])

# Sentiment distribution
sentiment_counts = df["sentiment"].value_counts()

print("\nSentiment Distribution:")
print(sentiment_counts)

# Create output directory
os.makedirs("output", exist_ok=True)

# -------------------------------
# 1. Sentiment Distribution
# -------------------------------
plt.figure(figsize=(8, 5))

sentiment_counts.plot(kind="bar")

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("output/sentiment_distribution.png")
plt.close()

# -------------------------------
# 2. Entity-wise Sentiment
# -------------------------------
entity_sentiment = pd.crosstab(
    df["entity"],
    df["sentiment"]
)

entity_sentiment.plot(
    kind="bar",
    figsize=(14, 7)
)

plt.title("Entity-wise Sentiment Analysis")
plt.xlabel("Entity")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("output/entity_sentiment.png")
plt.close()

print("\nOutput files created successfully:")
print("output/sentiment_distribution.png")
print("output/entity_sentiment.png")
