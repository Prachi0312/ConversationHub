# ConversationHub

### Customer Engagement & Data Platform

ConversationHub is a self-initiated, production-style customer engagement platform being developed to demonstrate end-to-end **backend, data engineering and cloud engineering** capabilities.

The platform is designed to centralize customer information and conversations, support automated customer interactions, and transform operational data into analytics-ready datasets.

> **Project Type:** Self-initiated portfolio project
> **Primary Focus:** Data Engineering + Backend Engineering + Cloud
> **Status:** Actively developed

---

## Business Problem

Customer-facing businesses often manage customer information and conversations across multiple systems.

This can make it difficult to:

* maintain centralized customer information
* manage customer records reliably
* track conversation history
* automate customer interactions
* analyze engagement data
* separate transactional and analytical workloads

ConversationHub is being developed as a unified platform to address these requirements.

---

## Current Architecture

```text
Client
  │
  ▼
FastAPI REST API
  │
  ▼
SQLAlchemy
  │
  ▼
PostgreSQL
  │
  ▼
Customer Data
```

The planned analytical architecture will extend this into:

```text
PostgreSQL
     │
     ▼
Incremental ETL / ELT
     │
     ▼
BigQuery
     │
     ▼
Analytics / Power BI
```

---

## Currently Implemented

* FastAPI application
* REST API foundation
* PostgreSQL running through Docker Compose
* SQLAlchemy database integration
* Customer database model
* Customer database table
* Customer API structure
* Pydantic request/response schemas
* OpenAPI / Swagger documentation
* Environment-based configuration foundation

---

## Customer API

Current API endpoints include:

```text
POST   /customers/
GET    /customers/
GET    /customers/{customer_id}
PUT    /customers/{customer_id}
DELETE /customers/{customer_id}
```

Interactive API documentation:

```text
/docs
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL
* SQL

### Development

* Docker
* Docker Compose
* Git
* GitHub Codespaces

### Planned Data Engineering

* BigQuery
* ETL / ELT
* Data quality validation
* Incremental data processing
* Analytics data modeling

### Planned Cloud / DevOps

* Google Cloud Platform
* Cloud Run
* Cloud SQL
* GitHub Actions
* CI/CD

---

## Local Development

### Prerequisites

* Python 3.x
* Docker
* Docker Compose

### Start PostgreSQL

```bash
docker compose up -d db
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Start FastAPI

```bash
python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Open API documentation

```text
http://localhost:8000/docs
```

---

## Project Roadmap

* [x] FastAPI application
* [x] PostgreSQL container
* [x] SQLAlchemy integration
* [x] Customer model
* [x] Customer API foundation
* [ ] Database migrations with Alembic
* [ ] Authentication and authorization
* [ ] Conversation management
* [ ] Message management
* [ ] WhatsApp Business API integration
* [ ] AI-assisted messaging
* [ ] PostgreSQL → BigQuery pipeline
* [ ] Data quality framework
* [ ] Analytics data models
* [ ] Power BI integration
* [ ] Automated testing
* [ ] GitHub Actions CI/CD
* [ ] GCP deployment
* [ ] Production monitoring

---

## Data Engineering Goals

The final platform will demonstrate an end-to-end data engineering workflow:

```text
Operational PostgreSQL
        ↓
Incremental Extraction
        ↓
Transformation
        ↓
Data Quality Checks
        ↓
BigQuery
        ↓
Analytics Models
        ↓
Power BI
```

The goal is to demonstrate practical skills in **SQL, data modeling, ETL/ELT, incremental processing, data quality, cloud data warehousing and analytics**.

---

## Project Type

This is a **self-initiated portfolio project** based on a realistic SaaS customer-engagement use case.

It is not presented as client work.

---

## Author

**Prachi Naik Nimbalkar**

Data Engineer | Python | SQL | ETL/ELT | GCP | BigQuery | FastAPI | Docker

GitHub: https://github.com/Prachi0312
