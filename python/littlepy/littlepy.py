#littlepy
#it compresses some python commands into a letter or so
#dumb

inp=input("> ")
#registries
r=0
a=0
b=0
c=0
d=0
e=0

#commands:
#a-e: save r to a through e
#A-E: save a-e to r 
#): r to int
#?: send input to r
#=: save the result of if a == b to c
#+: add a and b, save to c
#-: subtract a and b, save to c
#*: multiply a and b, save to c
#/: divide a and b, save to c
#!: prints r
#0-9: save 0-9 into r

for i in inp:
    if i=="a":
        a=r
    if i=="b":
        b=r
    if i=="c":
        c=r
    if i=="d":
        d=r
    if i=="e":
        e=r
    if i=="A":
        r=a
    if i=="B":
        r=b
    if i=="C":
        r=c
    if i=="D":
        r=d
    if i=="E":
        r=e
    if i==")":
        r=int(r)
    if i=="?":
        r=input("?")
    if i=="=":
        c=a==b
    if i=="+":
        c=a+b
    if i=="-":
        c=a-b
    if i=="*":
        c=a*b
    if i=="/":
        c=a/b
    if i=="!":
        print(r)
    if i in "0123456789":
        r=int(i)
