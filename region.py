class Region:
    def __init__(self, min_bound, max_bound, scale, func):
        self.min_bound = min_bound
        self.max_bound = max_bound
        self.scale = scale
        self.func = func

    def contains(self, x):
        return self.min_bound <= x < self.max_bound
