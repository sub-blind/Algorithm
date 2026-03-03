while True:
    text = input()

    if text == "*":
        break

    text = text.lower() 
    is_pangram = True
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in text:
            is_pangram = False
            break

    if is_pangram:
        print("Y")
    else:
        print("N")