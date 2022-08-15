jomle=input()
jomle=jomle.upper()
if "BA" in jomle:
    if "ABA" in jomle:
        print("NO")
    elif "BAB" in jomle:
        print("NO")
    elif "BA" in jomle:
        print("YES")
else:
    print("NO")
