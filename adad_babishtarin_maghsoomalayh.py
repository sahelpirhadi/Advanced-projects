def tedad_maghsoom(a):
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count=count+1
    return count

maximom=0
final_adad=0
for i in range(0,5):
    adad=int(input())
    maghsoom_count=tedad_maghsoom(adad)
    if maghsoom_count>maximom:
        maximom=maghsoom_count
        final_adad=adad
    if maghsoom_count==maximom:
        if adad>final_adad:
            final_adad=adad
print(final_adad,maximom)
    
        
