def Backtrack(arr,cur,INPUT): # sample function to create a backtracking function not meant to RUN
    c = list()
    nc = 0;

    if is_a_solution(arr,cur,INPUT):
        process_solution(arr,cur,INPUT) # if ans is found processing solution
    else:
        cur = cur+1
        Construct_Candidate(arr,cur,INPUT,c,nc) #Construct the solution for subproblems
        for i in range(nc):
            arr[cur] = c[cur]
            make_move(arr,cur,INPUT) # makeing a move
            Backtrack(arr,cur,INPUT) # backtracking to move further
            unmake_move(arr,cur,INPUT)  # unmaking the move as if the Backtrack doesnt work

            if(finished):
                return # for terminating Backtrack early
