__author__ = 'seung-wongim'


def ekisu_duration(section_string):
    print(section_string)
    duration = 0
    sections = section_string.split(", ")
    for i in sections:
        section_time = i.split(":")
        start_time = float(section_time[0])
        end_time = float(section_time[1])
        duration += end_time - start_time
    return int(duration)