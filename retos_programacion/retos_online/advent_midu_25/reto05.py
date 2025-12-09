from datetime import datetime
from math import floor

def time_until_take_off(from_time: str, take_off_time: str) -> int:
  np_format = "%Y*%m*%d@%H|%M|%S NP"
  from_tf = datetime.strptime(from_time, np_format)
  take_off_tf = datetime.strptime(take_off_time, np_format)
  delta = floor((take_off_tf - from_tf).total_seconds())
  return delta
