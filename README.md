# Invoice Reimbursement System Documentation

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Technology Stack](#technology-stack)
5. [Setup and Installation](#setup-and-installation)
6. [Configuration](#configuration)
7. [Usage](#usage)

   * [Running the Backend API](#running-the-backend-api)
   * [Running the Frontend (Streamlit)](#running-the-frontend-streamlit)
8. [API Endpoints](#api-endpoints)
9. [File Structure](#file-structure)
10. [Error Handling & Logging](#error-handling--logging)
11. [Testing](#testing)
12. [Troubleshooting](#troubleshooting)
13. [Future Enhancements](#future-enhancements)
14. [Contributors](#contributors)
15. [License](#license)

---

## Overview

The Invoice Reimbursement System is a web-based application designed to automate the analysis and querying of employee expense invoices against company policy documents. It provides:

* *Invoice Analysis*: Upload a company policy PDF and a ZIP of invoices; receive detailed reimbursement decisions.
* *Chat Assistant*: Contextual chat interface for follow-up queries about past analyses.
* *System Health*: Endpoint and UI to verify service availability.
* ![WhatsApp Image 2025-06-13 at 10 10 13_4ea18750](https://github.com/user-attachments/assets/011d9f61-2d4c-4df0-a1eb-ce44bdf74d0b)
* ![WhatsApp Image 2025-06-13 at 10 12 43_586780bd](https://github.com/user-attachments/assets/8e3b6453-3d07-4a69-a229-d06a000b84fc)
* ![WhatsApp Image 2025-06-13 at 10 13 32_19e422bb](https://github.com/user-attachments/assets/8d5f44a2-073f-48cc-9564-b765042a177b)



## Features

* *Policy Compliance*: Compare each invoice against the policy to determine reimbursable amounts.
* *Automated Classification*: Uses a generative AI model (Google Gemini) to interpret policies and invoices.
* *Vector Store*: Stores past analyses for retrieval and contextual chat.
* *Rich Frontend*: Interactive dashboards via Streamlit for non-technical users.
* *RESTful API*: FastAPI backend exposing endpoints for integration.

## Architecture

plaintext
+-------------+       HTTP       +---------------+       AI calls      +----------------+
|   Streamlit | <--------------> | FastAPI App   | <------------------> | AI / LLM Model |
|   Frontend  |                   |   Backend     |                     |  (Google Gemini)|
+-------------+                   +---------------+                     +----------------+
        |                                  |
        |                                  +--> MongoDB (Vector Store)
        |                                  |
        +--> User uploads PDFs & ZIPs      +--> File Temp Storage


## Technology Stack

* *Python 3.13*
* *FastAPI*: High-performance backend framework
* *Uvicorn*: ASGI server
* *Streamlit*: Frontend dashboard
* *Google Generative AI (Gemini)*: LLM for analysis
* *MongoDB*: Persistent vector store via pymongo
* *Sentence-Transformers*: Embeddings for chat context
* *Python-Multipart*: Handling file uploads
* *PyPDF2*: Extract text from PDFs
* *Zipfile36*: Unzip invoice archives
* *python-dotenv*: Environment variable management

## Setup and Installation

### Prerequisites

* macOS or Linux with Python 3.13 installed
* Git

bash
git clone <repo-url>
cd invoice_system
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo "GEMINI_API_KEY=YOUR_KEY" > .env
echo "MONGODB_CONNECTION_STRING=YOUR_CONN" >> .env


## Configuration

Environment variables in the .env file:

dotenv
GEMINI_API_KEY=<your Google Gemini API key>
MONGODB_CONNECTION_STRING=<your MongoDB URI>


Load these in shell with:

bash
set -a && source .env && set +a


## Usage

### Running the Backend API

bash
uvicorn main:app --reload --port 8000


### Running the Frontend (Streamlit)

bash
streamlit run streamlit_app.py --server.port 8501


Open your browser at http://localhost:8501.

## API Endpoints

| Path                | Method | Description                         |
| ------------------- | ------ | ----------------------------------- |
| /health           | GET    | Checks API health                   |
| /analyze-invoices | POST   | Upload policy PDF and invoice ZIP   |
| /chat             | POST   | Conversational queries with context |

## File Structure


invoice_system/
├── main.py                # FastAPI application
├── services/              # Business logic
│   ├── llm_service.py     # LLM analysis & chat
│   ├── vector_store.py    # MongoDB vector store
│   └── pdf_processor.py   # PDF text extraction
├── models/                # Pydantic schemas
├── streamlit_app.py       # Streamlit UI
├── requirements.txt       # Python dependencies
└── .env                   # Environment variables


## Error Handling & Logging

* FastAPI returns structured JSON errors (4xx/5xx).
* LLMService catches JSON parse errors and returns a placeholder response.
* Streamlit displays error messages via st.error().

## Testing

1. *Unit Tests*: (optional) Use pytest to test individual services.
2. *Manual*: Upload sample policy and invoice files via Streamlit and verify outputs.

## Troubleshooting

* **command not found: streamlit**: Ensure the virtual environment is activated.
* *Dependency build errors*: Pin problematic packages (e.g., numpy).
* *API model errors*: Run a model listing script to find compatible Gemini models.

## Future Enhancements

* *OAuth2 authentication*
* *Role-based access control*
* *Invoice image OCR support*
* *Deployment via Docker & Kubernetes*
* *Automated email notifications*

## Contributors

* *AMAN VERMA* – Development & Documentation

## License

This project is licensed under the MIT License.
