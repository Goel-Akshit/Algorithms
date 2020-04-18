from stack import Stack


def match_brackets(_input):
    reverse_dict = {"{": "}", "(": ")", "[": "]", "<": ">"}
    symbols = ["{","(", "[", "<"]
    reverse = [">","]","}", ")", ]
    stacki = Stack()
    maxi = 0
    continuous = False
    count = 0

    for i in _input:
        if i in symbols:
            #calculating internal depth
            if continuous:
                maxi = max(maxi, count+len(stacki)) #len helps to match total depth internal + begning
                continuous = False
                count = 0
            stacki.push(i)
        elif i in reverse:
            poped = stacki.pop()
            try:
                if i != reverse_dict[poped]:
                    return "Invalid"
            except:
                return "Invalid"
            count += 1
            continuous = True
    #calculating external depth at the last of string
    maxi = max(maxi, count+len(stacki))

    if stacki.isempty():
        return "{} and highest depth is {}".format("Valid", maxi)
    else:
        return "Invalid"

def main():
    string_input = input()
    x = match_brackets(string_input)
    print(x)



if __name__ == "__main__":
    main()
