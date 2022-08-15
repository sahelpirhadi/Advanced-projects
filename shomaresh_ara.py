ray={}
n=int(input())
for i in range(0,n):
    name=input()
    ray[name]=ray.get(name,0)+1
list_ray=list(ray.keys())
list_ray.sort()
for i in list_ray:
    print(i,ray[i])
    
