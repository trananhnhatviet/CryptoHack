def ToReducedRowEchelonForm(M):
    ## If M is empty, no need to proceed, and just return
    if not M: return
    ## if rows are less than column, lead variable used to check that, for every row increment, lead incremented by 1 and if its value greater than or equal to column count, return    
    lead = 0
    ## No of rows in Matrix
    rowCount = len(M)
    ## No of columns in Matrix
    columnCount = len(M[0])
    ## Iterating row of Matrix
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        ## If leading element of that row itself 0, check next row's leading element if its zero or not
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        ## Swap Rows i and r --> will happen only if lead element M[i][lead] equal to 0 and i is not equal to rowCount
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        ## Making Lead Entry -- 1
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        ## Each column will have single Non-Zero entry
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
    return M

M = [[6, 2, -3],[5, 1, 4],[2, 7, 1]]

M = (ToReducedRowEchelonForm(M))

for i in M:
    print(i)