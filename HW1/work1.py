# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано: a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка - стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a, b, c = map(int, input('Введите стороны треугольника через пробел: ').split())

if a > 0 and b > 0 and c > 0 and a + b > c or a + c > b or b + c > a:

    if a != b and a != c and b != c:
        print('Разносторонний треугольник')
    elif a == b and a != c or a == c and b != c or b == c and a != c:
        print('Равнобедренный треугольник')
    elif a == b and a == c and b == c:
        print('Равносторонний треугольник')
else:
    print('Треугольник не существует')
