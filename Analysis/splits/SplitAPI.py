from sql.Con import con

def read_splits():
    return con.read_table("SplitHistory")

def get_split_from_id(id):
    return con.read_query("SELECT * FROM SplitHistory WHERE id = " + str(id))

#TODO look at numpy arrays and see if they are better, I think they are
def get_split_from_ids(ids):
    splits = []
    for id in ids:
        splits.append(get_split_from_id(id))
    return splits

def has_splits(id):
    return get_split_from_id(id).shape[0] != 0