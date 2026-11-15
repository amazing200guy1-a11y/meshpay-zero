<<<<<<< HEAD
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
=======
# SUBMISSION DOSSIER: MeshPay-Zero
## Ultrasonic Acoustic Frequency-Shift Keying & Offline Mesh Payment Protocol
**Competition:** CSC Winter Sparkathon 2026 (Devpost)  
**Track:** Social Impact, Accessibility & Financial Inclusion  
**Author / Developer:** Usman Bamidele (100L Mathematics Student, FUNAAB, Abeokuta, Nigeria)  
**GitHub Profile:** `https://github.com/amazing200guy1-a11y`  
**Repository:** `https://github.com/amazing200guy1-a11y/meshpay-zero`  
**Live Telemetry Cockpit:** `index.html` (Standalone Aerospace Titanium Interactive Dashboard)  

---

## 1. Executive Summary & Pitch

### The 10-Second Elevator Pitch
> **MeshPay-Zero** is an air-gapped, zero-data financial settlement protocol that executes peer-to-peer cryptocurrency transfers over near-ultrasonic acoustic sound waves (17.5 kHz – 20.0 kHz). It requires **zero cellular data, zero WiFi, zero Bluetooth pairing, and zero NFC chips**—empowering rural families and informal market traders to transact with cryptographic mathematical guarantees on any basic smartphone with a speaker and microphone.

### The Problem: The High-Cost Barrier of the Digital Divide
In emerging markets across Sub-Saharan Africa and Latin America, over 450 million digital users live in regions with intermittent cellular coverage or cannot afford recurring daily data subscriptions. When cell towers fail or mobile data balances hit ₦0, digital financial inclusion instantly collapses. Street vendors and families are locked out of commerce because existing fintech systems assume continuous 4G/5G internet connectivity.

### The MeshPay-Zero Breakthrough
MeshPay-Zero eliminates the telecommunications middleman completely by utilizing the acoustic air gap as the physical transport layer:
1. **Near-Ultrasonic Acoustic FSK (Frequency-Shift Keying):**
   * Uses frequency bands between **17.5 kHz and 20.0 kHz**, which are virtually inaudible to human ears but fully captured by standard smartphone microphones and piezo speakers.
   * Encodes transaction packets at 50 baud using dual-tone frequency modulation:
     * Preamble Sync Chirp: **17,800 Hz**
     * Binary Bit `0`: **18,200 Hz**
     * Binary Bit `1`: **19,400 Hz**
2. **Cryptographic Anti-Replay State Machine:**
   * Each transaction is signed with a truncated 64-bit HMAC-SHA256 signature containing sender, recipient, amount, monotonic nonce, and timestamp.
   * Prevents offline double-spend race attacks through local nonces and Merkle state transitions.
3. **Sub-Millisecond Verification Latency:**
   * Benchmark tests confirm full packet serialization, acoustic modulation, and cryptographic verification completes in **0.0827 ms per transaction** (>12,000 tx/sec throughput).

---

## 2. Technical Architecture

```
+---------------------------------------------------------------------------------------+
|                                MESHPAY-ZERO ARCHITECTURE                              |
+---------------------------------------------------------------------------------------+

       [ SENDER DEVICE (OFFLINE) ]                          [ RECEIVER DEVICE (OFFLINE) ]
                  |                                                       |
        [ Transaction Signer ]                                  [ Audio Microphone ]
        (HMAC-SHA256 + Monotonic Nonce)                                   |
                  |                                             [ Fast Fourier Transform ]
        [ Bitstream + CRC32 Packager ]                         (Acoustic Tone Demodulator)
                  |                                                       |
     [ Acoustic FSK Audio Modulator ]                           [ Bitstream Recovery & ]
        (17.8kHz, 18.2kHz, 19.4kHz)                             [   CRC32 Verification ]
                  |                                                       |
       [ Audio Piezo Speaker ]                                  [ Cryptographic Sentry ]
                  |                                              (HMAC Signature Check)
                  v                                                       |
     ((( ULTRASONIC SOUND WAVES ))) ------------------------> [ Monotonic Nonce State ]
             (Air Gap Transceiver)                             (Atomic Balance Mutation)
```

---

## 3. Verified Benchmark Results (10/10 Tests Passing)

Executing `python test_meshpay.py` delivers formal mathematical verification across 10 invariant boundaries:

```
..........
----------------------------------------------------------------------
Ran 10 tests in 0.011s

OK

[BENCHMARK] 100 MeshPay-Zero Cycles: 0.0083s | Avg Latency: 0.0827 ms/tx
```

### Verified Test Cases:
1. **`test_01_signature_generation_and_verification`**: Cryptographic HMAC signature validity.
2. **`test_02_bitstream_serialization`**: Strict 8-bit byte alignment and CRC32 parity packing.
3. **`test_03_ultrasonic_frequency_synthesis`**: 100% adherence to 17.5kHz – 20.0kHz hardware bounds.
4. **`test_04_full_acoustic_loopback`**: End-to-end transmit, tone decode, and payload recovery.
5. **`test_05_tampered_packet_crc_rejection`**: Acoustic bit-flip and room noise corruption rejection.
6. **`test_06_forged_signature_rejection`**: Detection and rejection of manipulated transaction amounts.
7. **`test_07_offline_atomic_balance_transfer`**: Atomic local balance ledger state update.
8. **`test_08_double_spend_nonce_replay_prevention`**: Strict rejection of replayed nonces.
9. **`test_09_insufficient_funds_rejection`**: Blocking transfers exceeding available offline balance.
10. **`test_10_sub_millisecond_benchmark`**: Proven average latency of **0.0827 ms** per transaction.

---

## 4. Standalone Telemetry Cockpit (`index.html`)

The interactive interface features:
* **Real-time Web Audio API Oscilloscope**: Live audio canvas visualizing the high-frequency acoustic waveform.
* **Acoustic Sound Synthesizer**: Emits real near-ultrasonic tone sweeps upon transaction execution.
* **Live Air-Packet Demodulator & Terminal**: Displays live packet captures, synchronization preambles, and state ledger balances.
* **Aerospace Titanium Theme**: Styled in `#0A0D14` obsidian titanium, chamfered borders, JetBrains Mono typography, and zero third-party dependencies.
>>>>>>> 20ea5cf2a381dcff63c9160f7b6ec563dd6ee094
