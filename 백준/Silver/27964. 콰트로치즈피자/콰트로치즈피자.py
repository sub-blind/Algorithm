N = int(input())
cheeses = input().split()
t = set()

for cheese in cheeses:
    if cheese.endswith("Cheese"):
        t.add(cheese)

print("yummy" if len(t) >= 4 else "sad")