"""
=== Exercise 1 Test Data ===
# Higher Realm Test Data
# Use these in your test functions:
test_values = [23, 12, 25]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
"""


# === base methods ===


def fireball(target: str) -> str:
    return f"Fireball hists {target}"


def ice_ball(damage: int) -> int:
    return damage


def heal(target: str) -> str:
    return f"Heals {target}"


def is_dragon(condition: str):
    return condition == "Dragon"


# === Higher-order functions ===


def spell_combiner(spell1, spell2) -> callable:
    """
    ２つの関数を受け取って、両方を実行する新しい関数を返す
    """
    def combined(target):
        r1 = spell1(target)
        r2 = spell2(target)
        return (r1, r2)
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    関数の結果を倍率で増やす関数を返す
    """
    def amplified(value: int):
        result = base_spell(value) * multiplier
        return result
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    条件がTrueのときだけ実行する関数を返す
    """
    def caster(target: str):
        if condition(target):
            return spell(target)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    """
    関数のリストを受け取り、順番に実行する関数を返す
    """
    def sequenced(target):
        results = []
        for spell in spells:
            results.append(spell(target))
        return results
    return sequenced


def main():
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon"))
    amplified = power_amplifier(ice_ball, 3)
    print(f"Original: {ice_ball(10)}  Amplified: {amplified(10)}")
    condition = conditional_caster(is_dragon, heal)
    print(condition("Dragon"))
    print(condition("Wizard"))
    sequenced = spell_sequence([fireball, heal])
    print(sequenced("Wizard"))


if __name__ == "__main__":
    main()
