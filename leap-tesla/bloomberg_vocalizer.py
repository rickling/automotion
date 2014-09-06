from bloomberg_wrapper import BloombergWrapper
from vocalizer import Vocalizer

class BloombergVocalizer(object):
    def __init__(self):
        self.wrapper = BloombergWrapper()
        self.vocalizer = Vocalizer()

    def vocalize(self, securities):
        prices = self.wrapper.request(securities)

        statement = ""
        i = 0
        for security in securities:
            statement += "The current price of %s is %s dollars. " % (security, prices[i])
            i += 1

        self.vocalizer.vocalize(statement)

if __name__ == '__main__':
    main()

def main():
    bbg_vocalizer = BloombergVocalizer()
    print bbg_vocalizer.vocalize(["INDU Index", "AAPL Equity", "GOOG Equity"])
