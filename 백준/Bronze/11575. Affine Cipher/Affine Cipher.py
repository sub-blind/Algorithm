import sys

n = int(sys.stdin.readline())

for _ in range(n):
    multiplier, shift = map(int, sys.stdin.readline().split())
    original_text = sys.stdin.readline().strip()

    encrypted_text = []

    for character in original_text:
        alphabet_index = ord(character) - ord('A')
        encrypted_index = (multiplier * alphabet_index + shift) % 26
        encrypted_character = chr(encrypted_index + ord('A'))
        encrypted_text.append(encrypted_character)

    print("".join(encrypted_text))
