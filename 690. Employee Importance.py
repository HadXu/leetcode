class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


def getImportance(employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    d = {e.id: e for e in employees}
    stk = [d[id]]
    ret = 0
    while stk:
        top = stk.pop()
        ret += top.importance
        for n in top.subordinates:
            stk.append(d[n])
    return ret


if __name__ == '__main__':
    pass
