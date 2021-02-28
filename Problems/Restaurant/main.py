import itertools

main_course_menu = [each for each in zip(main_courses, price_main_courses)]
desserts_menu = [each for each in zip(desserts, price_desserts)]
drinks_menu = [each for each in zip(drinks, price_drinks)]
for a, b, c in itertools.product(main_course_menu, desserts_menu, drinks_menu):
    if (a[1] + b[1] + c[1]) <= 30:
        print(f"{a[0]} {b[0]} {c[0]} {(a[1] + b[1] + c[1])}")
