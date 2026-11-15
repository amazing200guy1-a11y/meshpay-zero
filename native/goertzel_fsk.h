#ifndef GOERTZEL_FSK_H
#define GOERTZEL_FSK_H

#include <stddef.h>
#include <stdint.h>

#define FS_SAMPLE_RATE 44100
#define FREQ_PREAMBLE  17800.0f
#define FREQ_BIT_0     18200.0f
#define FREQ_BIT_1     19400.0f

/**
 * Computes Goertzel filter power at target frequency from PCM audio samples.
 * s[n] = x[n] + 2*cos(omega)*s[n-1] - s[n-2]
 */
float goertzel_power(const float* samples, size_t num_samples, float target_freq, float sample_rate);

/**
 * Discriminates binary FSK symbol from raw audio frame.
 * Returns: 0 for FREQ_BIT_0, 1 for FREQ_BIT_1, -1 for Noise/Preamble.
 */
int8_t discriminate_fsk_symbol(const float* samples, size_t num_samples, float sample_rate);

#endif /* GOERTZEL_FSK_H */
