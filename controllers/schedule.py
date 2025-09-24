from datas.load import FileLoader

dayMapper = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
}

def handle_schedule(messages):
    if len(messages) != 2:
        print(messages)
        return f"❌ Usage: /schedule <XX> <1-6> | /jadwal <XX> <1-6>"

    initial = messages[0]
    day = messages[1]

    response = ""

    schedule = FileLoader().data
    if schedule is None:
        return "❌ Schedule data not found."
    if not day.isdigit() or int(day) < 1 or int(day) > 6:
        return "❌ Day must be a number between 1 and 6"
    schedule = schedule[dayMapper[int(day)]]
    exists = False
    initial = initial.upper() + "23-2"
    try:
        entry = schedule[initial]
        response += f"📅 {initial} - {dayMapper[int(day)].capitalize()}"
        for detail in entry['scheduleDetails']:
            exists = True
            response += f"\n- {detail['shiftSchedule']['name']} ({detail['shiftSchedule']['startTime']} - {detail['shiftSchedule']['endTime']}): {detail['description']}"

        if not exists:
            response += "\n- Free"
    except KeyError:
        return f"❌ Initial '{initial}' not found in schedule."
    
    return response
    