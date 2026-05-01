# 🚀 Groq CLI

Simple CLI tool untuk berinteraksi dengan API Groq langsung dari terminal menggunakan Python.

Tool ini memudahkan kamu mengirim prompt ke LLM tanpa perlu bikin script berulang.

---

## ✨ Features

- ⚡ Akses Groq API langsung dari terminal
- 🎯 Support pemilihan model
- 🧠 Support role (system/user)
- 🔑 API key via environment variable
- 🪶 Lightweight (single script)

---

## 📦 Installation

Clone repository:

```bash
git clone https://github.com/farisalfatih/groq-cli.git
cd groq-cli
```

(Optional) buat virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup API Key

Set environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

Atau gunakan file `.env`:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Jalankan CLI:

```bash
python groq_cli.py
```

Contoh interaksi:

```bash
Enter prompt: Jelaskan apa itu machine learning
Model: llama3-8b
Role: user
```

---

## ⚙️ Cara Kerja

1. User memasukkan prompt via terminal  
2. Script mengirim request ke Groq API  
3. Response dari model langsung ditampilkan di CLI  

---

## 📁 Project Structure

```
groq-cli/
│── groq_cli.py
│── requirements.txt
│── README.md
```

---

## 🚧 Limitations

- Tidak ada memory/session chat
- Belum support streaming response
- Masih single-file (belum modular)

---

## 🛠️ Future Improvements

- [ ] Chat mode (loop interaktif)
- [ ] Streaming response
- [ ] Config file (.yaml / .json)
- [ ] Multi-model preset
- [ ] Plugin system

---

## 🧠 Kenapa ini penting (Data Engineering POV)

CLI seperti ini penting di data engineering karena:

- Bisa dipakai untuk automation pipeline (ETL/ELT)
- Cocok untuk enrichment data teks
- Bisa diintegrasikan ke Linux workflow (cron, bash, airflow)
- Jadi jembatan antara data pipeline dan LLM

Kalau dikembangkan, bisa jadi:
👉 AI-powered data processing CLI tool

---

## 📜 License

MIT License
