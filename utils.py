from datetime import datetime

def save_output(text):
    filename = f"outputs/content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    return filename