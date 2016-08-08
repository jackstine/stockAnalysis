from Analysis.sql.Con import con

def readTable(table):
    return con.read_query("SELECT * FROM " + table)

def getTables():
    return con.read_query("SELECT TABLE_NAME FROM information_schema.tables WHERE TABLE_TYPE <> 'SYSTEM VIEW'")

def convertTablesToCVS():
    count = 0
    t = getTables()
    for a in t["TABLE_NAME"]:
        ti = readTable(a)
        print a
        ti.to_csv(path_or_buf="~/tables/" + a + ".csv", sep=",", chuncksize = 100000)