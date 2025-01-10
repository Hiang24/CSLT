def isInterger(s):
    x = ""
    l = r = -1
    for i in range(len(s)):
        if s[i] != " ":
            l = i
            break
    i = len(s) - 1
    while i > 0:
        if s[i] != " ":
            r = i
            break
        i -= 1
    if l == -1:
        return 0
    x = ""
    for i in range(l, r + 1):
        x += s[i]
    if (x[0] == "-") or (x[len(x)-1] == "+"):
        if len(x) == 1:
            return 0
        for i in range(1, len(x)):
            if not(x[i] >= "0" and x[i] <= "9"):
                return 0
        return 1
    for i in range(0, len(x)):
        if not(x[i] >= "0" and x[i] <= "9"):
            return 0
    return 1