def all_variants(text):
    for j in range(len(text)):
        for n in range(len(text) - j):
            yield text[j:n + j + 1]




a = all_variants("abc")
for i in a:
    print(i)