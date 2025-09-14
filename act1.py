name=input("What is your name: ")
print(f"Hello, {name}, I am your Chatbot")
n=input("How is your mood(good/bad):").lower()
if n=="good":
    print("I am glad to hear that.")
elif n=="bad":
    print("I am sorry to hear that.")
else:
    print("I see, Sometimes it is hard to put feelings into words.")
print(f"It was nice chatting with you, {name}, bye")
