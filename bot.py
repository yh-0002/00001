from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# 替换为你的 Bot Token
TOKEN = 'YOUR_BOT_TOKEN'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Send me a message and I will reply with a specific response!')

async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if 'hello' in user_message:
        response = 'Hi there! How can I help you today?'
    elif 'bye' in user_message:
        response = 'Goodbye! Have a great day!'
    else:
        response = 'I received your message!'
    
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
