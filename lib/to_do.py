
#def added_to_list(task):
    #return task

def added_to_list(tasks):
    newlist = []
    for task in tasks:
        if "#TODO" in task:
            newlist.append(task)
    return newlist
