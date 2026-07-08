# AGENTS.md

## Haryana Partition Manager

This repository contains a professional desktop application for managing Haryana Revenue records and partition proceedings.

The project is intended to become production quality.

---

# Primary Goal

Maintain correctness above all else.

Never sacrifice data integrity for code elegance.

Every change must preserve existing functionality unless explicitly requested.

---

# Architecture

Presentation
    GUI (PySide6)

↓

Application Services

↓

Repositories

↓

SQLAlchemy ORM

↓

SQLite

Business logic belongs in Services.

Repositories perform persistence only.

GUI must not directly manipulate database sessions.

---

# Coding Standards

Use

- Python 3.12+
- SQLAlchemy ORM
- Type hints
- Dataclasses where appropriate
- Enum for fixed values
- logging module
- Context managers

Avoid

- print()
- bare except:
- duplicated code
- global state

---

# Database Rules

Business identifiers are NOT primary keys.

Examples

Village
    Hadbast Number

Khewat
    Khewat Number

Parcel
    Khasra Number

These may change.

Internal relationships should eventually use UUID.

---

# Development Rules

Never rewrite a working module.

Always make incremental changes.

Each commit must be independently runnable.

Every change must include

- explanation
- affected files
- risk assessment

---

# Testing

Before major refactoring

Create tests.

Never reduce test coverage.

---

# Documentation

Whenever architecture changes

Update

README

ARCHITECTURE.md

ROADMAP.md

CHANGELOG.md

---

# Long-term Roadmap

Version 1.0

↓

Freeze

↓

HRL (Revenue Library)

↓

HRI (Importer/OCR)

↓

Future independent modules

Never continue expanding Version 1 indefinitely.