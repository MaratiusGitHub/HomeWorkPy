# задача 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# ¬ - Отрицание "не"
# ⋁ - "или"
# ⋀ - "и"

for x in True, False:
    for y in True, False:
        for z in True, False:
            if not (x or y or z) == ((not (x) and (not (y) and (not (z))))):
                print(f'True if x = {x}, y = {y}, z ={z}')
            else:
                print('False')
