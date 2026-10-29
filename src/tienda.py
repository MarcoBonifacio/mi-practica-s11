def proc(lst, t, d):
    total = 0
    for item in lst:
        p = item[0]
        q = item[1]
        total += p * q
    if t == "vip":
        total = total * 0.8
    elif t == "est":
        total = total * 0.85
    elif t == "may":
        total = total * 0.7
    if d > 100:
        total = total - 5
    elif d > 50:
        total = total - 2
    if total < 0:
        total = 0
    return total