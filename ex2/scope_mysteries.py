def mage_counter() -> callable:
    """
    何回呼ばれたかを数える関数を返す
    """
    count = 0

    def counter():
        """
        nonlocal: メソッドの内側から外側の変数を更新する時に必要
        """
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """
    渡された引数で要素(item)をエンチャント(enchantment_type)する
    """
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    """
    dictで記憶の保管庫を作成する
    """
    mem = {}

    def store(key: str, value):
        mem[key] = value

    def recall(key: str):
        if key in mem:
            return mem[key]
        return "Memory not found"
    return {"store": store, "recall": recall}


def main():
    print()
    print("Testing mage counter...")
    count = mage_counter()
    print(f"Call 1: {count()}")
    print(f"Call 2: {count()}")
    print(f"Call 3: {count()}")
    print()

    print("Testing spell accumulator")
    accumulate = spell_accumulator(10)
    print(f"Call 1: {accumulate(2)}")
    print(f"Call 2: {accumulate(3)}")
    print(f"Call 3: {accumulate(4)}")
    print()

    print("Testing enchantment factory")
    flame = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frozen("Shield"))
    print()

    print("Testing memory vault")
    vault = memory_vault()
    vault["store"]("name", "Ryuichi")
    print(vault["recall"]("name"))
    print(vault["recall"]("age"))


if __name__ == "__main__":
    main()
