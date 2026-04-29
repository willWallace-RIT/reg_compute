def compute_min(values):
    return min(values)

def condition_value(x, m, scale):
    return (x - m) / scale

def reconstruct_value(x_q, m, scale):
    return x_q * scale + m
