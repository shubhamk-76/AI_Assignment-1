import json
def load_data(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

file_path = 'indian_cities_data.json'
knowledge_base = load_data(file_path)

def recommend_destination(preferred_weather, budget):
    recommended_destinations = []
    for destination in knowledge_base:
        if destination['weather'].lower() == preferred_weather.lower() and \
           destination['rating'] >= 7.0 and \
           destination['budget']['min'] <= budget <= destination['budget']['max']:
            recommended_destinations.append(destination['city'])
    return recommended_destinations

def add_new_destination():
    new_destination = input("Enter the new destination: ")
    if any(dest['city'].lower() == new_destination.lower() for dest in knowledge_base):
        print("Destination already exists.")
        return
    
    rating = float(input(f"Rate {new_destination} on a scale of 10: "))
    knowledge_base.append({
        "city": new_destination,
        "weather": input(f"Enter the weather for {new_destination}: "),
        "famous_food": input(f"Enter the famous foods for {new_destination} (comma-separated): ").split(','),
        "rating": rating,
        "feedback": []
    })
    print(f"{new_destination} added with a rating of {rating}")

def add_feedback():
    destination = input("Enter the destination you want to provide feedback for: ")
    matching_destinations = [dest for dest in knowledge_base if dest['city'].lower() == destination.lower()]
    if not matching_destinations:
        print("Destination not found.")
        return
     
    feedback_text = input("Enter your feedback: ")
    matching_destinations[0]['feedback'].append(feedback_text)
    print("Feedback added successfully!")

def display_destinations():
    print("Available destinations:")
    for destination in knowledge_base:
        print(f"- {destination['city']} (Weather: {destination['weather']}, Rating: {destination['rating']})")
def display_feedback_for_destination():
    display_destinations()  # Display available destinations
    destination_name = input("Enter the name of the destination to view feedback: ").strip().lower()
    
    # Find the destination in the knowledge base
    matching_destinations = [dest for dest in knowledge_base if dest['city'].lower() == destination_name]
    
    if not matching_destinations:
        print("Destination not found.")
        return
    
    # Display feedback for the destination
    print(f"Feedback for {destination_name}:")
    for feedback in matching_destinations[0]['feedback']:
        print("-", feedback)
def check_destination_rating():
    display_destinations()  # Display available destinations
    destination_name = input("Enter the name of the destination to check its rating: ").strip().lower()

    # Find the destination in the knowledge base
    matching_destinations = [dest for dest in knowledge_base if dest['city'].lower() == destination_name]

    if not matching_destinations:
        print("Destination not found.")
        return

    # Display the rating for the destination
    print(f"Rating of {destination_name} is: {matching_destinations[0]['rating']}")
def give_feedback_for_destination():
    display_destinations()  # Display available destinations
    destination_name = input("Enter the name of the destination to give feedback: ").strip().lower()

    # Find the destination in the knowledge base
    matching_destinations = [dest for dest in knowledge_base if dest['city'].lower() == destination_name]

    if not matching_destinations:
        print("Destination not found.")
        return

    feedback_text = input("Enter your feedback for this destination: ")
    matching_destinations[0]['feedback'].append(feedback_text)
    print("Feedback added successfully!")
def display_city_information():
    display_destinations()  # Display available destinations
    destination_name = input("Enter the name of the destination to view information: ").strip().lower()

    # Find the destination in the knowledge base
    matching_destinations = [dest for dest in knowledge_base if dest['city'].lower() == destination_name]

    if not matching_destinations:
        print("Destination not found.")
        return

    # Display information for the destination
    print(f"\nInformation for {destination_name}:")
    print(f"Weather: {matching_destinations[0]['weather']}")
    print(f"Famous Food: {', '.join(matching_destinations[0]['famous_food'])}")
    print(f"Rating: {matching_destinations[0]['rating']}")
    print(f"Budget Range: {matching_destinations[0]['budget']['min']} - {matching_destinations[0]['budget']['max']}")
    print(f"Feedback:")
    for feedback in matching_destinations[0]['feedback']:
        print(f"- {feedback}")
    print("\n")

def main():
    print("Welcome to the Travel Advisory System!")
    
    preferred_weather = input("Enter the preferred weather condition for the place: ")
    budget = int(input("Enter Budget in integer value : "))
    
    recommended_destinations = recommend_destination(preferred_weather, budget)
    print("Recommended places:", recommended_destinations)
    while True:
        print("Press 1 if you want to go to a specific destination")
        print("Press 2 if you want to read feedback of a particular destination")
        print("Press 3 if you want to check the rating of certain destination ")
        print("Press 4 if you want to give feedback to a certain destination")
        print("Press 5 if want to add any destination")
        print("Press 6 if you want to exit")
        action=int(input())
        if(action == 1):
            display_city_information()
        elif(action==2):
            print("---------Following is the feedback of a particular destination --------------")
            display_feedback_for_destination()
        elif(action==3):
            check_destination_rating()
        elif(action==4):
            give_feedback_for_destination()
        elif(action==5):
            add_new_destination()
        else:
            break
    with open(file_path, 'w') as json_file:
        json.dump(knowledge_base, json_file, indent=4)
    print("--------------- Apka yatra mangalmay ho ---------------------- ")
if __name__ == "__main__":
    main()
