def RemoveDuplicates(arr):
    unique = set({})
    for i in arr:
        if not(i in unique):
            unique.add(i)
    return unique

def Merge(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    return arr1.union(arr2)

def CountUnique(string):
    words = set([x.lower() for x in string.split()])
    result = RemoveDuplicates(words)
    return len(result)

def FindSubList(st1, st2):
    if len(st1)>=len(st2):
        return st2.issubset(st1)
    else:
        return st1.issubset(st2)

def RemoveElements(st1, st2):
    result = st1.difference_update(st2)
    return result

def AnalyseSets(st1, st2, st3):
    one = st1.difference(st2, st3)
    three = st1.intersection(st2, st3)
    return one, three

def AnalyseText(line1, line2):
    line1 = set([x for x in line1.split()])
    line2 = set([x for x in line2.split()])
    same = line1.intersection(line2)
    uniq1 = line1
    uniq1.difference_update(line2)
    uniq2 = line2
    uniq2.difference_update(line1)
    return uniq1, uniq2, same
