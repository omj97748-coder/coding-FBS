# convert the time entered in hh ,min and sec into second.
hours = int(input('enter hours:-'))
minute=int(input('enter minutes:-'))
seconds=int(input('enter seconds:-'))

total_seconds = hours * 3600 + minute * 60 + seconds

print(f"Total time in seconds: {total_seconds}")