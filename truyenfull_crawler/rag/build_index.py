import json
import os
import numpy as np
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = "data/processed/chunks.json"
INDEX_PATH = "../data/vectorstore/faiss.index"
METADATA_PATH = "../data/vectorstore/metadata.json"

# Load model embedding local
model = SentenceTransformer("all-MiniLM-L6-v2")


def main():
    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print("Tổng chunks:", len(chunks))

    texts = [chunk["text"] for chunk in chunks]

    print("Đang tạo embeddings...")

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    embeddings = embeddings.astype("float32")

    dimension = embeddings.shape[1]

    # Dùng cosine similarity chuẩn hơn L2
    index = faiss.IndexFlatIP(dimension)

    # Chuẩn hóa vector để dùng cosine
    faiss.normalize_L2(embeddings)

    index.add(embeddings)

    os.makedirs("../data/vectorstore", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(METADATA_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False)

    print("Đã build FAISS index thành công!")


if __name__ == "__main__":
    main()