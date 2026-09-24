q = []

if  len(q) < 6:
    q.append(5)

if len(q) < 6:
    q.append(15)

if len(q) < 6:
    q.append(25)

if len(q) > 0 :
    q.remove(q[0])

if len(q) < 6:
    q.append(35)

if len(q) < 6:
    q.append(45)

if len(q) > 0 :
    q.remove(q[0])

if len(q) < 6:
    q.append(55)

print(q[0])

if len(q) < 6:
    q.append(65)

print(q)