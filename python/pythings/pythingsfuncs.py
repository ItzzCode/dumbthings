class display():
    def displayScreen(mem,xmax,ymax):
        for i in range(len(mem)):
            print(mem[i],end="")
            if i % xmax == 0 and i != 0:
                print("")

class misc():
    def createList(length):
        return list("#"*length)


if __name__ == "__main__":
    print("Run main, lol.")