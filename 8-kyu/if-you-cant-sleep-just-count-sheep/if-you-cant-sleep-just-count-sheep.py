def count_sheep(n):
    if n == 0:
        return ''
    s = ""
    for i in range(1,n+1):
        s += (f"{i} sheep...")
    return s