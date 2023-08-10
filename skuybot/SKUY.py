import os
import telegram
from dotenv import load_dotenv
from telegram import Update, Message
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from transformers import pipeline
import tldr

# Load token dari file .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telegram.Bot(token=TOKEN)

# Fungsi untuk menangani perintah /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Halo! Saya adalah bot Telegram.')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hallo , Selamat datang di bot telegram saya.")

# Fungsi untuk menangani perintah /help
def help(update: Update, context: CallbackContext):
    update.message.reply_text('Ada yang bisa saya bantu?')

def motivation(update: Update, context: CallbackContext):
    text_motivation = "Pantang menyerah adalah jalan ninjaku"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_motivation)

def tantangan(update: Update, context: CallbackContext):
    text_tantangan = "Push up 50 kali setiap pagi"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_tantangan)



def ringkas(update: Update, context: CallbackContext):
    try:
        message = update.message.text

        # Inisialisasi model ringkasan dari transformers
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


        # Meringkas teks menggunakan model
        summarized_text = summarizer(message, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
        print(f'Hasil ringkasan teks: {summarized_text}')
        # Kirim ringkasan teks ke pengguna
        update.message.reply_text(f'Ringkasan teks:\n{summarized_text}')

    except Exception as e:
        print(f'Error: {str(e)}')

    
    

#def handle_message(update, context):
  #  message = update.message
  #  chat_id = message.chat_id
   # text = message.text

    # Cek apakah pesan mengandung spam (sesuaikan dengan pola spam yang ingin Anda deteksi)
   # spam_patterns = ["Klik di sini untuk mendapatkan hadiah gratis", "Dapatkan uang cepat dengan cara mudah", "Penawaran terbatas! Diskon 90% hanya hari ini"]
    #is_spam = any(pattern.lower() in text.lower() for pattern in spam_patterns)

    #if is_spam:
        # Hapus pesan spam
     #   bot.delete_message(chat_id=chat_id, message_id=message.message_id)
        
#def echo(update: Update, context: CallbackContext):
    
  #  message = update.message.text
  #  context.bot.send_message(chat_id=update.effective_chat.id, text=message)
   # print(f"Pesan dari user: {message}")        

def main():
    # Buat instance Updater dan gunakan token dari .env
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    # Tambahkan handler untuk perintah /start dan /help
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("motivation", motivation))
    dp.add_handler(CommandHandler("tantangan", tantangan))
    # dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ringkas))
    # Tambahkan handler untuk pesan dari pengguna
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Jalankan bot
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
