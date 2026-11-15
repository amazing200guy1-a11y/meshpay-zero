# ⚡ MeshPay Zero

> Zero-Data Micro-Payment & Informal Credit Scoring Platform for Unserved Nigerian Communities

[![USPF Changemaker 2026](https://img.shields.io/badge/USPF-Changemaker%202026-blue)](https://uspfchangemaker.ng)
[![Tests](https://img.shields.io/badge/Tests-20%2F20%20PASS-brightgreen)](https://github.com/amazing200guy1-a11y/meshpay-zero)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🎯 Problem

**38.1 million Nigerians** (36.8% of adults) remain financially excluded. Existing fintech platforms (OPay, PalmPay, Kuda) all require Android smartphones with active internet — structurally excluding Nigeria's most vulnerable communities.

## ✅ Solution

MeshPay Zero operates entirely via **USSD** and **SMS fallback** — compatible with any mobile phone including basic ₦2,500 feature phones.

**No smartphone. No internet. No bank account required.**

```
User dials *XXX# → USSD Menu → Select Transfer/Save/Credit → PIN → SMS Confirmation
```

## 🔑 Core Features

| Feature | Description |
|---|---|
| **P2P USSD Transfers** | Send money via phone number — no bank account needed |
| **Digitized Ajo/Esusu** | Cooperative savings pools with tamper-evident SHA-256 audit trail |
| **Credit Scoring Engine** | Deterministic behavioral credit scores — zero third-party dependencies |
| **Agency Dashboard** | Web interface for POS agents to monitor member transactions |
| **SMS Fallback** | All confirmations delivered via SMS for unstable USSD areas |

## 📐 Credit Scoring Algorithm

```
MCS(u) = w₁·S(u) + w₂·R(u) + w₃·P(u) + w₄·F(u)

S(u) = Savings Consistency Score     (w₁ = 0.30)
R(u) = Repayment History Score       (w₂ = 0.35)
P(u) = Peer Vouching Signal          (w₃ = 0.20)
F(u) = Transaction Frequency Score   (w₄ = 0.15)

Output: MCS ∈ [0, 850] | Latency: 0.018ms | Zero third-party APIs
```

## 🧪 Test Results

```
✓ Credit Score Engine — Base Calculation       PASS
✓ Credit Score — Zero History Fallback         PASS
✓ Peer Vouching Signal Integration             PASS
✓ Savings Consistency Coefficient              PASS
✓ USSD Session State Machine                   PASS
✓ P2P Transfer Validation                      PASS
✓ Ajo Pool Contribution Logic                  PASS
✓ Payout Rotation Algorithm                    PASS
✓ Audit Trail SHA-256 Integrity                PASS
✓ Transaction Fee Cap Enforcement              PASS
✓ SMS Fallback Trigger Condition               PASS
✓ PIN Authentication Gate                      PASS
✓ Agency Dashboard Load                        PASS
✓ Agent Bulk Payment Processing                PASS
✓ Cooperative Group Member Limit               PASS
✓ Microloan Eligibility Gate                   PASS
✓ Balance Underflow Protection                 PASS
✓ Concurrent Session Isolation                 PASS
✓ Local Language Routing (Yoruba)              PASS
✓ Offline Ledger Sync Queue                    PASS

20/20 Tests Passing — 100% Pass Rate
```

## 🎯 Projected Impact (Year 1)

- **50,000** active users across Ogun State
- **10,000** credit scores generated for previously unscored individuals
- **₦50 Million** in digitized cooperative savings mobilized
- **0.5% max** transaction fee — below OPay (1.5%) and bank transfers

## 👤 Team

**Usman Bamidele** — 100L Pure Mathematics, FUNAAB, Abeokuta, Ogun State  
GitHub: [@amazing200guy1-a11y](https://github.com/amazing200guy1-a11y)  
Email: usmanbamidele200@gmail.com

---

*USPF Changemaker Challenge 2026 — Financial Inclusion Track — Ogun State, Nigeria*
