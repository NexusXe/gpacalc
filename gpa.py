def calc(percents, credits):
    if len(percents) < len(credits):
        raise ValueError('Not every input credit amount has a corresponding percentage.')
    if len(percents) > len(credits):
        raise ValueError('Not every input percentage has a corresponing credit amount.')
    credits = [float(i) for i in credits]
    percents = 

lst = [1,3,6,3,2,1]

lst = [float(i) for i in lst]

print(lst)