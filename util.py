def toa_uc(level, pts):
    if level > 400:
        pts_per_1p = 10500 - 20 * (400 + min(level - 400, 150) / 3)
    else:
        pts_per_1p = 10500 - 20 * level

    return 0.01 * pts / pts_per_1p
    
