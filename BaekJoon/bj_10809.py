def findalp(text):
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    order=[]
    for i in alp:
        order.append(text.find(i))
    return order

text = input()
print(*findalp(text),end=" ")



    