class F :
    def __init__(self, name):
        self.name = name
        self.freq = {}  # dictionary

    def show(self) :
        print(self.name)

    def freqCount(self) :
        for chr in self.name :
            if chr not in self.freq :
                self.freq[chr] = 0
            self.freq[chr] += 1

        return self.freq
    

obj1 = F("sourav")
obj1.show()
count1 = obj1.freqCount()


obj2 = F("Poddar")
obj2.show()
count2 = obj2.freqCount()

for keys in count1.keys() :
    if keys not in count2.keys() :
        print(keys)