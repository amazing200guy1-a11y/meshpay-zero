#include "goertzel_fsk.h"
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

float goertzel_power(const float* samples, size_t num_samples, float target_freq, float sample_rate) {
    if (num_samples == 0 || sample_rate <= 0.0f) return 0.0f;

    int k = (int)(0.5f + ((float)num_samples * target_freq) / sample_rate);
    float omega = (2.0f * (float)M_PI * (float)k) / (float)num_samples;
    float coeff = 2.0f * cosf(omega);

    float s_prev = 0.0f;
    float s_prev2 = 0.0f;

    for (size_t i = 0; i < num_samples; ++i) {
        float s = samples[i] + coeff * s_prev - s_prev2;
        s_prev2 = s_prev;
        s_prev = s;
    }

    float power = s_prev * s_prev + s_prev2 * s_prev2 - coeff * s_prev * s_prev2;
    return power;
}

int8_t discriminate_fsk_symbol(const float* samples, size_t num_samples, float sample_rate) {
    float p0 = goertzel_power(samples, num_samples, FREQ_BIT_0, sample_rate);
    float p1 = goertzel_power(samples, num_samples, FREQ_BIT_1, sample_rate);
    float p_preamble = goertzel_power(samples, num_samples, FREQ_PREAMBLE, sample_rate);

    if (p_preamble > p0 && p_preamble > p1) {
        return -1; /* Preamble detected */
    }
    if (p0 > p1 && p0 > 10.0f) {
        return 0;  /* Bit 0 */
    }
    if (p1 > p0 && p1 > 10.0f) {
        return 1;  /* Bit 1 */
    }
    return -2; /* Undefined noise floor */
}
