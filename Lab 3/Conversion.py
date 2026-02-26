def conversion(x):
    if x == "a":
        feet = int(input("\nEnter feet: "))
        value = feet * 0.3048
        return round(value, 2)
    else:
        meters = int(input("\nEnter meters: "))
        value = meters / 0.3048
        return round(value, 2)
