def nFacRuntimeFunc(n):
    if n <= 0:
        return
    for i in range(n):
        nFacRuntimeFunc(n-1)

nFacRuntimeFunc(3)