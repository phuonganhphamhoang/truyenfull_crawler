# RAG System Demo – Truyenfull Crawler

## 1. Giới thiệu

Project này xây dựng một hệ thống **Retrieval Augmented Generation (RAG)** để truy vấn nội dung truyện được crawl từ website.

Hệ thống cho phép:

- Thu thập dữ liệu từ website
- Tiền xử lý dữ liệu
- Lưu trữ dữ liệu dưới dạng vector embeddings
- Truy vấn dữ liệu và sinh câu trả lời bằng mô hình ngôn ngữ

Pipeline hoạt động của hệ thống:

```
Website → Crawler → Raw Data → Chunking → Embedding → Vector Database → Retrieval → LLM → Generated Answer
```

Hệ thống được xây dựng bằng **Python**, sử dụng **Scrapy** để crawl dữ liệu và triển khai pipeline **RAG** để truy vấn nội dung.

---

# 2. Các chức năng đã hoàn thành trong hệ thống RAG

## 2.1 Crawl dữ liệu từ website

Hệ thống sử dụng **Scrapy Spider** để thu thập nội dung truyện từ website.  
Spider sẽ truy cập vào các trang truyện, lấy nội dung chương truyện và lưu lại dưới dạng JSON.

File crawler:

```
spiders/truyen_spider.py
```

Dữ liệu sau khi crawl sẽ được lưu tại:

```
data/raw/full.json
```

---

## 2.2 Chunking dữ liệu

Sau khi crawl dữ liệu, nội dung truyện sẽ được chia thành các đoạn nhỏ (chunks).  
Việc chia nhỏ dữ liệu giúp hệ thống RAG dễ dàng tìm kiếm các đoạn văn bản liên quan khi người dùng đặt câu hỏi.

Script thực hiện chunking:

```
rag/prepare_data.py
```

Kết quả sẽ được lưu tại:

```
data/processed/chunks.json
```

---

## 2.3 Lưu dữ liệu vào Vector Database

Các đoạn văn bản sau khi chunk sẽ được chuyển thành **vector embeddings** bằng mô hình embedding.

Các embeddings này được lưu vào **Vector Database (FAISS)** để phục vụ truy vấn ngữ nghĩa.

Script xây dựng vector index:

```
rag/build_index.py
```

Script này sẽ:

- Tạo embeddings từ các chunks
- Xây dựng FAISS index
- Lưu vector database để phục vụ truy vấn

---

## 2.4 Hệ thống RAG trả lời câu hỏi

Hệ thống cho phép người dùng nhập câu hỏi liên quan đến nội dung truyện.

Quy trình xử lý:

1. Người dùng nhập câu hỏi
2. Hệ thống chuyển câu hỏi thành vector embedding
3. Tìm các đoạn văn bản liên quan trong Vector Database
4. Đưa các đoạn văn bản làm context
5. Sinh câu trả lời dựa trên dữ liệu đã crawl

Script chạy hệ thống:

```
rag/chat.py
```

---

# 3. Cấu trúc project

```
project_root/
│
├── README.md
├── scrapy.cfg
│
├── rag_system_demo/
│   └── README.md
│
└── truyenfull_crawler/
    ├── spiders/
    ├── rag/
    └── data/
        ├── raw/
        ├── processed/
        └── vectorstore/
```

---

# 4. Cài đặt hệ thống

## Bước 1: Clone repository

```
git clone <repository_url>
```

Di chuyển vào thư mục project:

```
cd truyenfull_crawler
```

---

## Bước 2: Tạo môi trường ảo Python

```
python -m venv venv
```

Kích hoạt môi trường:

Windows:

```
venv\Scripts\activate
```

MacOS / Linux:

```
source venv/bin/activate
```

---

## Bước 3: Cài đặt thư viện cần thiết

```
pip install -r requirements.txt
```

---

# 5. Cách chạy hệ thống

Các command dưới đây được chạy **tại thư mục root của project** (cùng cấp với file `scrapy.cfg`).

---

## Bước 1: Crawl dữ liệu

```
scrapy crawl truyen
```

Dữ liệu sau khi crawl sẽ được lưu tại:

```
data/raw/
```

---

## Bước 2: Chunk dữ liệu

```
python truyenfull_crawler/rag/prepare_data.py
```

Kết quả sẽ được lưu tại:

```
data/processed/chunks.json
```

---

## Bước 3: Build Vector Database

```
python truyenfull_crawler/rag/build_index.py
```

Script này sẽ tạo embeddings từ các chunks và lưu vào vector database.

---

## Bước 4: Chạy hệ thống RAG

```
python truyenfull_crawler/rag/chat.py
```

Sau khi chương trình chạy, người dùng có thể nhập câu hỏi liên quan đến nội dung truyện.  
Hệ thống sẽ truy vấn dữ liệu trong vector database và sinh câu trả lời dựa trên thông tin đã crawl.

---

# 6. Tổng kết

Hệ thống đã hoàn thành các thành phần chính của một pipeline **Retrieval Augmented Generation (RAG)**:

- Crawl dữ liệu từ website
- Tiền xử lý và chunking dữ liệu
- Tạo embeddings và lưu vào vector database
- Truy vấn dữ liệu và sinh câu trả lời bằng mô hình ngôn ngữ

Pipeline này cho phép xây dựng các hệ thống **hỏi đáp dựa trên dữ liệu riêng**, thay vì chỉ dựa vào kiến thức có sẵn của mô hình ngôn ngữ.
