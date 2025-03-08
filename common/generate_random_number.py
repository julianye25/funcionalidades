import random


def generate_unique_id(users):
    """Genera un ID único para cada usuario"""
    while True:
        new_id = random.randint(1, 1000)
        if not any(user["id"] == new_id for user in users):
            return new_id
