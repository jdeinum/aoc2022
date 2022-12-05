def main():
    max = 0
    with open("input.txt","r") as i:
        calories = i.readline()
        amount = 0
        while calories != "":
            if calories == "\n" and amount > max:
                max = amount
            if calories == "\n":
                amount = 0
            else:
                amount += int(calories)
            calories = i.readline()
        i.close()
    print(max)

if __name__ == "__main__":
    main()