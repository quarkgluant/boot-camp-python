import sys, time

def progressbar(list, prefix="", size=60, file=sys.stdout):
    count = len(list)
    start = time.time()
    def show(j):
        x = int(size * j / count)
        percent = j / count * 100
        total_time = (time.time() - start) * count  if j == 0 else (time.time() - start) * (count  / j)
        eta = abs(total_time - (time.time() - start))
        file.write("ETA: %02.2fs [%02.2f%s] %s[%s%s%s] %i/%i | elapsed time %02.2fs\r" % (eta, percent, "%", prefix, "="*x, ">", " "*(size-x), j, count, (time.time() - start)))
        file.flush()
    show(0)
    for index, item in enumerate(list):
        yield item
        show(index + 1)
    file.write("\n")
    file.flush()