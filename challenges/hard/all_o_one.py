class AllOne(object):
    def __init__(self):
        self.max = ""
        self.min = ""
        self.data = {}

    def inc(self, key):
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

        if self.max:
            if self.data[key] > self.data[self.max]:
                self.max = key
        else:
            self.max = key

    def dec(self, key):
        if self.data[key]:
            if self.data[key] == 1:
                del self.data[key]
            else:
                self.data[key] -= 1
        else:
            self.data[key] = 1

        if self.min:
            if self.data[key] < self.data[self.min]:
                self.min = key
        else:
            self.min = key

    def getMaxKey(self):
        if self.data:
            return self.max
        else:
            return ""


    def getMinKey(self):
        if self.data:
            return self.min
        else:
            return ""



folder = AllOne()
folder.inc("sophie")
folder.inc("alondra")
folder.inc("alondra")
folder.inc("sophie")
folder.inc("sophie")
folder.inc("alondra")
folder.inc("Jenny")
folder.inc("sophie")
folder.inc("sophie")
folder.inc("sophie")
folder.inc("Jenny")
folder.inc("alondra")
folder.inc("alondra")
folder.inc("Jenny")
folder.inc("alondra")
folder.inc("alondra")
folder.inc("sophie")
folder.inc("sophie")
folder.inc("sophie")
folder.inc("Jenny")
folder.inc("May")

print folder.getMaxKey()
print folder.getMinKey()
