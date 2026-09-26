"""Coverage check of the interval methods used in HTAB v0.

Simulates y = k t + AR(1) noise with known k and reports how often nominal 90%
intervals contain the true k, for the preregistered Newey-West t interval and
for the AR(1)-exact sensitivity interval. Results are reported in RESULTS.md.

Usage: python src/coverage_check.py
"""

import numpy as np

from htab_lib import ar1_exact_se, ols_hac, t_interval

R = 2000
TRUE_K = 0.3


def run(n, rho, rng):
    hit_nw = hit_ar1 = 0
    for _ in range(R):
        yrs = np.arange(n)
        z = rng.normal(0, 0.3, n)
        e = np.empty(n)
        e[0] = z[0] / np.sqrt(1 - rho ** 2)
        for t in range(1, n):
            e[t] = rho * e[t - 1] + z[t]
        fit = ols_hac(yrs, TRUE_K * yrs + e)
        lo, hi = t_interval(fit["k"], fit["se"], fit["df"], 0.90)
        hit_nw += lo <= TRUE_K <= hi
        se, _ = ar1_exact_se(fit)
        lo, hi = t_interval(fit["k"], se, fit["df"], 0.90)
        hit_ar1 += lo <= TRUE_K <= hi
    return hit_nw / R, hit_ar1 / R


def main():
    rng = np.random.default_rng(20260926)
    print("n,rho,coverage_newey_west_90,coverage_ar1_exact_90")
    for n in (7, 10, 15, 30):
        for rho in (0.0, 0.5, 0.8):
            a, b = run(n, rho, rng)
            print(f"{n},{rho},{a:.3f},{b:.3f}")


if __name__ == "__main__":
    main()
