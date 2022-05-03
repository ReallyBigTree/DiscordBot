from yahoo_fin import stock_info as stockInfo, stock_info
from yahoo_finance import Share as shareInfo


async def quote(ctx, *, symbol):
    getQuote = stockInfo.get_live_price(symbol)
    await ctx.send(symbol + "\n$" + str(round(getQuote, 2)))


async def gainers(ctx):
    dailyGainer = stockInfo.get_day_gainers()
    await ctx.send(dailyGainer)

async def losers(ctx):
    dailyLoser = stockInfo.get_day_losers()
    await ctx.send(dailyLoser)


