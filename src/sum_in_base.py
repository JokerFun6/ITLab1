def add_in_base(a: str, b: str, base: int) -> str:
    """
    Складывает два числа, записанных в системе счисления с основанием base.

    :param a: первое число, строка (например, "1011")
    :param b: второе число, строка (например, "111")
    :param base: основание системы счисления, 2 <= base <= 36
    :return: сумма в той же системе счисления, строка

    Пример:
        add_in_base("1011", "111", 2) -> "10010"
        add_in_base("FF", "1", 16) -> "100"
    """

    if not 2 <= base <= 36:
        raise ValueError("Система счисления должна быть между 2 и 36")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid = set(digits[:base])

    for operand in (a, b):
        if not operand or any(ch.upper() not in valid for ch in operand):
            raise ValueError(f"Неверная цифра в операнде - {operand!r} для системы счисления {base}")

    