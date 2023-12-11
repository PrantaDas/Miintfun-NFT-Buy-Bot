import os
import datetime
import asyncio

async def scheduler(call_back):
    days_to_run = list(map(int, os.environ.get('DAYS_TO_RUN','').split(',')))
    start_hour = int(os.environ.get('START_HOUR','0'),10)
    start_minute = int(os.environ.get('START_MINUTE','0'),10)

    while True:
        current_datetime = datetime.datetime.now()
        day_of_week = current_datetime.weekday()
        current_hour = current_datetime.hour
        current_minute = current_datetime.minute

        if day_of_week in days_to_run and current_hour == start_hour and current_minute == start_minute:
            await call_back()
        
        await asyncio.sleep(60)