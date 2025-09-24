from datas.load import FileLoader

dayMapper = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
}

def handle_shift(messages):
    if len(messages) != 1:
        return f"❌ Usage: /shift <1-6>"
    
    day = messages[0]
    if not day.isdigit() or int(day) < 1 or int(day) > 6:
        return "❌ Day must be a number between 1 and 6"
    
    response = f"📅 Shift for {dayMapper[int(day)].capitalize()}\n"
    data = FileLoader().data
    if data is None:
        return "❌ Schedule data not found."
    data = data[dayMapper[int(day)]]
    initials = sorted(data.keys())
    pagi = []
    malam = []
    for initial in initials:
        if data[initial]['shift'] == 'P':
            pagi.append(initial)
        elif data[initial]['shift'] == 'M':
            malam.append(initial)
            
    response += f"\n🌅 Pagi ({len(pagi)}):\n" + ", ".join(pagi)
    response += f"\n🌃 Malam ({len(malam)}):\n" + ", ".join(malam)
    return response