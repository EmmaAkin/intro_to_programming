def getarray(arr, i):
    for i in range()
    for (var j=0, l=arg[i].length; j<l; j++) {
            var a = arr.slice(0); // clone arr
            a.push(arg[i][j]);
            if (i==max)
                r.push(a);
            else
                helper(a, i+1);
        }
    pass

def knightsmoves(x, y):
    delta = x-y

    if(y>delta):
        return 2 * floor((y - delta) / 3) + delta
    else:
        return delta - 2 * floor((delta - y) / 4)
