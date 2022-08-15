sen=int(input())
maximom=0
pre_maximom=0
while sen!=-1:
    if sen>maximom:
        pre_maximom=maximom
        maximom=sen
    elif sen>pre_maximom:
        pre_maximom=sen
    sen=int(input())
print(maximom,pre_maximom)
