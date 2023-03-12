while True:
    def flames(name1, name2):
        name1 = name1.lower().replace(" ", "")
        name2 = name2.lower().replace(" ", "")
        flames = "FLAMES"
        for char in name1:
            if char in name2:
                name2 = name2.replace(char, "", 1)
                name1 = name1.replace(char, "", 1)
        count = len(name1) + len(name2)
        while len(flames) > 1:
            index = (count % len(flames)) - 1
            if index >= 0:
                flames = flames[:index] + flames[index+1:]
            else:
                flames = flames[:len(flames)-1]
        return flames.upper()

    #Example usage
    name1 = input("Enter First Name:")
    name2 = input("Enter Second Name:")
    result = flames(name1, name2)
    print(f"The FLAMES relationship between {name1} and {name2} is {result}")
