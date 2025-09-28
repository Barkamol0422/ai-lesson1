import re, random, datetime, pytz
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = {
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Because of all their hot spots!"
}

history = []
last_suggestion = None

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    global last_suggestion
    print(Fore.CYAN + "TravelBot: Beaches, Mountains, Cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        last_suggestion = suggestion
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + f"TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
    else:
        print(Fore.RED + "TravelBot: I don't have that type of destination")
    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Packing versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(list(jokes))}")

def weather_info():
    city = normalize_input(input(Fore.YELLOW + "Enter a city: "))
    print(Fore.CYAN + f"TravelBot: Simulated weather in {city}: Sunny, 25°C.")

def news_update():
    print(Fore.GREEN + "TravelBot: Here's the latest travel news: Airports are offering discounts on international flights!")

def local_time():
    city = normalize_input(input(Fore.YELLOW + "Enter a city (Tokyo, Paris, New York): "))
    zones = {
        "tokyo": "Asia/Tokyo",
        "paris": "Europe/Paris",
        "new york": "America/New_York"
    }
    if city in zones:
        tz = pytz.timezone(zones[city])
        now = datetime.datetime.now(tz)
        print(Fore.CYAN + f"TravelBot: Local time in {city.title()} is {now.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't know that city.")

def save_history():
    with open("history.txt", "w") as f:
        f.write("\n".join(history))

def show_help():
    print(Fore.MAGENTA + "\nI can: ")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Show weather info (say 'weather')")
    print(Fore.GREEN + "- Give travel news (say 'news')")
    print(Fore.GREEN + "- Show local time (say 'time')")
    print(Fore.GREEN + "- Type 'exit' or 'bye' to end. \n")

def chat():
    print(Fore.CYAN + "Hello! I am TravelBot")
    name = input(Fore.YELLOW + "Your name?: ")
    print(Fore.GREEN + f"Nice to meet you {name}!")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        history.append(f"{name}: {user_input}")
        user_input = normalize_input(user_input)
        if re.search(r"\b(recommend|suggest)\b", user_input):
            recommend()
        elif re.search(r"\b(pack|packing)\b", user_input):
            packing_tips()
        elif re.search(r"\b(funny|joke)\b", user_input):
            tell_joke()
        elif re.search(r"\b(weather)\b", user_input):
            weather_info()
        elif re.search(r"\b(news|update)\b", user_input):
            news_update()
        elif re.search(r"\b(time|clock)\b", user_input):
            local_time()
        elif re.search(r"\b(help)\b", user_input):
            show_help()
        elif re.search(r"\b(exit|bye)\b", user_input):
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            save_history()
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
