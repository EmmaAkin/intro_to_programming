# you can write to stdout for debugging purposes, e.g.
# printf("this is a debug message\n");

def eqindexMultiPass(data):
    # "Multi pass"
    for i in range(len(data)):
        suml = sum(data[:i])
        sumr = sum(data[i+1:])

        if sumr==suml:

          print ("Index is:",i)

eqindexMultiPass([-1, 3, -4, 5, 1, -6, 2, 1])