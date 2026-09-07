# ConversationHub

### AI-Powered Customer Engagement & Data Platform

[![Python](https://img.shields.io/badge/Python-3.x-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-API-green)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)]()
[![BigQuery](https://img.shields.io/badge/BigQuery-Analytics-orange)]()
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)]()
[![GCP](https://img.shields.io/badge/GCP-Cloud-red)]()

ConversationHub is a production-style customer engagement and data platform designed to centralize customer information, manage conversations, support automated messaging, and transform operational data into analytics-ready datasets.

The project demonstrates an end-to-end engineering workflow covering **backend API development, transactional data modeling, ETL/ELT pipelines, data quality, analytical modeling, cloud infrastructure, containerization, CI/CD and business analytics**.

> **Project Type:** Self-initiated portfolio project
> **Primary Focus:** Data Engineering + Backend Engineering + Cloud
> **Status:** Actively developed

---

## Table of Contents

* [Business Problem](#business-problem)
* [Solution](#solution)
* [Architecture](#architecture)
* [Key Features](#key-features)
* [Data Engineering](#data-engineering)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Database Design](#database-design)
* [API](#api)
* [Analytics](#analytics)
* [Security](#security)
* [Local Development](#local-development)
* [Environment Variables](#environment-variables)
* [Testing](#testing)
* [CI/CD](#cicd)
* [Cloud Deployment](#cloud-deployment)
* [Engineering Decisions](#engineering-decisions)
* [Current Status](#current-status)
* [Future Improvements](#future-improvements)

---

# Business Problem

Customer-facing businesses often receive customer information and conversations through multiple channels.

This can result in:

* fragmented customer information
* disconnected conversation history
* limited visibility into customer engagement
* repetitive manual communication
* difficulty generating reliable analytics
* operational databases being used directly for analytical workloads

ConversationHub was designed to address these challenges through a unified backend, transactional database, data pipeline and analytics layer.

---

# Solution

ConversationHub provides a centralized platform for:

1. Customer management
2. Conversation and message tracking
3. Automated customer communication
4. AI-assisted messaging
5. Transactional data storage
6. Incremental ETL/ELT processing
7. Analytical data modeling
8. Business analytics and reporting

The architecture separates **operational workloads from analytical workloads**.

PostgreSQL is used for transactional application data, while BigQuery is used as the analytical warehouse.

---

# Architecture

```text
                         Customer Channels
                                │
                                ▼
                    ┌──────────────────────┐
                    │   WhatsApp Business  │
                    │         API          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       FastAPI        │
                    │      Backend API     │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
       Customer API     Conversation API     AI Service
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     PostgreSQL       │
                    │  Transactional DB    │
                    └──────────┬───────────┘
                               │
                         Incremental
                           ETL / ELT
                               │
                               ▼
                    ┌──────────────────────┐
                    │      BigQuery        │
                    │  Analytics Warehouse │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
             Analytics API              Power BI
```

Deployment architecture:

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ├── Tests
   ├── Linting
   └── Docker Build
          │
          ▼
       GCP
    ┌─────┴──────┐
    │            │
 Cloud Run    BigQuery
    │
 Cloud SQL
    │
Secret Manager
```

---

# Key Features

## Customer Management

* Create customers
* Retrieve customers
* Retrieve individual customers
* Update customer information
* Delete customers
* Phone-number uniqueness validation

## Conversation Management

* Store customer conversations
* Track conversation state
* Maintain conversation history
* Associate conversations with customers

## Message Management

* Store inbound and outbound messages
* Track message timestamps
* Track message sender/type
* Associate messages with conversations

## AI Messaging

* AI-assisted customer responses
* Configurable LLM integration
* Conversation-aware responses
* Message persistence for analytics

## WhatsApp Integration

* Incoming message webhook
* Webhook verification
* Outbound message integration
* Conversation persistence

---

# Data Engineering

The analytical architecture separates operational data from analytical workloads.

```text
PostgreSQL
     │
     │ Incremental Extraction
     ▼
Raw Layer
     │
     ▼
Staging Layer
     │
     ▼
Transformation
     │
     ▼
Data Quality Checks
     │
     ▼
Analytics Layer
     │
     ▼
BigQuery
     │
     ▼
Power BI / Analytics API
```

### Incremental Processing

The pipeline uses an incremental loading strategy rather than repeatedly processing the complete dataset.

Records are identified using timestamps/watermarks such as:

```text
created_at
updated_at
```

This reduces unnecessary processing and makes the pipeline more scalable.

### Data Quality

The pipeline validates:

* duplicate records
* null values
* invalid customer references
* invalid message records
* row-count consistency
* schema consistency

---

# Analytics

The analytics layer is designed to support metrics such as:

* total customers
* active customers
* messages per day
* inbound vs outbound messages
* customer engagement
* response time
* conversation volume
* customer segmentation
* geographic distribution
* AI-assisted vs human responses

The resulting datasets can be consumed by Power BI or other BI tools.

---

# Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL
* SQL
* Alembic

### Data Engineering

* Python
* Pandas
* ETL/ELT
* Data validation
* Incremental processing
* BigQuery

### Cloud

* Google Cloud Platform
* Cloud Run
* Cloud SQL
* BigQuery
* Secret Manager

### DevOps

* Docker
* Docker Compose
* GitHub Actions
* CI/CD

### AI & Integrations

* LLM API
* WhatsApp Business API
* HTTP APIs

### Analytics

* BigQuery
* Power BI

---

# Project Structure

```text
ConversationHub/
│
├── backend/
│   └── app/
│       ├── api/
│       │   ├── auth.py
│       │   ├── customer.py
│       │   ├── conversation.py
│       │   ├── message.py
│       │   └── webhook.py
│       │
│       ├── core/
│       │   ├── security.py
│       │   └── logging.py
│       │
│       ├── database/
│       │   ├── db.py
│       │   └── migrations/
│       │
│       ├── models/
│       │   ├── user.py
│       │   ├── customer.py
│       │   ├── conversation.py
│       │   └── message.py
│       │
│       ├── schemas/
│       │   ├── customer.py
│       │   ├── conversation.py
│       │   └── message.py
│       │
│       ├── services/
│       │   ├── ai_service.py
│       │   ├── whatsapp_service.py
│       │   └── analytics_service.py
│       │
│       └── main.py
│
├── data_pipeline/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validation.py
│   └── pipeline.py
│
├── sql/
│   ├── staging/
│   └── analytics/
│
├── tests/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docs/
│   ├── architecture.md
│   └── database.md
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# Database Design

Core entities:

```text
User
 │
 └── Customer
       │
       └── Conversation
              │
              └── Message
```

Example relationship:

```text
Customer
---------
id
name
phone
city
created_at
updated_at

Conversation
------------
id
customer_id
status
started_at
ended_at

Message
-------
id
conversation_id
sender_type
message_type
content
created_at
```

---

# API

Interactive API documentation is available through FastAPI's OpenAPI documentation.

Local development:

```text
http://localhost:8000/docs
```

Example endpoints:

```text
POST   /customers/
GET    /customers/
GET    /customers/{customer_id}
PUT    /customers/{customer_id}
DELETE /customers/{customer_id}
```

Additional endpoints will be added for authentication, conversations, messages and webhooks.

---

# Security

The project follows security practices including:

* environment-based configuration
* secrets excluded from Git
* `.env.example` for required configuration
* password hashing
* JWT-based authentication
* API validation
* database constraints
* webhook verification
* cloud secret management

No production credentials or API keys are stored in the repository.

---

# Local Development

## Prerequisites

* Python 3.x
* Docker
* Docker Compose
* Git

## Clone

```bash
git clone https://github.com/Prachi0312/ConversationHub.git
cd ConversationHub
```

## Start PostgreSQL

```bash
docker compose up -d db
```

## Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Start FastAPI

```bash
python -m uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# Environment Variables

Copy:

```bash
cp .env.example .env
```

Example configuration:

```env
DATABASE_URL=
SECRET_KEY=
WHATSAPP_ACCESS_TOKEN=
WHATSAPP_PHONE_NUMBER_ID=
WHATSAPP_VERIFY_TOKEN=
LLM_API_KEY=
GCP_PROJECT_ID=
BIGQUERY_DATASET=
```

Never commit `.env` or production credentials.

---

# Testing

Tests are implemented using:

* pytest
* FastAPI test client
* database integration tests
* pipeline validation tests

Run:

```bash
pytest
```

---

# CI/CD

GitHub Actions is used to automate:

```text
Git Push
   ↓
Install Dependencies
   ↓
Lint
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Deploy
```

---

# Cloud Deployment

The application is designed for deployment on Google Cloud.

Target architecture:

```text
FastAPI
   ↓
Cloud Run
   ↓
Cloud SQL PostgreSQL

Data Pipeline
   ↓
BigQuery

Secrets
   ↓
Secret Manager
```

---

# Engineering Decisions

### PostgreSQL for transactional workloads

PostgreSQL provides reliable transactional storage for customer, conversation and message data.

### BigQuery for analytical workloads

BigQuery separates analytical workloads from the transactional application database and provides scalable analytical querying.

### Incremental ETL

Incremental processing reduces unnecessary data movement and improves pipeline efficiency.

### Docker

Docker provides reproducible development and deployment environments.

### FastAPI

FastAPI provides a typed, documented and high-performance API layer with automatic OpenAPI documentation.

---

# Current Status

### Completed

* [x] Repository setup
* [x] FastAPI application
* [x] Docker Compose
* [x] PostgreSQL container
* [x] SQLAlchemy database connection
* [x] Customer model
* [x] Customer database table
* [x] Customer REST API foundation

### In Progress

* [ ] Customer CRUD testing
* [ ] Database migrations
* [ ] Authentication
* [ ] Conversation management
* [ ] Message management
* [ ] WhatsApp integration
* [ ] AI messaging
* [ ] PostgreSQL → BigQuery pipeline
* [ ] Data quality framework
* [ ] Analytics models
* [ ] Power BI integration
* [ ] Automated tests
* [ ] GitHub Actions
* [ ] GCP deployment

---

# Future Improvements

* Event-driven architecture
* Message queues
* Advanced customer segmentation
* Real-time analytics
* Data lineage
* Observability
* Rate limiting
* API versioning
* Horizontal scaling
* Advanced data quality monitoring

---

# Project Type

**Self-initiated portfolio project**

The platform is designed around a realistic SaaS customer-engagement use case and demonstrates production-oriented engineering practices across backend development, data engineering, analytics and cloud infrastructure.

---

## Author

**Prachi Naik Nimbalkar**

Data Engineer | Python | SQL | ETL/ELT | GCP | BigQuery | FastAPI | Docker

GitHub: https://github.com/Prachi0312

---

## License

This project is intended for educational and portfolio purposes.
