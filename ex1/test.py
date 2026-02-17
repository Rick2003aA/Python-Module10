def fireball(target: str) -> str:
    return f"Fireball hists {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def damage(value: int) -> int:
    return value


def is_dragon(target: str) -> bool:
    return target == "Dragon"


def spell_combiner(spell1, spell2):
    def combined(target):
        r1 = spell1(target)
        r2 = spell2(target)
        return (r1, r2)
    return combined


def power_amplifier(base_spell, multiplier: int):
    def amplified(value: int):
        result = base_spell(value) * multiplier
        return result
    return amplified


def conditional_caster(condition, spell):
    def caster(target):
        if condition(target):
            return spell(target)
        return "Spell fizzled"
    return caster


test1 = spell_combiner(fireball, heal)
print(test1("Dragon"))
test2 = power_amplifier(damage, 3)
print(test2(10))
test3 = conditional_caster(is_dragon, heal)
print(test3("Dragon"))
print(test3("Goblin"))
