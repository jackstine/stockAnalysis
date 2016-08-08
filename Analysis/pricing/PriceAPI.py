from Analysis.sql.Con import con
from Analysis.splits import SplitAPI
from Analysis.pricing import PriceModel as pm
from Analysis.splits import SplitsModel as spm
import time, math

def get_price_of_id(id):
    return con.read_query("SELECT * FROM NasdaqSummaryQuote WHERE id =" + str(id),"date")

# Adds the following rows: adjustPrice, and ratio
# where ratio is the ratio used on price to get the adjustPrice
# adjustPrice is the price of the security at the date, price * ratio
def get_split_adjusted_price(id):
    datesRatio = SplitAPI.get_split_from_id(id).loc[:, [spm.DATE, spm.RATIO]].sort_values(by = spm.DATE, ascending = False)
    prices = get_price_of_id(id).sort_index(ascending = False)
    priceDates = prices.index
    minRatioDate = datesRatio[spm.DATE].min()
    ratioIndex = 0
    priceRatios = []
    if (datesRatio.shape[0] != 0):
        currentRatioChangeDate = datesRatio.iloc[ratioIndex][spm.DATE]
        currentRatio = 1.0
        for i,date in enumerate(priceDates):
            # change the ratio when the date is equal to the currentRatioChangeDate
            # if the date is also larger than the minRatioDate, then continue
            if (date <= currentRatioChangeDate and date >= minRatioDate):
                ratio = datesRatio.iloc[ratioIndex][spm.RATIO]
                currentRatio = currentRatio / ratio
                ratioIndex += 1
                if (currentRatioChangeDate != minRatioDate):
                    currentRatioChangeDate = datesRatio.iloc[ratioIndex][spm.DATE]
            priceRatios.append(currentRatio)
    else:
        priceRatios = [1 for i in range(0,prices.shape[0])]
    #creates two new columns in the prices data frame
    prices[pm.RATIO] = priceRatios
    prices[pm.ADJUSTED_PRICE] = prices[pm.PRICE] * prices[pm.RATIO]
    return prices

def get_short_return_from_date(prices, beginDate, endDate):
    """
    returns the short return on investment given a short on the beginDate
    and a buy on the endDate
    :param prices:
    :param beginDate:
    :param endDate:
    :return: the return PriceStruture containing the return or loss of the short investment
    """
    ps = pm.PriceStructure()
    ps.setEndDate(endDate)
    ps.setStartDate(beginDate)
    beginPrice = prices.at[beginDate, pm.ADJUSTED_PRICE]
    endPrice = prices.at[endDate, pm.ADJUSTED_PRICE]
    ps.setStartPrice(beginPrice)
    ps.setEndPrice(endPrice)
    ps.setReturn((beginPrice - endPrice) / (beginPrice * 1.0))
    return ps

def get_long_return_from_date(prices, beginDate, endDate):
    """
    :param prices: A price dataframe that interfaces the Prices
    :param beginDate: The date to Begin a Long investment
    :param endDate: The date to End a Long investment
    :return: the return of the long investment
    """
    ps = pm.PriceStructure()
    ps.setEndDate(endDate)
    ps.setStartPrice(beginDate)
    beginPrice = prices.at[beginDate, pm.ADJUSTED_PRICE]
    endPrice = prices.at[endDate, pm.ADJUSTED_PRICE]
    ps.setStartPrice(beginPrice)
    ps.setEndPrice(endPrice)
    ps.returnValue = (beginPrice / endPrice) - 1.0
    return ps

def get_max_date(prices):
    return prices.index.max()

def long_return_from_days(prices, daysFrom):
    """
    Assumes that the dataframe is sorted
    given a prices interface, returns the return on long investment from the
    begining (the most latest date) to the daysFrom'th' index of the dataframe prices
    :param prices: a datframe that contains the Price interface
    :param daysFrom: the Number of days from the begining, the begining is the start of the prices data frame
    :return: the return or loss of the long investment
    """
    today = get_max_date(prices)
    if (prices.shape[0] > daysFrom):
        toDate = prices.index[daysFrom]
        return get_long_return_from_date(prices, today, toDate)
    else:
        return pm.PriceStructure()

def short_return_from_days(prices, daysFrom):
    """
    Assumes that the dataframe is sorted
    given a prices interface, returns the return on short investment from the
    begining (the most latest date) to the daysFrom'th' index of the dataframe prices
    :param prices: a datframe that contains the Price interface
    :param prices: a datframe that contains the Price interface
    :param daysFrom: the Number of days from the begining, the begining is the start of the prices data frame
    :return: new PS if there is a existing date, else it will return the short return of the investment in PS
    """
    today = get_max_date(prices)
    if (prices.shape[0] > daysFrom):
        toDate = prices.index[daysFrom]
        return get_short_return_from_date(prices, today, toDate)
    else:
        return pm.PriceStructure()

def totalReturn(prices):
    dates = prices.index
    minDate = dates.min()
    maxDate = dates.max()
    return get_long_return_from_date(prices, maxDate, minDate)

def get_full_dict(id):
    """
    returns a dictionary of all the long and short investments, plus the max return and loss
    on a investment given the prices. The days between a investment are in TERMS varibale
    of the price interface
    :param id: id of the stock
    :return: d: dictionary of ratios -> this is the
    """
    prices = get_split_adjusted_price(id)
    d = dict_of_ratios(prices)
    d[pm.MAX_RETURN], days_return = get_max_long_return_all(prices)
    d[pm.MAX_LOSS], days_loss = get_max_loss_all(prices)
    days_return = max(days_return, 1)
    days_loss = max(days_loss, 1)
    d[pm.MAX_RETURN].setAnnualizedReturn(get_annulized_return(d[pm.MAX_RETURN].returnValue, days_return / ( 1.0 * pm.ONE_YEAR)))
    d[pm.MAX_LOSS].setAnnualizedReturn(get_annulized_return(d[pm.MAX_LOSS].returnValue, days_loss / (pm.ONE_YEAR * 1.0)))
    return unwrap_PriceStructures_to_dict(d)

def unwrap_PriceStructures_to_dict(d):
    newd = dict()
    for key in d.keys():
        ps = d[key]
        returnV = ps.returnValue
        annual = ps.annulized_return
        newd[key] = returnV
        if (ps.type == pm.SHORT):
            newd[pm.ANNULALIZED_SHORT + "_" + ps.term] = annual
        else:
            newd[pm.ANNULALIZED_LONG + "_" + ps.term] = annual
    return newd


def dict_of_ratios(prices):
    """
    ASSUMES that the prices is sorted
    using the varibale TERMS in the price interface, returns a dictionary of all the long and short
    position returns given a holding of that long
    :param prices: A dataFrame of the prices interface
    :return:a dictionary of all the shorts and long investments
    """
    d = dict()
    add_short_investments(prices,d)
    add_long_investments(prices,d)
    return d

def add_short_investments(prices,d):
    """
    Adds all the short investment oppurtunities from the TERMS varibale in the prices interface
    :param prices: A data frame of the prices interface
    :param d: a dictionary
    """
    for key,value in pm.TERMS.iteritems():
        shortReturn = short_return_from_days(prices, value[pm.TERM])
        d[pm.SHORT + "_" + key] = shortReturn
        shortReturn.returnValue = abs(float(shortReturn.returnValue))
        shortReturn.annulized_return = get_annulized_return(shortReturn.returnValue, value[pm.YEARS])
        shortReturn.setTerm(key)
        shortReturn.setType(pm.SHORT)
        # d[pm.ANNULALIZED_SHORT + "_" + key] =

def add_long_investments(prices,d):
    """
    Adds all the long investment oppurtunities from the TERMS variable in the prices interface
    :param prices: A data frame of the prices interface
    :param d: a dictionary
    """
    for key, value in pm.TERMS.iteritems():
        longReturnOnInvestment = long_return_from_days(prices, value[pm.TERM])
        d[pm.LONG + "_" + key] = longReturnOnInvestment
        longReturnOnInvestment.annulized_return = get_annulized_return(longReturnOnInvestment.returnValue, value[pm.YEARS])
        longReturnOnInvestment.setTerm(key)
        longReturnOnInvestment.setType(pm.LONG)
        # d[pm.ANNULALIZED_LONG +"_" + key] = get_annulized_return(longReturnOnInvestment, value[pm.YEARS])

def get_annulized_return_days(r, days):
    """
    returns the annulized return given the number of days
    :param r:
    :param days:
    :return: annulied return
    """
    if (days == 0):
        return 0
    else:
        numberOfYears =  math.ceil(days / pm.ONE_YEAR)
        numberOfYears = numberOfYears if numberOfYears > 0.1 else 1
        return get_annulized_return(r, numberOfYears)

def get_annulized_return(r, years):
    return ((1 + float(r)) ** (1/ (years * 1.0)) ) - 1

def get_max_long_return_all(prices):
    """
    returns the max long return on a dataframe given all of the dates
    :param prices: a data frame of the price interface
    :return: the max long return on a investment
    """
    return get_max_long_return(prices, _get_number_of_rows(prices))

def get_max_loss_all(prices):
    """
    return the max loss of the data frame
    :param prices: data frame that interfaces the prices
    :return: the max loss over the data frame
    """
    return get_max_loss(prices, _get_number_of_rows(prices))

# Returns the max return from the number of trading days given to date,
# where daysFrom is the number of trading days
def get_max_long_return(prices, daysFrom):
    """
    returns the max long return.  return the highest return over the period starting at daysFrom
    :param prices: the data Frame of the prices
    :param daysFrom: the number of days from the begining, to start the investment
    :return: return the highest return
    """
    ps = pm.PriceStructure()
    numOfRows = prices.shape[0]
    if (daysFrom > prices.shape[0] or numOfRows == 0):
        return pm.PriceStructure(), 0
    pricesDT = _get_prices_begin_date(prices,daysFrom)
    low = pricesDT.getPricesAt(0)
    high = low
    highestGain = 0
    daysCounted = 0
    beginDate = pricesDT.getDateAt(0)
    for i,p in enumerate(pricesDT.prices):
        if (low > p):
            low = p
            beginDate = pricesDT.getDateAt(0)
            high = 0
        high = max(high,p)
        currentGain = high / low
        if (currentGain > highestGain):
            highestGain = currentGain
            ps.setStartPrice(low)
            ps.setEndPrice(high)
            ps.setStartPrice(beginDate)
            ps.setEndDate(pricesDT.getDateAt(i))
        daysCounted = i if highestGain == currentGain else daysCounted
    ps.setReturn(highestGain - 1)
    return ps, daysCounted  # subtract 1 for the Gain on investment


#returns the max loss that could have happened given the number of trading
# days till date,  where daysFrom is the number of trading days.
def get_max_loss(prices, daysFrom):
    """
    returns the max loss investment from daysFrom to the highest or most recent date
    :param prices: data frame of the prices interface
    :param daysFrom: the numnber of days from the begining of the investment
    :return: max loss
    """
    ps = pm.PriceStructure()
    numOfRows = prices.shape[0]
    if (daysFrom > prices.shape[0] or numOfRows == 0):
        return pm.PriceStructure(), 0
    pricesDT = _get_prices_begin_date(prices, daysFrom)
    low = pricesDT.getPricesAt(0)
    high = low
    highestLoss = 0
    daysCounted = 0
    beginDate = pricesDT.getDateAt(0)
    for i,p in enumerate(pricesDT.prices):
        if (high < p):
            high = p
            beginDate = pricesDT.getDateAt(i)
            low = p
        low = min(low,p)
        currentLoss = (low / high) - 1  # subtract 1 for the Loss on investment
        if (currentLoss < highestLoss):
            highestLoss = currentLoss
            ps.setStartPrice(high)
            ps.setEndPrice(low)
            ps.setStartDate(beginDate)
            ps.setEndDate(pricesDT.getDateAt(i))
        daysCounted = i if highestLoss == currentLoss else daysCounted
    ps.setReturn(highestLoss)
    return ps, daysCounted


# returns the number of gains and losses over a range
def get_number_of_gains_and_losss_margin(prices,daysFrom, margin):
    pricesFromBeginDate = _get_prices_begin_date(prices, daysFrom)
    beginDay = pricesFromBeginDate.index[0]
    low = pricesFromBeginDate[beginDay]
    high = pricesFromBeginDate[beginDay]
    negMargin = margin * -1.0
    posMargin = margin * 1.0
    lossCount = 0
    gainCount = 0
    for p in pricesFromBeginDate:
        high = max(p,high)
        low = min(p,low)
        loss = (low / high) - 1
        gain = (high / low) - 1
        if (loss <= negMargin):
            lossCount += 1
            low = p
            high = p
        elif (gain >= posMargin):
            gainCount += 1
            low = p
            high = p
    return gainCount, lossCount


def _get_prices_begin_date(prices, daysFrom):
    numberOfRows = _get_number_of_rows(prices)
    beginRow = numberOfRows - daysFrom
    endRow = numberOfRows
    sortedPrices = prices.sort_index(ascending=True)[beginRow:endRow]
    pdt = pm.PriceDateTime()
    pdt.setPrices(sortedPrices[pm.ADJUSTED_PRICE])
    return pdt

def _get_number_of_rows(prices):
    return prices.shape[0]  # 0 indexes the rows of the shape of the df