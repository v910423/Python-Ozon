import logging
from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
  update.message.reply_text('Hi! Use /set <seconds> for setting timer')

def alarm(context):
  job = context.job
  context.bot.send_message(job.context, text='Beep')

def set_timer(update, context):
  chat_id = update.message.chat_id
  try:
    due = int(context.args[0])
    if due<0:
      update.message.reply_text('time cannot be less than zero')
      return
    if 'job' in context.chat_data:
      old_job = context.chat_data['job']
      old_job.schedule_removal()
    new_job = context.job_queue.run_once(alarm, due, context=chat_id)
    context.chat_data['job'] = new_job
    update.message.reply_text('timer was installed.')
  except(IndexError, ValueError):
    update.message.reply_text("Use /set <seconds>")

def unset(update, context):
  if "job" not in context.chat_data:
    update.message.reply_text("You have no active timer.")
    return

  job = context.chat_data['job']
  job.schedule_removal()
  del context.chat_data['job']

  update.message.reply_text('Timer is deleted')

def error(update, context):
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
  updater = Updater('1279142106:AAFoVeNd_YWVHbNxwxyUtAaEeWVwiyYIkDg', use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", start))
  dp.add_handler(CommandHandler("set", set_timer, pass_args=True,
                                pass_job_queue=True, pass_chat_data=True))
  dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
  dp.add_error_handler(error)
  updater.start_polling()
  updater.idle()

main()

