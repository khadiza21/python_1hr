
def numberOfEmployeesFullTarget( hours, target):
    num_emp = 0
    for hr in hours:
        if hr>=  target:
            num_emp = num_emp +1
    return num_emp


hours = [0,1,2,3,2,1,3,4,5,3]
target = 2

print (numberOfEmployeesFullTarget(hours, target))
