import pythingsfuncs as f

def main():
    xmax = 10 
    ymax = 10
    scr = f.misc.createList(100)
    print(scr)
    mem = f.misc.createList(30)
    f.display.displayScreen(scr,xmax,ymax)
    print(mem)
    return 0

if __name__ == "__main__":
    main()
else:
    print("huh")