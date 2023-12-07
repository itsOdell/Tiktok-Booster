import re
import shutil

def convert_time_to_seconds(text):
    # Extract minutes and seconds using regular expressions
    minutes_regex = r'(\d+)\sminute'
    seconds_regex = r'(\d+)\ssecond'

    minutes = 0
    seconds = 0

    minute_matches = re.findall(minutes_regex, text)
    second_matches = re.findall(seconds_regex, text)

    if minute_matches:
        # Extract minutes and convert to seconds
        minutes = int(minute_matches[0]) * 60

    if second_matches:
        # Extract seconds
        seconds = int(second_matches[0])

    # Calculate total time in seconds
    total_time_in_seconds = minutes + seconds
    return total_time_in_seconds


def print_center(str: str) -> None:
    print(str.center(shutil.get_terminal_size().columns))