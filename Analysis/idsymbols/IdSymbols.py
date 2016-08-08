from Analysis.sql.Con import con


def get_id_symbols():
    return con.read_table("IDSymbol")

def get_symbol(id):
    return con.read_query("SELECT symbol from IDSymbol WHERE id = " + str(id))

#inserts the symbol into the df, given the id of the symbol.
# NOTE: the df need only be that ids symbol...
# Adds to every row in the dataframe the symbol
def insert_symbols(df, id):
    symbols = []
    rows_index = 0
    symbol = get_symbol(id)
    for row in range(0,df.shape[rows_index]):
        symbols.append(symbol)
    df["symbol"] = symbols
