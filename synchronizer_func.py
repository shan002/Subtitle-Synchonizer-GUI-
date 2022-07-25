import re
import os


def add_time(Time, milliseconds):

    hour, minute, second, milisecond = map(int, re.split(':|,', Time))
    totalMs = milisecond + second * 1000 + minute * 60 * 1000 + hour * 60 * 60 * 1000 + milliseconds
    if totalMs < 0:
        totalMs = 0
    hour = totalMs // (60 * 60 * 1000)
    totalMs %= (60 * 60 * 1000)
    minute = totalMs // (60 * 1000)
    totalMs %= (60 * 1000)
    second = totalMs // 1000
    milisecond %= 1000

    newTime = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2) + ',' + str(milisecond).zfill(3)
    return newTime


def synchronize(file_name, new_file_name, delay_ms):
	with open(file_name, 'r', encoding="utf-8") as file, open(new_file_name, 'w', encoding="utf-8") as new_file:
	    for line in file:
	        if '-->' in line:
	            line = line.strip('\n')
	            begin_time, end_time = line.split('-->')
	            begin_time = add_time(begin_time.strip(), delay_ms)
	            end_time = add_time(end_time.strip(), delay_ms)
	            line = begin_time + ' --> ' + end_time + '\n'

	        new_file.write(line)
