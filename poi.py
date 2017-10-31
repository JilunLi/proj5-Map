class POI() :
    def __init__(self, poifile):
        self.poilist = []
        ls = open(poifile, 'r')
        for line in ls:
            if line.strip().startswith("#"):
                continue
            line = line.strip().split()
            if len(line) < 3:
                continue
            record =(line[0], line[1], line[2:])
            self.poilist.append((line[0], line[1], line[2:]))

    def getData(self):
        return self.poilist

