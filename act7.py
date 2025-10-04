import random

m=['rock', 'paper', 'scissors']
h={'rock': 0, 'paper': 0, 'scissors': 0}
w={'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

def a():
    if sum(h.values())==0:
        return random.choice(m)
    p=max(h, key=h.get)
    return w[p]

def r(p, c):
    if p==c:
        return "d"
    elif w[p]==c:
        return "c"
    else:
        return "p"

def main():
    print("Rock Paper Scissors AI\nType 'rock', 'paper', or 'scissors'. Type 'quit' to exit.\n")
    ps=0
    cs=0
    t=0
    while True:
        u=input("Your move: ").lower()
        if u=='quit':
            print("\nGame Over")
            break
        if u not in m:
            print("Invalid\n")
            continue
        c=a()
        print(f"AI: {c}")
        o=r(u, c)
        t+=1
        if o=="d":
            print("Draw\n")
        elif o=="p":
            ps+=1
            print("You win\n")
        else:
            cs+=1
            print("AI wins\n")
        h[u]+=1
        print(f"Score after {t}: You {ps} - AI {cs}\n")

if __name__=="__main__":
    main()
