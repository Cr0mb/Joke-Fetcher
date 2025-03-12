import requests

def get_joke(category):
    if category == "ten":
        url = "https://official-joke-api.appspot.com/random_ten"
    elif category == "random":
        url = "https://official-joke-api.appspot.com/random_joke"
    else:
        url = f"https://official-joke-api.appspot.com/jokes/{category}/random"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        jokes = response.json()
        
        if isinstance(jokes, list):
            joke = jokes[0]
            return joke['setup'], joke['punchline']
        elif isinstance(jokes, dict):
            return jokes['setup'], jokes['punchline']
        else:
            print("Error: No joke found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None

def display_joke():
    categories = ['programming', 'general', 'random', 'ten']

    print("Select a joke category:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category.capitalize()}")

    try:
        category_choice = int(input("\nEnter the number of the category: "))
        if 1 <= category_choice <= len(categories):
            selected_category = categories[category_choice - 1]
            joke = get_joke(selected_category)
            if joke:
                setup, punchline = joke
                print(f"\n{setup}")
                input("Press Enter to see the punchline...")
                print(f"{punchline}\n")
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    while True:
        display_joke()
        again = input("Do you want another joke? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break
