# Macro Placement Project (Partcl × HRT 2026 challenge, personal project)

Goal: build a rigorous, reproducible macro placer that minimises proxy cost on the 17 IBM ICCAD04
benchmarks, then validates on NG45 designs. The official contest closed 2026-05-21; this is a
portfolio/research project benchmarked against its public leaderboard (README.md).

Upstream snapshot: partcleda/macro-place-challenge-2026 @ 996193c. Submodule external/MacroPlacement
(TILOS evaluator) is pinned; do not bump it.

## Commands
- Setup: `uv sync` (submodule: `git submodule update --init external/MacroPlacement`)
- One benchmark: `uv run evaluate submissions/harshvardhanmaskara/placer.py -b ibm01`
- All 17: `uv run evaluate submissions/harshvardhanmaskara/placer.py --all`
- NG45 designs: `uv run evaluate submissions/harshvardhanmaskara/placer.py --ng45`
- Visualise: add `--vis`
- Tests: `uv run pytest`

## Hard rules (contest constraints, keep them even though it is closed)
- Placer interface: `class X: def place(self, benchmark) -> Tensor[num_macros, 2]` of CENTER coords.
- Zero hard-macro overlaps (no tolerance; leave a tiny gap when legalising), all inside canvas,
  fixed macros unmoved. Soft macros may overlap and are movable, but never resize them.
- Only flips N/FN/FS/S for orientation; no 90° rotations.
- NEVER modify `macro_place/` evaluation code, `external/`, or `compute_proxy_cost`. No hardcoding
  per-benchmark solutions; the algorithm must be general.
- Runtime budget: < 1 hour per benchmark (judges: 16-core CPU, 100GB, RTX 6000 Ada). This Mac has no CUDA.
- Placer must be self-contained (runs offline); open-source licence (Apache 2.0 or GPL) if published.

## Layout
- `submissions/harshvardhanmaskara/` — my placer(s). `submissions/examples/`, `submissions/will_seed/` are upstream references; don't edit.
- `experiments/` — scratch scripts, sweeps, result CSVs.
- `NOTES.md` — experiment log: every change gets a row with avg proxy cost, per-benchmark worst case, runtime.

## Working style
- Establish a baseline number before changing anything; record in NOTES.md.
- One change per experiment; compare on all 17 benchmarks, not just ibm01 (avoid overfitting).
- Fix random seeds; results must be reproducible.
- Reference scores: RePlAce 1.4578 avg, Will Seed 1.5338, 1st place 0.9507.
- Credit any ideas borrowed from the open-source winners (Archgen, AbuPlace, macro-weave) in NOTES.md.
