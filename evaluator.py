from .conditioning import condition_value
from .quantization import quantize

class RCCEvaluator:
    def __init__(self, regions):
        self.regions = regions

    def evaluate(self, x, local_min):
        for region in self.regions:
            if region.contains(x):
                x_c = condition_value(x, local_min, region.scale)
                x_q = quantize(x_c)
                return region.func(x_q)
        return 0  # fallback
