
from apscheduler.schedulers.background import BackgroundScheduler
import time
def scheduled_etl():
    etl_process()

# Set up scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_etl, 'interval', minutes=60)  # Schedule to run every 60 minutes
scheduler.start()

# Keep the script running to allow scheduled tasks to execute
try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    