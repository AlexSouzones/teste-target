import json
import webbrowser

button_style = {
    "width": 25,
    "height": 2,
    "bg": "gray",
    "fg": "white",
    "font": ("Arial", 20),
}

button_style_pages = {
    "width": 12,
    "height": 1,
    "bg": "gray",
    "fg": "white",
    "font": ("Arial", 14),
}

label_style_pages = {
    "width": 15,
    "height": 1,
    "bg": "black",
    "fg": "white",
    "font": ("Arial", 16),
}

label_style_result = {
    "width": 40,
    "height": 3,
    "bg": "white",
    "fg": "black",
    "font": ("Arial", 14),
}

label_style_title = {
    "width": 20,
    "height": 1,
    "bg": "#FF7F50",
    "fg": "white",
    "font": ("Arial", 20),
}

label_style_info = {
    "font": ("Arial", 16),
    "bg": "#98FB98",
    "fg": "black",
    "padx": 10,
    "pady": 10,
    "anchor": "w",
    "justify": "left",
    "wraplength": 420,
}


def linkedin_link():
    url = "https://www.linkedin.com/in/alexandre-p-souza-0b9532211"
    webbrowser.open(url)
    

def github_link():
    url = "https://github.com/AlexSouzones"
    webbrowser.open(url)


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
