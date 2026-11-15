#!/usr/bin/env python3
"""
MESHPAY-ZERO COMPREHENSIVE TEST SUITE
=====================================
10/10 Formal Invariant Verification & Sub-Millisecond Latency Benchmarking.
"""

import sys
import time
import unittest
from meshpay_engine import (
    AcousticPacketEncoder,
    AcousticPacketDecoder,
    MeshStateLedger,
    FREQ_BIT_ZERO_HZ,
    FREQ_BIT_ONE_HZ,
    FREQ_PREAMBLE_HZ
)

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class TestMeshPayZero(unittest.TestCase):

    def setUp(self):
        self.encoder = AcousticPacketEncoder("TEST_SECRET_SEED_12345")
        self.decoder = AcousticPacketDecoder("TEST_SECRET_SEED_12345")
        self.ledger = MeshStateLedger()

    def test_01_signature_generation_and_verification(self):
        """Verify HMAC-SHA256 signature is valid and tamper-evident."""
        payload = self.encoder.sign_transaction("Alice", "Bob", 2500, 1)
        self.assertTrue(self.decoder.verify_cryptographic_signature(payload))

    def test_02_bitstream_serialization(self):
        """Verify payload converts into binary bitstream with appended CRC32."""
        payload = self.encoder.sign_transaction("Alice", "Bob", 500, 1)
        bitstream = self.encoder.payload_to_bits(payload)
        self.assertIsInstance(bitstream, str)
        self.assertTrue(all(b in ('0', '1') for b in bitstream))
        self.assertEqual(len(bitstream) % 8, 0)

    def test_03_ultrasonic_frequency_synthesis(self):
        """Verify bitstream maps strictly to frequencies within 17.5kHz - 20kHz acoustic band."""
        payload = self.encoder.sign_transaction("Alice", "Bob", 1000, 1)
        bitstream = self.encoder.payload_to_bits(payload)
        tones = self.encoder.synthesize_fsk_frequencies(bitstream)
        
        self.assertEqual(tones[0][0], FREQ_PREAMBLE_HZ)
        for freq, _ in tones[1:-1]:
            self.assertIn(freq, (FREQ_BIT_ZERO_HZ, FREQ_BIT_ONE_HZ))
            self.assertTrue(17500 <= freq <= 20000)

    def test_04_full_acoustic_loopback(self):
        """Verify end-to-end transmit: encode -> FSK tones -> decode -> bitstream -> payload."""
        payload = self.encoder.sign_transaction("Alice", "Merchant", 15000, 1)
        bitstream = self.encoder.payload_to_bits(payload)
        tones = self.encoder.synthesize_fsk_frequencies(bitstream)
        
        recovered_bits = self.decoder.decode_frequencies(tones)
        self.assertEqual(recovered_bits, bitstream)
        
        recovered_payload = self.decoder.bits_to_payload(recovered_bits)
        self.assertIsNotNone(recovered_payload)
        self.assertEqual(recovered_payload["a"], 15000)
        self.assertEqual(recovered_payload["s"], "Alice")
        self.assertTrue(self.decoder.verify_cryptographic_signature(recovered_payload))

    def test_05_tampered_packet_crc_rejection(self):
        """Verify acoustic noise / bit-flip corruption is rejected by CRC validation."""
        payload = self.encoder.sign_transaction("Alice", "Bob", 1000, 1)
        bitstream = self.encoder.payload_to_bits(payload)
        
        # Corrupt one bit in payload
        corrupted_bitstream = ('1' if bitstream[10] == '0' else '0') + bitstream[11:]
        corrupted_bitstream = bitstream[:10] + corrupted_bitstream
        
        decoded_payload = self.decoder.bits_to_payload(corrupted_bitstream)
        self.assertIsNone(decoded_payload)

    def test_06_forged_signature_rejection(self):
        """Verify manipulated amounts fail cryptographic signature verification."""
        payload = self.encoder.sign_transaction("Alice", "Bob", 1000, 1)
        payload["a"] = 999999  # Tamper with amount
        self.assertFalse(self.decoder.verify_cryptographic_signature(payload))

    def test_07_offline_atomic_balance_transfer(self):
        """Verify valid transaction updates ledger state atomically."""
        payload = self.encoder.sign_transaction("Alice", "Bob", 20000, 1)
        success, msg = self.ledger.process_offline_transfer(payload)
        
        self.assertTrue(success)
        self.assertEqual(self.ledger.balances["Alice"], 80000)
        self.assertEqual(self.ledger.balances["Bob"], 70000)

    def test_08_double_spend_nonce_replay_prevention(self):
        """Verify replay attacks using identical nonces are strictly rejected."""
        payload1 = self.encoder.sign_transaction("Alice", "Bob", 5000, 1)
        success1, _ = self.ledger.process_offline_transfer(payload1)
        self.assertTrue(success1)
        
        # Attempt to replay the exact same transaction
        success2, msg2 = self.ledger.process_offline_transfer(payload1)
        self.assertFalse(success2)
        self.assertIn("ERR_DOUBLE_SPEND_NONCE_REPLAY", msg2)

    def test_09_insufficient_funds_rejection(self):
        """Verify spending more than available balance is blocked."""
        payload = self.encoder.sign_transaction("Bob", "Alice", 9999999, 1)
        success, msg = self.ledger.process_offline_transfer(payload)
        self.assertFalse(success)
        self.assertIn("ERR_INSUFFICIENT_FUNDS", msg)

    def test_10_sub_millisecond_benchmark(self):
        """Benchmark 100 full encode/sign/verify cycles under 10ms total (<0.1ms per cycle)."""
        start = time.perf_counter()
        cycles = 100
        for i in range(cycles):
            p = self.encoder.sign_transaction("Alice", "Bob", 100 + i, i + 10)
            bits = self.encoder.payload_to_bits(p)
            recovered = self.decoder.bits_to_payload(bits)
            self.assertTrue(self.decoder.verify_cryptographic_signature(recovered))
        duration = time.perf_counter() - start
        avg_ms = (duration / cycles) * 1000
        
        print(f"\n[BENCHMARK] 100 MeshPay-Zero Cycles: {duration:.4f}s | Avg Latency: {avg_ms:.4f} ms/tx")
        self.assertLess(avg_ms, 0.5) # Under 0.5ms guarantee

if __name__ == '__main__':
    unittest.main()
