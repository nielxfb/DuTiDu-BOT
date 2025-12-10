import threading

lock = threading.Lock()


def handle_rang(messages):
    rang_file = "datas/rang.txt"
    allowed_rooms = [
        "601",
        "602",
        "603",
        "604",
        "605",
        "606",
        "608",
        "609",
        "610",
        "613",
        "614",
        "621",
        "622",
        "623",
        "624",
        "625",
        "626",
        "627",
        "628",
        "629",
        "630",
        "631",
        "706",
        "708",
        "710",
        "711A",
        "721",
        "722",
        "723",
        "724",
        "725",
        "727",
        "729",
        "730",
        "731",
    ]

    lock.acquire()
    try:
        if len(messages) == 0 or (
            len(messages) == 1 and messages[0] not in allowed_rooms
        ):
            try:
                with open(rang_file, "r") as f:
                    current = f.read().strip()
                if current == "":
                    return "❌ Rang is not set. Use /rang <room_no> to set it."
                else:
                    return f"📍 Current rang: {current}"
            except FileNotFoundError:
                return "❌ Rang is not set. Use /rang <room_no> to set it."

        elif len(messages) == 1:
            room = messages[0]
            with open(rang_file, "w") as f:
                f.write(room)
            return f"✅ Rang set to {room}."
        else:
            return "❌ Usage: /rang | /rang <room_no>"

    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

    finally:
        lock.release()
