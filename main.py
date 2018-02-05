database = "./data"
column = ["isim","numarasi","sinifi"]
def read(id, column=column[0]):
    with open(database) as dataread:
        source = dataread.read().splitlines()
    return source[id].split(",")[column.index(column)]
def add(string, data=""):
    dict = {}
    for s in [string]:
        for sp in s.split(","):
            key = sp.strip().split(":")[0]
            value = sp.strip().split(":")[1]
            dict [key] = value
    for r in column:
        data = data + dict[r] + ","
    with open(database,"a") as append:
        append.write(data[0:-1] + "\n")

add("isim:ali, sinifi:5K, numarasi:1001")
print read(0, "isim")
