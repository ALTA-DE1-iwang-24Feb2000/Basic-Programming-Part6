def compare(a, b):
    pattern = ""
    if len(a) == len(b) or len(a) > len(b):
         if a.count(b) > 0:
            start = a.index(b)
            end = start + len(b)
            pattern = a[start:end]
    elif len(a) < len(b):
        if b.count(a) > 0:
            start = b.index(a)
            end = start + len(a)
            pattern = b[start:end]
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA