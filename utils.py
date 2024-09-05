import json
import webbrowser
import xml.etree.ElementTree as ET

button_style = {
    "width": 25,
    "height": 2,
    "bg": "gray",
    "fg": "white",
    "font": ("Arial", 20),
}

button_style_pages = {
    "width": 14,
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

label_style_legend = {
    "width": 40,
    "height": 3,
    "bg": "slategray",
    "fg": "white",
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

input_style_frame = {
    "font": ("Arial", 14),
    "bg": "white",
    "fg": "black",
    "width": 10,
    "justify": "center",
}


def linkedin_link() -> None:
    url = "https://www.linkedin.com/in/alexandre-p-souza-0b9532211"
    webbrowser.open(url)


def github_link() -> None:
    url = "https://github.com/AlexSouzones"
    webbrowser.open(url)


def processar_valor(entry: str) -> None | float:
    valor_numerico = entry.replace(".", "").replace(",", ".").replace("R$", "")
    try:
        valor_float = float(valor_numerico)
    except ValueError:
        valor_float = None

    return valor_float


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


def load_data(file_path: str) -> None | list[dict[str, int, float]]:
    if file_path.lower().endswith(".json"):
        with open(file_path, "r") as file:
            data = json.load(file)
            info = [dicionario for dicionario in data if dicionario["valor"] > 0]
            if info:
                return info
            return None


def calculate_mid_value(info_values: list[dict[str, int, float]]) -> int | float:
    values = [info["valor"] for info in info_values]
    mid = sum(values) / len(values)
    return mid


def state_values(info_values: list[dict[str, int, float]]) -> dict[str, int, float]:
    max_value = info_values[0]
    min_value = info_values[0]
    mid_value = calculate_mid_value(info_values)
    best_days = 0
    for info in info_values:
        if info["valor"] < min_value["valor"]:
            min_value = info
        if info["valor"] > max_value["valor"]:
            max_value = info
        if info["valor"] > max_value["valor"]:
            max_value = info
        if info["valor"] > mid_value:
            best_days += 1
    return {
        "min value": min_value,
        "max value": max_value,
        "mid value": mid_value,
        "best days": best_days,
    }


if __name__ == "__main__":
    ...
