from random import *


class Adviser:

    def stop(self, count):
        if count > 7:
            r = random()
            if r < 0.5:
                return True
        if count > 5:
            r = random()
            if r < 0.35:
                return True
        return False
