from random import *


class Adviser:

    def stop(self, count):
        if count > 15:
            r = random()
            if r < 0.5:
                return True
        if count > 10:
            r = random()
            if r < 0.35:
                return True
        return False
