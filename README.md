# RAG System Demo – Truyenfull Crawler

## 1. Giới thiệu

Project này xây dựng một hệ thống **Retrieval Augmented Generation (RAG)** để truy vấn nội dung truyện được crawl từ website.
Hệ thống cho phép thu thập dữ liệu từ website, xử lý dữ liệu, lưu trữ vào Vector Database và sử dụng mô hình ngôn ngữ để sinh câu trả lời dựa trên dữ liệu đã thu thập.

Quy trình hoạt động của hệ thống:

Website → Crawler → Raw Data → Chunking → Embedding → Vector Database → Retrieval → LLM → Generated Answer

Hệ thống được xây dựng bằng **Python**, sử dụng **Scrapy để crawl dữ liệu** và triển khai pipeline **RAG** để truy vấn và sinh câu trả lời.

---

# 2. Các chức năng đã hoàn thành trong hệ thống RAG

## 2.1 Crawl dữ liệu từ website

Hệ thống sử dụng **Scrapy Spider** để thu thập nội dung truyện từ website.
Spider sẽ truy cập vào các trang truyện, lấy nội dung chương truyện và lưu lại dưới dạng JSON để sử dụng cho các bước xử lý tiếp theo.

File thực hiện crawler:

spiders/truyen_spider.py

Kết quả sau khi crawl sẽ được lưu tại:

data/raw/full.json

Screenshot minh chứng:

![Crawl Data](crawl_data.png)

---

## 2.2 Chunking dữ liệu

Sau khi crawl dữ liệu, nội dung truyện được xử lý và chia thành các đoạn nhỏ (chunks).
Việc chunking giúp hệ thống RAG dễ dàng tìm kiếm các đoạn văn bản liên quan khi người dùng đặt câu hỏi.

Script thực hiện chunking:

rag/prepare_data.py

Sau khi chạy script, các chunks sẽ được lưu tại:

data/processed/chunks.json

Screenshot minh chứng:

![Chunking](chunking.png)

---

## 2.3 Lưu dữ liệu vào Vector Database

Các đoạn văn bản sau khi được chunk sẽ được chuyển thành **vector embeddings** và lưu vào **Vector Database**.
Vector database cho phép hệ thống tìm kiếm các đoạn văn bản có nội dung liên quan tới câu hỏi của người dùng.

Script xây dựng vector index:

rag/build_index.py

Sau khi chạy script này, hệ thống sẽ tạo vector index để phục vụ truy vấn trong hệ thống RAG.

Screenshot minh chứng:

![Vector Database](vector_db.png)

---

## 2.4 Hệ thống RAG trả lời câu hỏi

Hệ thống RAG cho phép người dùng nhập câu hỏi liên quan đến nội dung truyện.
Quy trình xử lý như sau:

1. Người dùng nhập câu hỏi
2. Hệ thống tìm các đoạn văn bản liên quan trong Vector Database
3. Các đoạn văn bản được đưa vào làm context cho mô hình ngôn ngữ
4. Mô hình sinh câu trả lời dựa trên dữ liệu đã crawl

Script chạy hệ thống RAG:

rag/chat.py

Screenshot minh chứng:

![RAG Answer](rag_answer.png)

---

# 3. Cấu trúc project

Cấu trúc chính của project:

project_root/

README.md
scrapy.cfg

rag_system_demo/
    README.md
    crawl_data.png
    chunking.png
    vector_db.png
    rag_answer.png

truyenfull_crawler/
    spiders/
    rag/
    data/

---

# 4. Cách cài đặt hệ thống

## Bước 1: Clone project

Chạy tại terminal:

git clone <repository_url>

Sau đó di chuyển vào thư mục project:

cd truyenfull_crawler

---

## Bước 2: Tạo môi trường ảo Python

Tại thư mục root của project:

python -m venv venv

Kích hoạt môi trường:

Windows

venv\Scripts\activate

MacOS / Linux

source venv/bin/activate

---

## Bước 3: Cài đặt thư viện cần thiết

pip install -r requirements.txt

---

# 5. Cách chạy hệ thống

Các command dưới đây được chạy **tại thư mục root của project** (cùng cấp với file `scrapy.cfg`).

---

## Bước 1: Crawl dữ liệu từ website

Chạy crawler bằng lệnh:

scrapy crawl truyen

Sau khi chạy xong, dữ liệu sẽ được lưu trong thư mục:

data/raw/

---

## Bước 2: Chunk dữ liệu

Chạy script xử lý dữ liệu:

python truyenfull_crawler/rag/prepare_data.py

Script này sẽ đọc dữ liệu từ thư mục raw và tạo các đoạn văn bản nhỏ (chunks).

Kết quả sẽ được lưu tại:

data/processed/chunks.json

---

## Bước 3: Build Vector Database

Chạy script tạo vector index:

python truyenfull_crawler/rag/build_index.py

Script này sẽ tạo embeddings từ các chunks và lưu chúng vào vector database.

---

## Bước 4: Chạy hệ thống RAG

Chạy chương trình chat:

python truyenfull_crawler/rag/chat.py

Sau khi chạy chương trình, người dùng có thể nhập câu hỏi liên quan đến nội dung truyện.
Hệ thống sẽ truy vấn dữ liệu trong vector database và sinh câu trả lời dựa trên thông tin đã crawl.

---

# 6. Tổng kết

Hệ thống đã hoàn thành các thành phần chính của một pipeline RAG:

* Crawl dữ liệu từ website
* Tiền xử lý và chunking dữ liệu
* Tạo embeddings và lưu vào vector database
* Truy vấn dữ liệu và sinh câu trả lời bằng mô hình ngôn ngữ

Pipeline này cho phép xây dựng các hệ thống hỏi đáp dựa trên dữ liệu riêng thay vì chỉ dựa vào kiến thức có sẵn của mô hình.

---
