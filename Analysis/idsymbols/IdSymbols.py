from Analysis.sql.Con import con


def get_id_symbols():
    return con.read_table("IDSymbol")