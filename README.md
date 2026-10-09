# Moroccan Darija Sentiment Analysis

**An end-to-end Natural Language Processing (NLP) project for classifying Moroccan Darija YouTube comments as positive, negative, or neutral.**

This project investigates sentiment analysis for an under-resourced, non-standardized dialect that can be written in Arabic script, Latin transliteration (Arabizi), or a mixture of both. It covers the complete workflow: **data collection, linguistic cleaning, human-assisted annotation, exploratory analysis, machine learning, Transformer fine-tuning, and a web application**.

## Project highlights

| Highlight | Result |
| --- | --- |
| Raw YouTube comments collected | ~130,000 |
| Final annotated dataset | **83,411 comments** |
| Sentiment classes | Positive, Negative, Neutral |
| Manually annotated gold dataset | 1,600 comments |
| Agreement between LLM labels and human validation | **94.82%** |
| Model/vectorization configurations evaluated | 25+ |
| Selected deployable classical model | **Stacking (SVM + Logistic Regression + Naive Bayes)** |
| Highest reported Transformer score | **DarijaBERT — 0.743 weighted F1** |

*Results are taken from the accompanying academic project report (2025–2026).*

## The problem

Moroccan Darija is challenging for traditional NLP systems because it has no single standardized spelling, includes Arabic and Latin/Arabizi writing, frequently mixes languages, and relies on cultural context, irony, and implicit sentiment. The goal is to build and evaluate a reliable pipeline that can recognize sentiment in real-world Darija comments.

## End-to-end workflow

```text
YouTube Data API v3
        |
        v
Collection (~130,000 raw comments)
        |
        v
Cleaning, normalization and Darija filtering
        |
        v
Manual gold set + Gemini-assisted pre-annotation
        |
        v
Human review and correction in Label Studio
        |
        v
Final dataset (83,411 annotated comments)
        |
        v
Vectorization (BoW, TF-IDF word/char, embeddings)
        |
        v
Classical ML, ensembles and Transformer fine-tuning
        |
        v
Evaluation and experiment tracking (MLflow / W&B)
        |
        v
Python backend + Angular frontend
```

### 1. Data collection and preparation

- Collected public comments from diverse Moroccan YouTube channels using **YouTube Data API v3**.
- Removed irrelevant content, duplicate comments, URLs, mentions, spam and other noise.
- Normalized Arabic and Latin/Arabizi text and applied Darija-specific linguistic filtering.
- Preserved negation markers that can reverse sentiment polarity.

### 2. Annotation and quality control

- Built a **1,600-comment** manually labeled reference set.
- Used **Gemini-assisted pre-annotation**, followed by review and corrections in **Label Studio**.
- Produced a final dataset of **83,411** comments with three sentiment classes:

| Sentiment | Comments |
| --- | ---: |
| Positive | 28,622 |
| Negative | 27,827 |
| Neutral | 26,962 |
| **Total** | **83,411** |

### 3. Modeling and experimentation

- **Text representations:** Bag of Words, TF-IDF (word and character n-grams), Word2Vec/FastText embeddings.
- **Classical models:** Linear SVM, Logistic Regression, Naive Bayes, Random Forest, XGBoost, LightGBM.
- **Ensemble methods:** Voting, Stacking, and combined word/character TF-IDF features.
- **Transformers:** Fine-tuning and comparing **DarijaBERT** and **AraBERT**.
- **Experiment tracking:** MLflow and Weights & Biases.

## Results

| Model | Evaluation metric | Reported score |
| --- | --- | ---: |
| Linear SVM + TF-IDF (phase 1) | Test macro F1 | 0.6877 |
| Word + Character TF-IDF SVM | Test macro F1 | **0.7326** |
| **Stacking (SVM + LR + NB)** | Test macro F1 | **0.7293** |
| AraBERT | Weighted F1 | 0.708 |
| **DarijaBERT** | **Weighted F1** | **0.743** |

**Model choice:** The Stacking model was selected as a practical classical solution for its balance of performance, robustness and deployment simplicity. DarijaBERT achieved the highest reported Transformer score.

> **Metric note:** The report presents *macro F1* for classical models and *weighted F1* for Transformers. These values should not be interpreted as a strictly like-for-like comparison.

## Technology stack

| Area | Technologies |
| --- | --- |
| Programming and analysis | Python, Jupyter Notebook |
| Data collection | YouTube Data API v3 |
| Annotation | Label Studio, Gemini-assisted labeling |
| Machine learning | scikit-learn, XGBoost, LightGBM |
| Deep learning | Hugging Face Transformers (DarijaBERT, AraBERT) |
| Experiment tracking | MLflow, Weights & Biases |
| Application | Python backend, Angular frontend |

## Repository structure

```text
.
├── Data_Collect/                     # Data-collection work
├── sentiment-app/
│   ├── backend/
│   │   ├── main.py                  # Python backend entry point
│   │   ├── requirements.txt         # Backend Python dependencies
│   │   └── stacking_svm_lr_nb.pkl   # Serialized stacking model
│   └── frontend/
│       └── sentiment-ui/            # Angular application
│           ├── src/
│           ├── public/
│           ├── angular.json
│           └── package.json
├── nettoyage.ipynb
├── labelisation.ipynb
├── ml_classique.ipynb
├── notebook_models.ipynb
├── final_workflow_&_final_analysis.ipynb
└── README.md
```

*Directory names reflect the project structure shown in VS Code; actual data files and notebooks may vary.*

## Run locally

**Prerequisites:** Python, Node.js/npm, and the saved model artifact required by the backend. Use versions compatible with the project's dependency files.

### Backend

From the repository root:

```bash
cd sentiment-app/backend
python -m venv .venv
```

Activate the virtual environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Then install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

**Starting the backend depends on the code in `main.py`.** If it defines a FastAPI application named `app` and the requirements include Uvicorn, start it with:

```bash
python -m uvicorn main:app --reload
```

If a different server/framework is used, adjust this command to match `main.py`.

### Frontend

Open a **second terminal** from the repository root:

```bash
cd sentiment-app/frontend/sentiment-ui
npm ci
npx ng serve
```

Angular commonly serves the app at `http://localhost:4200`. Verify that the frontend's API configuration points to the backend URL used on your computer.

> **Setup note:** The application startup instructions above are based on the visible folder structure, not a source-code audit. Confirm the server command, ports, API route and any environment variables in `main.py` and the Angular files before treating this section as fully tested.

## Limitations and next steps

- Sarcasm, irony, implicit sentiment and mixed-language text remain difficult to classify.
- Neutral and negative comments are particularly easy to confuse.
- Improve annotation reliability through double human annotation and inter-annotator agreement.
- Extend the dataset beyond YouTube and further improve Arabic/Arabizi coverage.
- Explore specialized or context-aware models and validate performance on independently collected data.

## Academic context

Developed as part of the **Natural Language Processing** module at **ENSA Khouribga, Sultan Moulay Slimane University**, during the **2025–2026 academic year**.

**Project contributors:** Ihsane Foudal, Kadidiatou Dem, Nawal Ait-Tami and Hiba El Hamdani.  
**Academic supervisor:** Pr. Imad Hafidi.

---

