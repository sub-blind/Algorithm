def get_sub_name(first_char):
    if first_char == 'F':
        return "Foundation"
    elif first_char == 'C':
        return "Claves"
    elif first_char == 'V':
        return "Veritas"
    else:
        return "Exploration"


def main():
    sub_num = input().strip()
    first = sub_num[0]
    print(get_sub_name(first))


if __name__ == "__main__":
    main()
