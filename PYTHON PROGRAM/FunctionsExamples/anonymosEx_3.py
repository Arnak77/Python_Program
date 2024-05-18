vowel=lambda word:"vowel" if 'a' in word.lower() or 'u' in word.lower() or 'o' in word.lower() or 'i' in word.lower() or 'e' in word.lower() else "Not vowel"


res=vowel("bnm")
print(res)