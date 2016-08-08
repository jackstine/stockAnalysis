import pandas
from collections import OrderedDict
import Analysis.google.GoogleAPI as gAPI
from circumpunct.API import getStockOpinionWebPage
from Analysis.spreadsheets.Spreadsheets import hyperlink

filepath = "C:\\Users\\bh5kb\\Desktop\\pricings.csv"
def func(row, column, previous_column, new_column, pricings):
    value = row[column]
    rowNumber = row.name
    value -= int(row[previous_column])
    pricings.loc[rowNumber, new_column] = value


def isIncreasing(row, column, prevous_columns, new_column, pricings):
    value = row[column]
    rowNumber = row.name
    finalValue = True
    for i in prevous_columns:
        v = row[i]
        if (v > value or v < 0):
            finalValue = False
    pricings.loc[rowNumber, new_column] = finalValue

def getLongsAndShorts(pricings):
    cantHaveIn = ["id", "Web", "Has_Splits", "max_return", "max_loss", "Unnamed: 0"]
    percentages = []
    for i in pricings:
        if ("annulalized" not in i) and (i not in cantHaveIn):
            percentages.append(i)
    longs = list()
    shorts = list()
    for i in percentages:
        if "long" in i and "year" in i:
            longs.append(i)
        elif "short" in i and "year" in i:
            shorts.append(i)
        else:
            pass
    return longs, shorts


def getFileWorkstation():
    filepath = "C:\\Users\\bh5kb\\Desktop\\pricings.csv"
    pricings = pandas.read_csv(filepath)
    return pricings


def workstation():
    filepath = "C:\\Users\\bh5kb\\Desktop\\pricings.csv"
    savePath = "C:\\Users\\bh5kb\\Desktop\\pricings_alone.csv"
    pricings = pandas.read_csv(filepath)
    originalColumns = pricings.columns
    longs,shorts = getLongsAndShorts(pricings)

    for i in longs:
        splits = str(i).split("_")
        year = splits[2]
        if int(year) > 1:
            YearColumn = splits[0] + "_" + splits[1] + "_" + year
            previousColumn = splits[0] + "_" + splits[1] + "_" + str( int(year) - 1)
            newColumn = splits[0]+"_" + "year_alone_" + str(year)
            pricings[newColumn] = 0
            pricings.apply(func, axis=1, args=(YearColumn, previousColumn, newColumn, pricings))
    print pricings
    pricings.to_csv(savePath)

def addWebPage(row, value, pricings):
    symbol = row["Web"]
    pricings.loc[row.name, "CIR_WEB"] = hyperlink(getStockOpinionWebPage(row["id"]), symbol)
    pricings.loc[row.name, "Web"] = hyperlink(gAPI.google_financial_website(symbol), symbol)

def increasesYearOverYear():
    pricings =  getFileWorkstation()
    savePath = "C:\\Users\\bh5kb\\Desktop\\pricings_increasing.csv"
    longs, shorts = getLongsAndShorts(pricings)
    org = pricings.columns.tolist()
    pricings["CIR_WEB"] = ""
    pricings.apply(addWebPage, axis=1, args=(True, pricings))
    for i in longs:
        splits = str(i).split("_")
        year = splits[2]
        if int(year) > 1:
            YearColumn = splits[0] + "_" + splits[1] + "_" + year
            previousColumns = []
            for y in range(1,int(year)):
                previousColumns.append(splits[0] + "_" + splits[1] + "_" + str( y))
            newColumn = "year_increasing_" + str(year)
            pricings[newColumn] = False
            pricings.apply(isIncreasing, axis=1, args=(YearColumn, previousColumns, newColumn, pricings))
    org.insert(3, "CIR_WEB")
    pricings.to_csv(savePath, columns=org)

increasesYearOverYear()
