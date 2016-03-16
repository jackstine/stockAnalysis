def insertModelList(ms, stream):
    for m in ms:
        stream.insert(m).queue()
