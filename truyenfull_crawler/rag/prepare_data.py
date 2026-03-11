import json
import os

RAW_PATH = "../data/raw/full.json"
PROCESSED_PATH = "../data/processed/chunks.json"


def chunk_text(text, chunk_size=1000):
    paragraphs = text.split("\n")
    
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def main():
    with open(RAW_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("Tổng chương:", len(data))

    all_chunks = []

    for chapter in data:
        chapter_title = chapter["chapter_title"]
        content = chapter["content"]

        chunks = chunk_text(content)

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "chapter": chapter_title,
                "chunk_id": i,
                "text": chunk
            })

    print("Tổng chunks:", len(all_chunks))

    os.makedirs("../data/processed", exist_ok=True)

    with open(PROCESSED_PATH, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print("Đã lưu chunks.json")


if __name__ == "__main__":
    main()