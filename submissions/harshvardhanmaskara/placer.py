"""My macro placer. Baseline: keep the benchmark's initial placement (no optimisation yet)."""
import torch

from macro_place.benchmark import Benchmark


class HarshPlacer:
    def __init__(self, seed: int = 0):
        self.seed = seed

    def place(self, benchmark: Benchmark) -> torch.Tensor:
        torch.manual_seed(self.seed)
        placement = benchmark.macro_positions.clone()
        return placement
