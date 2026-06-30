# Candidate Transformation Pipeline

```text
                 CSV
                  │
                  │
                 JSON
                  │
                  │
              Resume PDF
                  │
                  ▼
             Data Parsers
                  │
                  ▼
            Normalization
                  │
                  ▼
          Candidate Factory
                  │
                  ▼
        Candidate Matcher
                  │
          Same Person?
           /         \
         No           Yes
         │             │
         ▼             ▼
    Keep Separate   Merge Engine
                        │
                        ▼
              Unified Candidate
                        │
                        ▼
                 JSON Output
```
