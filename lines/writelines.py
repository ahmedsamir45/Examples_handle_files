lines = open("lines.txt","w")
list_lines = ['this is a new first line',"\nthis is a new second line","\nthis is a new third line"]

lines.writelines(list_lines)
lines.close()