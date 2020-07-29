names=("shiv","kiran","rahul")
comps=("dell","hp","asus")
ram=("2","3","4")
zipped=list(zip(names,comps,ram)) #we can use set also instead of list but order doesn't
print(zipped)
#or we can itrate here also
for (a,b,c) in zipped:
    print(a,b,c)
