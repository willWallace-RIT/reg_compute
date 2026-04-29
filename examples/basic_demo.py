from rcc.region import Region
from rcc.evaluator import RCCEvaluator

# Define functions
def high_precision(x):
    return x * x

def low_precision(x):
    return x << 1  # cheap approx (2x)

regions = [
    Region(0, 10, 0.1, high_precision),
    Region(10, 100, 1.0, low_precision),
]

evaluator = RCCEvaluator(regions)

values = [1.2, 5.7, 20.3, 50.8]

local_min = min(values)

for v in values:
    print(v, "->", evaluator.evaluate(v, local_min))
