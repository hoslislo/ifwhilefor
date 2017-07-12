# if while for
print "if --"
x = 1
if x > 0:
    print("yo")
else:
    print("dude")

print "while --"
x = 1
while x >= 0:
    print("yo" if x >= 0 else "dude")
    #x *= -1
    x += -1

print "for --"
for x in range(3, 8, 2):
    print(x)

print "done try 3"
# https://www.jetbrains.com/help/pycharm/publishing-a-project-on-github.html