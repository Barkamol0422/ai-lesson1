def c():
    print("🤖 Hello! I’m your friendly chatbot.")
    while True:
        m=input("How are you feeling today? (happy, sad, angry, tired): ").lower()
        if m=="happy":
            print("😊 That’s awesome! Happiness is contagious.")
        elif m=="sad":
            print("😢 I’m sorry to hear that. I hope things get better soon.")
        elif m=="angry":
            print("😡 Take a deep breath... it helps to calm down.")
        elif m=="tired":
            print("😴 You should get some rest and recharge.")
        else:
            print("🤔 I’m not sure how to respond to that, but I’m here to chat!")
        t=input("What do you want to talk about? (sports, music, coding, exit): ").lower()
        if t=="sports":
            print("⚽ Sports are great! Do you like football or basketball more?")
        elif t=="music":
            print("🎵 Music heals the soul. What’s your favorite song?")
        elif t=="coding":
            print("💻 Coding is fun! Python is my favorite. Do you code too?")
        elif t=="exit":
            print("👋 Goodbye! Have a great day.")
            break
        else:
            print("Hmm, I don’t know much about that topic yet.")
        a=input("Do you want to keep chatting? (yes/no): ").lower()
        if a!="yes":
            print("👋 Okay, see you next time!")
            break
c()
