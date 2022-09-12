from ortools.sat.python import cp_model

def main():
    num_cont = 5
    num_shifts = 2
    num_days = 7

    all_cont = range(num_cont)
    all_shifts = range(num_shifts)
    all_days = range(num_days)

    shift_requests = [[[0, 0 ], [0, 0], [0, 0], [0, 0], [0, 1],
                       [0, 1], [0, 0]],
                      [[0, 0], [0, 0], [1, 0], [1, 0], [0, 0],
                       [0, 0], [0, 0]],
                      [[0, 1,], [1, 0], [0, 0], [1,0], [0, 0],
                       [0, 1], [0, 0]],
                      [[0, 0,], [0, 0], [1,0], [1, 0], [0, 0],
                       [1, 0], [0, 0]],
                      [[0, 0], [0, 1], [1, 0], [0,0], [1, 0],
                       [0, 1], [0, 0]]]

    # create the model
    model = cp_model.CpModel()

    # create the shift variables
    # shifts[(n,d,s)] == controller works shift 's' on day 'd' 
    shifts = {}
    for n in all_cont:
        for d in all_days:
            for s in all_shifts:
                shifts[(n,d,s)] = model.NewBoolVar('shift_n%id%is%i' % (n,d,s))
    
    # each shift is assigned to exactly one controller
    # this will need to be changed to have ~10 controllers on shift
    for d in all_days:
        for s in all_shifts:
            model.AddExactlyOne(shifts[(n,d,s)] for n in all_cont)

    # ensure each controller only works one shift per day
    for n in all_cont:
        for d in all_days:
            model.AddAtMostOne(shifts[(n,d,s)] for s in all_shifts)

    """ distribute the shifts as evenly as possible so that each controller works 
    min_shifts_per_cont.
    if this isnt possible due to the number of shifts being divisible by the number of controllers
    some controllers will be allocated an extra shift """
    min_shifts_per_cont = (num_shifts * num_days) // num_cont

    if num_shifts * num_days % num_cont == 0:
        max_shifts_per_cont = min_shifts_per_cont
    else:
        max_shifts_per_cont = min_shifts_per_cont + 1
    
    for n in all_cont:
        num_shifts_worked = 0
        for d in all_days:
            for s in all_shifts:
                num_shifts_worked += shifts[(n,d,s)]
        model.Add(min_shifts_per_cont <= num_shifts_worked)
        model.Add(num_shifts_worked <= max_shifts_per_cont)

    
