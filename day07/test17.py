f = open('test16.txt', 'rt')
rows = f.readlines()
for row in rows:
    print(row)
f.close()



# while True:
#     row = f.readline()
#     print(row)
#     if not row:
#         break
# f.close()