from .FinancialModel import FinancialModel

def makeGoogleAnnual(rows, fields):
    return FinancialModel(rows[fields["symbol"]], rows[fields["date"]], rows[fields["cashequivalents"]], rows[fields["shortterminvestments"]], 
        rows[fields["totalreceivablesnet"]], rows[fields["totalinventory"]], rows[fields["totalcurrentassets"]],
        rows[fields["propertyplantequipmenttotalgross"]], rows[fields["longterminvestments"]],
        rows[fields["totalassets"]], rows[fields["accountspayable"]], rows[fields["totalcurrentliabilities"]],
        rows[fields["totallongtermdebt"]], rows[fields["totaldebt"]], rows[fields["minorityinterest"]],
        rows[fields["totalliabilities"]], rows[fields["preferredstocknonredeemablenet"]], rows[fields["additionalpaidincapital"]],
        rows[fields["commonstocktotal"]], rows[fields["treasurystockcommon"]], rows[fields["otherequitytotal"]],
        rows[fields["totalequity"]], rows[fields["depreciationdepletion"]], rows[fields["amortization"]],
        rows[fields["deferredtaxes"]], rows[fields["cashfromoperatingactivities"]], rows[fields["capitalexpenditures"]],
        rows[fields["cashfrominvestingactivities"]], rows[fields["cashfromfinancingactivities"]], rows[fields["totalcashdividendspaid"]],
        rows[fields["issuanceretirementofstocknet"]], rows[fields["issuanceretirementofdebtnet"]], rows[fields["cashfromfinancingactivities"]],
        rows[fields["cashinterestpaidsupplemental"]], rows[fields["cashtaxespaidsupplemental"]], rows[fields["revenue"]],
        rows[fields["totalrevenue"]], rows[fields["costofrevenuetotal"]], rows[fields["grossprofit"]],
        rows[fields["sellinggeneraladminexpensestotal"]], rows[fields["researchdevelopment"]], rows[fields["depreciationamortization"]],
        rows[fields["interestexpenseincomenetoperating"]], rows[fields["totaloperatingexpense"]], rows[fields["operatingincome"]],
        rows[fields["gainlossonsaleofassets"]], rows[fields["incomebeforetax"]], 
        rows[fields["netincome"]], rows[fields["preferreddividends"]], rows)
