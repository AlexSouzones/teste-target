import json

button_style = {
    "width": 30,
    "height": 4,
    "bg": "gray",
    "fg": "white",
    "font": ("Arial", 16),
}


def calculate_percentage(value: int | float, total: int | float) -> int | float:
    if total == 0:
        return 0
    return (value / total) * 100


def reverse_text(text: str) -> str:
    return text[::-1]


def is_fibonacci(number: int) -> bool:
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    if b == number:
        return True
    return False


def load_data(file_path: str) -> None:
    if file_path.endswith(".json"):
        with open(file_path, "r") as file:
            data = json.load(file)
            print(data)
    elif file_path.endswith(".xml"):
        ...


if __name__ == "__main__":
    ...
