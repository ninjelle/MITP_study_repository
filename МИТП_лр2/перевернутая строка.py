def reverse_string(text):
    return ''.join(reversed(text))
while True:
    text = input("Your string: ")
    print(f"original string: {text}")
    print(f"reversed string: {reverse_string(text)}")
    print("-" * 30)
