# Candidate Data Transformer

A modular Python application that transforms candidate data from multiple sources (CSV, JSON, and Resume PDF) into a unified candidate profile.

---

## Project Overview

Recruiters often receive candidate information from multiple platforms. This project demonstrates how to:

- Parse candidate data from different sources
- Normalize inconsistent data
- Match duplicate candidates
- Merge candidate profiles intelligently
- Generate a unified JSON profile

---

## Features

- CSV Candidate Parser
- JSON Candidate Parser
- Resume PDF Parser
- Candidate Factory Pattern
- Data Normalization
- Candidate Matching Engine
- Intelligent Merge Engine
- Skill Extraction
- Confidence Scoring
- Output JSON Generation
- Logging

---

## Project Structure

```
candidate-data-transformer/
│
├── data/
│   ├── input/
│   └── output/
│
├── docs/
├── logs/
├── samples/
│   ├── resumes/
│   ├── candidates.csv
│   └── candidates.json
│
├── src/
│   ├── confidence/
│   ├── logging_utils/
│   ├── matcher/
│   ├── merger/
│   ├── models/
│   ├── normalizers/
│   ├── parsers/
│   ├── utils/
│   └── main.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

## Workflow

```
CSV
     \
JSON ----\
          \
Resume ----> Normalize
             ↓
      Candidate Factory
             ↓
      Candidate Matcher
             ↓
       Merge Engine
             ↓
      Unified Candidate
             ↓
       JSON Output
```

---

## Installation

```bash
git clone <repository-url>

cd candidate-data-transformer

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run

```bash
python src/main.py
```

---

## Sample Output

```
MERGED CANDIDATE

Name : Aryan Ganesh

Email : aryanganesh13@gmail.com

Phone : 636133418

Skills

- Python
- SQL
- React
- Git
```

---

## Technologies Used

- Python
- Pandas
- Pydantic
- pdfplumber
- Regex
- Logging

---

## Future Improvements

- NLP-based Skill Extraction
- OCR Support
- REST API
- Database Integration
- Web Interface

---

## Author

Gurunath Rachannavar
