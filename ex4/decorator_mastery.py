from functools import wraps
from typing import Any
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end-start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball():
    time.sleep(0.3)
    return "Fireball cast!"


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for s in name:
            if not (s.isalpha() or s == " "):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return "fuck"


def main():
    print()
    print("Testing spell timer...")
    result = fireball()
    print(result)
    guild = MageGuild()
    print(guild.cast_spell("Dragon", 20))
    print(guild.cast_spell("Dragon", 5))


if __name__ == "__main__":
    main()
