import random
from typing import Generator


AVAILABLE_NAMES = ['John', 'Jane', 'Mary', 'David', 'Alex', 'Max' 'Nick',
                   'Anastasia', 'Leo']
AVAILABLE_COLORS = ['blue', 'green', 'brown', 'grey', 'black']


class User:

    def __init__(self, name: str, nickname: str, age: int, eyes_color: str):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.eyes_color = eyes_color

    @property
    def info(self) -> dict:
        return {
            "Name": self.name,
            "Nickname": self.nickname,
            "Age": self.age,
            "Eyes_color": self.eyes_color
        }

    def __str__(self) -> str:
        return self.nickname

    def __repr__(self) -> str:
        return self.nickname

    def __ge__(self, other) -> bool:
        return self.age >= other.age

    def __gt__(self, other) -> bool:
        return self.age > other.age

    def __le__(self, other) -> bool:
        return self.age <= other.age

    def __lt__(self, other) -> bool:
        return self.age < other.age

    def __eq__(self, other) -> bool:
        return self.age == other.age


def users_generator(number: int) -> Generator[User, None, None]:
    def get_random_name() -> str:
        return random.choice(AVAILABLE_NAMES)

    def get_random_color() -> str:
        return random.choice(AVAILABLE_COLORS)

    def get_random_age() -> int:
        return random.randint(0, 100)

    def get_random_nickname(name: str) -> str:
        random_nickname_number = random.randint(10000, 99999)
        return f"{name}{random_nickname_number}"

    for _ in range(number):
        random_name = get_random_name()
        random_color = get_random_color()
        random_age = get_random_age()
        random_nickname = get_random_nickname(random_name)

        yield User(
            name=random_name,
            nickname=random_nickname,
            age=random_age,
            eyes_color=random_color
        )


def main():
    gen = users_generator(50)
    for num, user in enumerate(gen):
        print(f"#{num+1}", user.info)


if __name__ == '__main__':
    main()
