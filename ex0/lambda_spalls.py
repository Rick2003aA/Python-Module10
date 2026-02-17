"""
=== Exercise 0 Test Data ===
# Lambda Sanctum Test Data
artifacts = [{'name': 'Storm Crown', 'power': 83, 'type': 'focus'},
             {'name': 'Light Prism', 'power': 115, 'type': 'weapon'},
             {'name': 'Ice Wand', 'power': 95, 'type': 'relic'},
             {'name': 'Storm Crown', 'power': 88, 'type': 'weapon'}]

mages = [{'name': 'Zara', 'power': 97, 'element': 'wind'},
         {'name': 'Ash', 'power': 65, 'element': 'ice'},
         {'name': 'Sage', 'power': 89, 'element': 'fire'},
         {'name': 'River', 'power': 84, 'element': 'lightning'},
         {'name': 'Jordan', 'power': 59, 'element': 'ice'}]
spells = ['freeze', 'flash', 'darkness', 'earthquake']
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    return sort(artifacts["power"])
    の処理をlambdaを用いて関数を作成せずに行う
    """
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    return (bool)
    の処理をlambdaを用いて関数を作成せずに行う
    """
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    return f"* {s} *"
    の処理をlambdaを用いて関数を作成せずに行う
    """
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda p: p["power"], mages))
    return dict({
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    })


def main():
    print("Testing artifact sorter...")
    artifacts = [{'name': 'Storm Crown', 'power': 83, 'type': 'focus'},
                 {'name': 'Light Prism', 'power': 115, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 95, 'type': 'relic'},
                 {'name': 'Storm Crown', 'power': 88, 'type': 'weapon'}]

    mages = [{'name': 'Zara', 'power': 97, 'element': 'wind'},
             {'name': 'Ash', 'power': 65, 'element': 'ice'},
             {'name': 'Sage', 'power': 89, 'element': 'fire'},
             {'name': 'River', 'power': 84, 'element': 'lightning'},
             {'name': 'Jordan', 'power': 59, 'element': 'ice'}]

    spells = ['freeze', 'flash', 'darkness', 'earthquake']

    try:
        sort_result = artifact_sorter(artifacts)
        mage_result = power_filter(mages, 85)
        spells_result = spell_transformer(spells)
        int_result = mage_stats(mages)
        for info in sort_result:
            print(info)
        print()
        for m_info in mage_result:
            print(m_info)
        print()
        for s_info in spells_result:
            print(s_info, end="")
        print()
        for i in int_result.items():
            print(i)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
