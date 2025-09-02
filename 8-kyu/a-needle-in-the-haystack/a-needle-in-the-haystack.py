def find_needle(haystack):
    i = 0
    for h in haystack:
        if (h == "needle"):
            return f"found the needle at position {i}"
        i += 1
        
​