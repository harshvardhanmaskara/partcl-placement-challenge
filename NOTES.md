# Experiment Log

Reference: RePlAce 1.4578 · Will Seed 1.5338 · #7 Vibe 0.9939 · #2 Carrotato 0.9522 · #1 Archgen 0.9507 (avg proxy, 17 IBM).

| # | Date | Change | Avg proxy | Worst bench | Runtime/bench | Overlaps | Notes |
|---|------|--------|-----------|-------------|---------------|----------|-------|
| 0 | 2026-10-01 | Upstream greedy_row_placer (ibm01 only) | 2.0463 (ibm01) | - | 0.0s | 0 | setup verified; matches README |
| 1 | 2026-10-01 | `submissions/harshvardhanmaskara/placer.py` = benchmark's initial placement, untouched | 1.4551 | ibm17 1.7899 | 0.0s | **1939 (INVALID)** | Initial placement overlaps heavily; not a legal submission. Score is a floor to beat *after legalising*. |

## Ideas backlog
- Legalise the initial placement with minimal displacement (zero overlaps) — first real milestone; initial is 1.4551 but illegal
- Start from initial placement + legalisation, then local search
- Analytical/force-directed global placement, then SA refinement
- Joint soft-macro optimisation (own implementation; plc.optimize_stdcells is slow)
- Study open-source winners for techniques (credit them)
