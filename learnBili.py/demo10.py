file = open('c.txt','a')
file.write('hello')
file.close()
file.write('world')
file.flush()