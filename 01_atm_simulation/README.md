# OOP-Based ATM Simulation Terminal

A robust command-line interface (CLI) banking application built using Python. This project simulates automated teller machine workflows, emphasizing secure state management, data validation, and clean object-oriented architecture.

---

## 🎯 Project Objectives & Core Features
- **Account Registration & Multi-User Support:** Validates inputs dynamically (12-digit account mapping, 4-digit PIN structures) and flags pre-existing accounts to enforce identity logic.
- **Authentication Gateway:** Implements a state-driven user session handshake before granting system access.
- **Core Banking Utilities:** Complete transactional suite covering balance inquiries, monetary deposits, secure fund withdrawals with safety balance checks, and instant PIN modifications.
- **Dynamic File Persistence:** Seamlessly interacts with a localized data engine to read and write application states natively using flat-file formats.

---

## 🏗️ System Architecture & Workflow

The application leverages an Object-Oriented paradigm where the core operational controller encapsulates user workflows, data verification layers, and real-time JSON input/output channels.

```text
[ Authentication Gateway ] ───► Login / Registration
            │
            ▼
     (State Verified)
            │
            ▼
┌────────────────────────────────────────────────────────┐
│                   ATM Core Operations                  │
├───────────────┬────────────────┬───────────────────────┤
│ Check Balance │ Deposit Assets │ Secure Fund Withdraw  │
└───────────────┴────────────────┴───────────────────────┘
            │
            ▼
[ JSON Serialization Engine ] ───► Persistent Disk Storage (database.json)
