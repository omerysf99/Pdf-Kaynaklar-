import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot token'ınızı buraya girin
BOT_TOKEN = "BOT_TOKEN_BURAYA_GIRIN"

# Log ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kullanıcı /start yazdığında çalışacak fonksiyon"""
    await update.message.reply_text("selam mk")

def main():
    """Botu başlat"""
    # Bot uygulamasını oluştur
    application = Application.builder().token(8202149683:AAH06aJ3yY_L8_mcbnziGOKP81e_BI381sA).build()

    # Komut handler'larını ekle
    application.add_handler(CommandHandler("start", start))

    # Botu başlat
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
