from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import requests as res      
import json                  
import pandas as pd

# 替换为你的 Bot Token
TOKEN = '7913141683:AAHuJXDJ_uyJQKAGnsP0neeVgei1SOMLoNI'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('請輸入要查詢的股價代碼')

async def echo(update: Update, context: CallbackContext) -> None:
    y = update.message.text.lower()
    url='https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL'
    re=res.get(url)
    data=json.loads(re.text)
    df=pd.DataFrame(data)
    a = df[df['Code'] == y]['OpeningPrice']
    b = df[df['Code'] == y]['HighestPrice']
    c = df[df['Code'] == y]['LowestPrice']
    d = df[df['Code'] == y]['ClosingPrice']
    e = df[df['Code'] == y]['Change']
    f = df[df['Code'] == y]['Transaction']
    x = df[df['Code'] == y]['Name']

    if x.empty:
        response = (f"股票代號 {y} 不存在或沒有資料")
    else:
        response = (f"{y} {x.values[0]}\n開盤價為: {a.values[0]}\n最高價為: {b.values[0]}\n最低價為: {c.values[0]}\n收盤價為: {d.values[0]}\n漲跌差為: {e.values[0]}\n成交量為: {f.values[0]}")
   
    # 打印收到的消息和回复到控制台
    print(f"Received message: {update.message.text}")
    print(f"Response: {response}")

    # 回复用户
    await update.message.reply_text(response)

def main():
    # 创建 Application 对象并传入 Bot Token
    app = ApplicationBuilder().token(TOKEN).build()

    # 注册 /start 命令的处理程序
    app.add_handler(CommandHandler('start', start))

    # 注册文本消息的处理程序
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 启动 Bot
    app.run_polling()

if __name__ == '__main__':
    main()
