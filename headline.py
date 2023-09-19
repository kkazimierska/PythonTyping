def headline(text: str, upper: bool = False) -> str:
    if upper:
        return f"{text.upper()}\n{'-' * len(text)}"
    else:
        return f"{text}\n{'-' * len(text)}"



# print(headline("Implement clean and scalable code.", upper = "no"))
