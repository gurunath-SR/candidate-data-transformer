# 🚀 Candidate Data Transformer

A modular Python application that parses candidate information from multiple sources (CSV, JSON, Resume PDF, and LinkedIn), normalizes inconsistent data, intelligently matches duplicate profiles, and generates a unified candidate profile with confidence scoring, resume quality analysis, and recruiter-friendly summaries.

---

# 📌 Project Objective

Recruiters often receive candidate information from multiple platforms such as:

- Resume PDFs
- CSV exports
- JSON APIs
- LinkedIn profiles

These sources usually contain inconsistent, duplicate, or incomplete information.

The objective of this project is to automatically:

- Parse candidate data from multiple sources
- Normalize inconsistent fields
- Detect duplicate candidates
- Merge candidate profiles intelligently
- Remove duplicate skills, education, and experience
- Generate a unified candidate profile
- Calculate profile confidence
- Evaluate resume completeness
- Rank candidates for recruiters

---

# ✨ Features

### ✅ Multi-Source Parsing

- CSV Parser
- JSON Parser
- Resume PDF Parser
- LinkedIn Profile Parser

---

### ✅ Data Normalization

- Name normalization
- Email normalization
- Phone normalization
- Location normalization

---

### ✅ Candidate Matching

Matches duplicate candidates using:

- Email Matching
- Phone Matching
- Name Similarity

---

### ✅ Intelligent Merge Engine

Merges information from multiple sources while preserving the most reliable values.

Includes:

- Field-level confidence selection
- Duplicate skill removal
- Duplicate experience removal
- Duplicate education removal
- Provenance tracking

---

### ✅ Resume Analysis

Automatically extracts:

- Name
- Email
- Phone
- Location
- Skills
- GitHub
- LinkedIn
- Headline
- Experience
- Education

---

### ✅ Candidate Quality Metrics

- Resume Quality Score
- Overall Confidence Score
- Field Confidence
- Candidate Ranking Score

---

### ✅ Recruiter Summary

Generates a clean recruiter-friendly profile instead of raw JSON.

Example:

```
Candidate ID : CAN-1D4ECFCC2B

Name : Aryan Ganesh

Email : aryanganesh13@gmail.com

Phone : 6361334168

Location : Bangalore

Skills

• Python
• React
• SQL
• Machine Learning

Resume Score : 50%

Candidate Rank : Good Candidate
```

---

### ✅ Logging

Pipeline execution logs every major step.

Example:

```
Reading CSV Candidate

Reading Resume Candidate

Matching Candidate

Candidate Matched

Output Saved Successfully
```

---

### ✅ Unit Testing

Includes pytest test cases for:

- Normalizers
- Candidate Matcher
- Merge Engine

---

# 🏗 Project Architecture

```
                CSV Candidate
                     │
                     │
                JSON Candidate
                     │
                     │
               Resume PDF
                     │
                     │
             LinkedIn Profile
                     │
                     ▼
              Source Parsers
                     │
                     ▼
             Data Normalization
                     │
                     ▼
            Candidate Factory
                     │
                     ▼
           Candidate Matcher
                     │
                     ▼
         Intelligent Merge Engine
                     │
                     ▼
      Confidence & Quality Scoring
                     │
                     ▼
          Candidate Ranking Engine
                     │
                     ▼
         Recruiter Summary Report
                     │
                     ▼
        Unified Candidate JSON
```

---

# 📂 Project Structure

```
candidate-data-transformer/

│
├── data/
│   ├── output/
│   │      merged_candidate.json
│   │
│   └── logs/
│          pipeline.log
│
├── docs/
│
├── samples/
│   ├── candidates.csv
│   ├── candidates.json
│   ├── resumes/
│   └── linkedin/
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
│
├── requirements.txt
│
├── pytest.ini
│
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Pydantic | Candidate Data Models |
| pdfplumber | Resume PDF Parsing |
| Regular Expressions | Information Extraction |
| Logging | Pipeline Monitoring |
| Pytest | Unit Testing |
| JSON | Unified Output Format |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/gurunath-SR/candidate-data-transformer.git
```

Move into the project

```bash
cd candidate-data-transformer
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
python src/main.py
```

---

# 🧪 Run Tests

```bash
pytest
```

Example:

```
========================

5 passed

========================
```

---

# 📄 Sample Output

```
======================================================================
MERGED CANDIDATE
======================================================================

Candidate ID : CAN-1D4ECFCC2B

Name : Aryan Ganesh

Email : aryanganesh13@gmail.com

Phone : 6361334168

Location : Bangalore

Skills

• Python
• React
• SQL
• Git
• Machine Learning

Overall Confidence : 0.56

Resume Quality Score : 50%

Candidate Ranking : Good Candidate
```

---

# 📈 Current Capabilities

✔ CSV Parsing

✔ JSON Parsing

✔ Resume PDF Parsing

✔ LinkedIn Parsing

✔ Candidate Matching

✔ Intelligent Profile Merge

✔ Candidate ID Generation

✔ Confidence Scoring

✔ Resume Quality Analysis

✔ Candidate Ranking

✔ Recruiter Summary Generation

✔ Skill Deduplication

✔ Experience Deduplication

✔ Education Deduplication

✔ Logging

✔ Unit Testing

---

# 🔮 Future Enhancements

- NLP-based Skill Extraction using spaCy
- OCR Support for Scanned Resumes
- REST API using FastAPI
- PostgreSQL Integration
- Docker Containerization
- Kubernetes Deployment
- Machine Learning Based Candidate Ranking
- Web Dashboard
- Bulk Resume Processing

---

# 👨‍💻 Author

**Gurunath Rachannavar**

GitHub: https://github.com/gurunath-SR

---

⭐ If you found this project useful, consider giving it a star!
