from textblob import TextBlob

h=[]
p=0
n=0
u=0

def a(t):
    global p,n,u
    s=TextBlob(t).sentiment.polarity
    if s>0:
        p+=1
        return "Positive"
    elif s<0:
        n+=1
        return "Negative"
    else:
        u+=1
        return "Neutral"

while True:
    x=input("You: ")
    if x.lower()=="exit":
        print("Report:")
        print("Positive:",p)
        print("Negative:",n)
        print("Neutral:",u)
        print("History:")
        for y in h:
            print(y)
        break
    elif x.lower()=="stats":
        print("Positive:",p,"Negative:",n,"Neutral:",u)
    elif x.lower()=="reset":
        p=n=u=0
        h=[]
        print("Data reset")
    elif x.lower()=="history":
        for y in h:
            print(y)
    else:
        r=a(x)
        h.append((x,r))
        print("Bot:",r)
