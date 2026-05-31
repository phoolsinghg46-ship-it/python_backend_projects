# Relational Contact Directory (SQLite3)

A lightweight data management utility built with Python and SQLite3. This command-line interface (CLI) application demonstrates how to establish relational data storage, structure transactional safety layers, and implement efficient data querying workflows.

---

## 🎯 Project Objectives & Core Features
- **Structured Schema Initialization:** Automatically checks for database tables and configures required data fields (Auto-incrementing IDs, constraints like `NOT NULL`, and variable type assignments) seamlessly at runtime.
- **Data Insertion & Persistence:** Adds contact profiles securely to a local `.db` file engine, ensuring records remain safe even after terminating application runtimes.
- **Dynamic Pattern Matching:** Features partial-string querying (e.g., searching "Jo" lists entries matching "John", "Joseph", etc.) via standard pattern-matching functions.
- **Relational Ledger Reads:** Pulls data matrices from the local environment and refactors raw relational tuples into structured terminal rows for optimal human readability.

---

## 🏗️ System Architecture & Workflow

The architecture decouples individual operation handlers from script runtime environments, utilizing scoped context controllers to guarantee data safety and prevent data block locks.

```text
       [ CLI Terminal Loop ]
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
[ Create ]   [ Read ]   [ Search ]
      │          │          │
      └──────────┼──────────┘
                 │
                 ▼
     [ SQLite Context Manager ]
                 │
                 ▼
    [ Engine File: contact_project.db ]
    