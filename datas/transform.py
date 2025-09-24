import json

def transform_schedule_data(input_data):
    """
    Transform the schedule JSON structure to use initials as keys
    with only scheduleDetails as values.
    """
    transformed_data = {}
    
    for day, schedules in input_data.items():
        transformed_data[day] = {}
        
        for schedule in schedules:
            initial = schedule["initial"]
            schedule_details = schedule["scheduleDetails"]
            
            transformed_data[day][initial] = {
                "shift": schedule["shift"],
                "scheduleDetails": schedule_details
            }
    
    return transformed_data

def main():
    # Read the input JSON file
    # Replace 'input.json' with your actual file path
    try:
        with open('datas/schedule.json.bak', 'r', encoding='utf-8') as file:
            input_data = json.load(file)
    except FileNotFoundError:
        print("Error: input.json file not found. Please ensure the file exists.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input file.")
        return
    
    # Transform the data
    transformed_data = transform_schedule_data(input_data)
    
    # Write the transformed data to a new JSON file
    with open('transformed_schedule.json', 'w', encoding='utf-8') as file:
        json.dump(transformed_data, file, indent=2, ensure_ascii=False)
    
    print("Transformation complete! Output saved to 'transformed_schedule.json'")
    
    # Optional: Print a sample of the transformed data
    print("\nSample of transformed data (Monday first 2 entries):")
    monday_items = list(transformed_data.get('monday', {}).items())[:2]
    for initial, data in monday_items:
        print(f'"{initial}": {json.dumps(data, indent=2)}')

# Alternative function if you want to work with the data directly in memory
def transform_from_string(json_string):
    """
    Transform JSON data from a string instead of a file.
    """
    input_data = json.loads(json_string)
    return transform_schedule_data(input_data)

if __name__ == "__main__":
    main()