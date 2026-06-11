try:
    print("A")

    raise ValueError("Oops")

    print("B")

except ValueError:
    print("C")

finally:
    print("D")

print("E")