def kelly_fraction(edge, odds):
    if odds <= 1:
        return 0
    return max((edge*(odds-1) - (1-edge))/ (odds-1), 0)
