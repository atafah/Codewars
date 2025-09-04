def double_char(s):
    doubled = ""
    for character in s:
        doubled += f"{character}{character}"
    return doubled