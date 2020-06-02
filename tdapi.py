import requests

apikey = "" # api key goes here

# time is in epoch for inputs and outputs
# inputs stated, either periodType/period stated or endDate/startDate inputed, not both
# boolean is a boolean
# ex: example = priceHistory("GOOG", client_id, "day", "2", "minute", "1", endDate = None, startDate = None, boolean = "true")
# returns price history of specified period in format: "{'open': '', 'high': '', 'low': '', 'close': '', 'volume': '', 'datetime': ''}"
def priceHistory(ticker, apikey, periodType, period, frequencyType, frequency, endDate, startDate, boolean):
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker) # endpoint as raw text

    query = {
        "apikey": apikey, 
        "periodType": periodType, # periodType in: "day", "month", "year", "ytd"; default is "day"
        "period": period, # period in: #; default is "10" for days, "1" for the rest
        "frequencyType": frequencyType, # frequencyType in: "minute", "daily", "weekly", "monthly"; frequencyType < periodType
        "frequency": frequency, # frequency in: #; default is "1"
        "endDate": endDate, # endDate in: epoch time; endDate should only be provided if period and periodType is not provided 
        "startDate": startDate, # startDate in: epoch time; startDate should only be provided if period and periodType is not provided 
        "needExtendedHoursData": boolean # boolean in: "true", "false"
        }

    response = requests.get(url = endpoint, params = query) # request
    pH = response.json()
    return pH

# time is in epoch for output
# inputs are the ticker and apikey
# ex: example = quote("AAPL", apikey)
# returns a real-time and *DELAYED* quote at that time
# quote has info depending on whether symbol is mutual fund, future, index, options, forex, ETF, or equity
def quote(ticker, apikey):
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/quotes".format(ticker) # endpoint as raw text

    query = {
        "apikey": apikey
        }

    response = requests.get(url = endpoint, params = query) # request
    q = response.json()
    return q

# inputs depend on placeType, refer to documentation or inputs to query below for reference
# ex: example = quote(apikey, "orderType": "MARKET", "session": "NORMAL", "duration": "DAY", "orderStrategyType": "SINGLE", "orderLegCollection": [{"instruction": "Buy", "quantity": 15, "instrument": {"symbol": "XYZ", "assetType": "EQUITY"} } ])
# in this example, this would "Buy 15 shares of XYZ at the Market good for the Day"
# returns: not sure

# I HAVE NOT TESTED THIS SINCE I DO NOT WANT TO PLACE AN ORDER : )
def placeOrder(accountId, apikey, complexOrderStrategyType, orderType, session, price, duration, orderStrategyType, orderLegCollection, placeType):
    endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(accountId) # endpoint as raw text
    
    if placeType == "stock":
        query = {
            "apikey": apikey,
            "orderType": orderType, # 'MARKET' or 'LIMIT' or 'STOP' or 'STOP_LIMIT' or 'TRAILING_STOP' or 'MARKET_ON_CLOSE' or 'EXERCISE' or 'TRAILING_STOP_LIMIT' or 'NET_DEBIT' or 'NET_CREDIT' or 'NET_ZERO'
            "session": session, # 'NORMAL' or 'AM' or 'PM' or 'SEAMLESS'
            "price": price, # a number
            "duration": duration, # 'DAY' or 'GOOD_TILL_CANCEL' or 'FILL_OR_KILL'
            "orderStrategyType": orderStrategyType, # 'SINGLE' or 'OCO' or 'TRIGGER'
            "orderLegCollection": orderLegCollection # in form of: [{"instruction": instruction, "quantity": quantity, "instrument": {"symbol": ticker, "assetType": assetType} }]
        }

        response = requests.post(url = endpoint, params = query) # request
        pO = response.json()
        return pO
    elif placeType == "option":
        query = {
            "apikey": apikey,
            "complexOrderStrategyType": complexOrderStrategyType, # 'NONE' or 'COVERED' or 'VERTICAL' or 'BACK_RATIO' or 'CALENDAR' or 'DIAGONAL' or 'STRADDLE' or 'STRANGLE' or 'COLLAR_SYNTHETIC' or 'BUTTERFLY' or 'CONDOR' or 'IRON_CONDOR' or 'VERTICAL_ROLL' or 'COLLAR_WITH_STOCK' or 'DOUBLE_DIAGONAL' or 'UNBALANCED_BUTTERFLY' or 'UNBALANCED_CONDOR' or 'UNBALANCED_IRON_CONDOR' or 'UNBALANCED_VERTICAL_ROLL' or 'CUSTOM'
            "orderType": orderType, # 'MARKET' or 'LIMIT' or 'STOP' or 'STOP_LIMIT' or 'TRAILING_STOP' or 'MARKET_ON_CLOSE' or 'EXERCISE' or 'TRAILING_STOP_LIMIT' or 'NET_DEBIT' or 'NET_CREDIT' or 'NET_ZERO'
            "session": session, # 'NORMAL' or 'AM' or 'PM' or 'SEAMLESS'
            "price": price, # a number
            "duration": duration, # 'DAY' or 'GOOD_TILL_CANCEL' or 'FILL_OR_KILL' 
            "orderStrategyType": orderStrategyType, # 'SINGLE' or 'OCO' or 'TRIGGER'
            "orderLegCollection": orderLegCollection # in form of: [{"instruction": instruction, "quantity": quantity, "instrument": {"symbol": ticker, "assetType": assetType} }]
        }

        response = requests.post(url = endpoint, params = query) # request
        pO = response.json()
        return pO
    elif placeType == "spread":
        query = {
            "apikey": apikey,
            "orderType": orderType, # 'MARKET' or 'LIMIT' or 'STOP' or 'STOP_LIMIT' or 'TRAILING_STOP' or 'MARKET_ON_CLOSE' or 'EXERCISE' or 'TRAILING_STOP_LIMIT' or 'NET_DEBIT' or 'NET_CREDIT' or 'NET_ZERO'
            "session": session, # 'NORMAL' or 'AM' or 'PM' or 'SEAMLESS'
            "price": price, # a number
            "duration": duration, # 'DAY' or 'GOOD_TILL_CANCEL' or 'FILL_OR_KILL' 
            "orderStrategyType": orderStrategyType, # 'SINGLE' or 'OCO' or 'TRIGGER'
            "orderLegCollection": orderLegCollection # in form of: [{"instruction": instruction, "quantity": quantity, "instrument": {"symbol": ticker, "assetType": assetType} {"instruction": instruction, "quantity": quantity, "instrument": {"symbol": ticker, "assetType": assetType} {...} }]
            # orderLegCollection depends on how many legs in option
        }

        response = requests.post(url = endpoint, params = query) # request
        pO = response.json()
        return pO    
    else:
        pO = "placeType incorrectly specified, choices are: 'stock', 'option', 'spread'"
        return pO

# inputs accountId and the transactionId
# I THINK THIS HAPPENS vvv, i do not have an open transaction currently
# returns transaction details
def getTransaction(accountId, transactionId):
    endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/transactions/{}".format(accountId, transactionId) # endpoint as raw text

    response = requests.get(url = endpoint) # request
    gT = response.json()
    return gT

# inputs accountId and the orderId
# I THINK THIS HAPPENS vvv, i do not have an open order currently
# if this is executed after the order is filled, returns the order details if the order is placed
def getOrder(accountId, orderId):
    endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders/{}".format(accountId, orderId) # endpoint as raw text

    response = requests.get(url = endpoint) # request
    gO = response.json()
    return gO

# inputs accountId and the orderId
# I THINK THIS HAPPENS vvv, i do not have an open order currently
# if this is executed before the order is filled, cancels the open order
def cancelOrder(accountId, orderId):
    endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders/{}".format(accountId, orderId) # endpoint as raw text

    response = requests.delete(url = endpoint) # request
    cO = response.json()
    return cO

# inputs specified, index MUST be specified as symbol (can be $COMPX, $DJI, $SPX.X)
# returns top 10 movers with details
def getMovers(apikey, index, direction, change):
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/movers".format(index) # endpoint as raw text

    query = {
        "apikey": apikey,
        "direction": direction, # "up" or "down"
        "change": change, # "value" or "percent"
    }

    response = requests.get(url = endpoint, params = query)
    gM = response.json()
    return gM