import json
from collections import namedtuple

import requests as rq
import datetime

from pprint import pprint


def export_to_csv(path, raw_request_string):
    response = rq.get(raw_request_string)
    pprint(response.text)

    calendar_data = json.loads(response.text)

    g_calendar_header = "Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private"

    csv_data = []

    for event in calendar_data:
        event = namedtuple("Employee", event.keys())(*event.values())

        subject = event.title

        date_start = datetime.datetime.fromtimestamp(event.start)
        start_date = date_start.strftime('%d/%m/%y')
        start_time = date_start.strftime("%H:%M %p")

        date_end = datetime.datetime.fromtimestamp(event.end)
        end_date = date_end.strftime('%d/%m/%y')
        end_time = date_end.strftime("%H:%M %p")

        all_day_event = "False"
        description = event.description
        location = event.sroom
        private = "True"

        csv_data.append(",".join(
            [subject, start_date, start_time, end_date, end_time, all_day_event, description, location,
             private]) + "\n")

    with open(path, "w") as f:
        f.write(g_calendar_header + "\n")
        f.writelines(csv_data)


if __name__ == '__main__':
    export_to_csv("./test.csv", "https://selfservice.campus-dual.de/room/json?userid=[YOUR_USER_ID]&hash=[MAGIC_HASH]&start=[TIME_STAMP_START]&end=[TIME_STAMP_END]")
