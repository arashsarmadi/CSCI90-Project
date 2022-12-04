def find_string_noncompliant():
    data = set(["sampleString1", "sampleString2", "sampleString3"])
    # Noncompliant: a loop is used to access a single item.
    for i in data:
        if i == "sampleString1":
            print("found item")