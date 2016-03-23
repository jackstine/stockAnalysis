from sql.Con import con
from splits import SplitAPI
from pricing import PriceModel as pm
from splits import SplitsModel as spm
import time

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
    currentRatioChangeDate = datesRatio.iloc[ratioIndex][spm.DATE]
    currentRatio = 1.0
    priceRatios = []
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
    #creates two new columns in the prices data frame
    prices[pm.RATIO] = priceRatios
    prices[pm.ADJUSTED_PRICE] = prices[pm.PRICE] * prices[pm.RATIO]
    return prices

def get_return_from_date(prices, beginDate, endDate):
    beginPrice = prices.at[beginDate, pm.ADJUSTED_PRICE]
    endPrice = prices.at[endDate, pm.ADJUSTED_PRICE]
    return (beginPrice / endPrice) - 1.0

def get_max_date(prices):
    return prices.index.max()

def return_from_days(prices, daysFrom):
    today = get_max_date(prices)
    toDate = prices.index[daysFrom]
    return get_return_from_date(prices,today,toDate)

def totalReturn(prices):
    dates = prices.index
    minDate = dates.min()
    maxDate = dates.max()
    return get_return_from_date(prices, maxDate, minDate)

def print_ratios(prices):
    for key, value in pm.TERMS.iteritems():
        print key + ": " + str(return_from_days(prices,value))


# Returns the max return from the number of trading days given to date,
# where daysFrom is the number of trading days
def get_max_return(prices, daysFrom):
    pricesFromBeginDate = _get_prices_begin_date(prices,daysFrom)
    beginDay = pricesFromBeginDate.index[0]
    low = pricesFromBeginDate.at[beginDay]
    high = pricesFromBeginDate.at[beginDay]
    highestGain = 0
    for p in pricesFromBeginDate:
        if (low > p):
            low = p
            high = 0
        high = max(high,p)
        currentGain = high / low
        highestGain = max(currentGain,highestGain)
    return highestGain - 1  # subtract 1 for the Gain on investment


#returns the max loss that could have happened given the number of trading
# days till date,  where daysFrom is the number of trading days.
def get_max_loss(prices, daysFrom):
    pricesFromBeginDate = _get_prices_begin_date(prices, daysFrom)
    beginDay = pricesFromBeginDate.index[0]
    low = pricesFromBeginDate.at[beginDay]
    high = pricesFromBeginDate.at[beginDay]
    highestLoss = 0
    for p in pricesFromBeginDate:
        if (high < p):
            high = p
            low = p
        low = min(low,p)
        currentLoss = (low / high) - 1  # subtract 1 for the Loss on investment
        highestLoss = min(currentLoss,highestLoss)
    return highestLoss


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
    numberOfRows = prices.shape[0]  # 0 indexes the rows of the shape of the df
    beginRow = numberOfRows - daysFrom
    endRow = numberOfRows
    return prices.sort_index(ascending=True)[beginRow:endRow][pm.ADJUSTED_PRICE]