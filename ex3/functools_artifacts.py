"""
=== Exercise 3 Test Data ===
# Ancient Library Test Data
spell_powers = [34, 21, 10, 18, 18, 18]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [20, 8, 17]
"""
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    operationをもとにlistの中身を計算して結果を返す関数を返す
    operation: "add", "multiply", "max", "min"
    """
    if not spells:
        return "No spells"
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        return ("Unknown operation")


def base_enchantment(power: int, element: str, target: str):
    return f"Power: {power}, Element: {element}, Target: {target}"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = partial(base_enchantment, 50, "fire")
    ice = partial(base_enchantment, 50, "ice")
    lightning = partial(base_enchantment, 50, "lightning")

    return {
        "fire_enchantment": fire,
        "ice_enchantment": ice,
        "lightning_enchantment": lightning
    }


@lru_cache(maxsize=None)
def memorized_fibonacci(n: int) -> int:
    if n < 0:
        return "number must be >= 0"
    if n <= 1:
        return n
    return memorized_fibonacci(n - 1) + memorized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(x):
        return "Unknown spell"

    @cast.register(int)
    def _(x: int):
        return f"Damage: {x}"

    @cast.register(str)
    def _(x: str):
        return f"Enchantment: {x}"

    @cast.register(list)
    def _(xs: list):
        results = []
        for item in xs:
            results.append(cast(item))
        return results
    return cast


def main():
    print()
    print("Testing spell reducer...")
    test_list = [1, 2, 3, 4, 5]
    result_add = spell_reducer(test_list, "add")
    result_mul = spell_reducer(test_list, "multiply")
    result_max = spell_reducer(test_list, "max")
    result_min = spell_reducer(test_list, "min")
    print(f"Sum: {result_add}")
    print(f"Product: {result_mul}")
    print(f"Max: {result_max}")
    print(f"Min: {result_min}")
    print()

    print("Testing partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire_enchantment"]("Dragon"))
    print()

    print("Testing memorized fibonacci...")
    num = 10
    print(f"Fib({num}): {memorized_fibonacci(num)}")
    print()

    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(f"int case: {cast(10)}")
    print(f"str case: {cast("hi")}")
    print(f"str case: {cast([10, "Ice", 7])}")


if __name__ == "__main__":
    main()
