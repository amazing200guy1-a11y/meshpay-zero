/**
 * MESHPAY-ZERO AUDIO WORKLET PROCESSOR
 * Continuous ultrasonic FSK demodulation in browser audio render thread.
 */

export class GoertzelDemodulator {
  private readonly sampleRate: number;

  constructor(sampleRate: number = 44100) {
    this.sampleRate = sampleRate;
  }

  public computePower(samples: Float32Array, targetFreq: number): number {
    const N = samples.length;
    const k = Math.round((N * targetFreq) / this.sampleRate);
    const omega = (2.0 * Math.PI * k) / N;
    const coeff = 2.0 * Math.cos(omega);

    let sPrev = 0.0;
    let sPrev2 = 0.0;

    for (let i = 0; i < N; i++) {
      const s = samples[i] + coeff * sPrev - sPrev2;
      sPrev2 = sPrev;
      sPrev = s;
    }

    return sPrev * sPrev + sPrev2 * sPrev2 - coeff * sPrev * sPrev2;
  }

  public detectSymbol(samples: Float32Array): 0 | 1 | -1 {
    const p0 = this.computePower(samples, 18200);
    const p1 = this.computePower(samples, 19400);
    const pSync = this.computePower(samples, 17800);

    if (pSync > p0 && pSync > p1) return -1; // Preamble sync
    return p1 > p0 ? 1 : 0;
  }
}
