import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "../data/vectorstore/faiss.index"
METADATA_PATH = "../data/vectorstore/metadata.json"

# Load model embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index(INDEX_PATH)

# Load metadata
with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)


def search(query, top_k=3):
    # Embed câu hỏi
    query_vector = model.encode([query], convert_to_numpy=True)
    query_vector = query_vector.astype("float32")

    # Chuẩn hóa để dùng cosine
    faiss.normalize_L2(query_vector)

    # Search
    scores, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        results.append(metadata[idx])

    return results


if __name__ == "__main__":
    while True:
        query = input("\nBạn hỏi gì (gõ 'exit' để thoát): ")

        if query.lower() == "exit":
            break

        results = search(query)

        print("\n🔎 Top đoạn liên quan:\n")

        for i, r in enumerate(results):
            print(f"--- Kết quả {i+1} ---")
            print("Chương:", r["chapter"])
            print(r["text"][:500])
            print("\n")