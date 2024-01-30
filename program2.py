g = input("Enter gender in terms of M or F: ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if g == 'M':
    if 134 <= hemoglobin <= 167:
        print("normal level of hemoglobin for males.")
    elif hemoglobin < 134:
        print("low level of hemoglobin for males.")
    else:
        print("high level of hemoglobin for males.")
elif g == 'F':
    if 117 <= hemoglobin <= 155:
        print("normal level of hemoglobin  for females")
    elif hemoglobin < 117:
        print("low level of hemoglobin females.")
    else:
        print("high level of hemoglobin for females.")
else:
    print("PLEASE PROVIDE CORRECT LETTER FOR GENDER")