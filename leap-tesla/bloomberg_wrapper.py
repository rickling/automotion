import blpapi

class BloombergWrapper(object):
    """ Python Wrapper for the Bloomberg API """
    def __init__(self):
        self.sessionOptions = blpapi.SessionOptions()
        self.sessionOptions.setServerHost("10.8.8.1")
        self.sessionOptions.setServerPort(8194)

    def create_session(self):
        session = blpapi.Session(self.sessionOptions)

        if not session.start():
            raise Exception("Failed to start session on 10.8.8.1:8194.")

        if not session.openService("//blp/refdata"):
            raise Exception("Failed to open //blp/refdata")

        return session

    def request(self, securities):
        session = self.create_session()
        refDataService = session.getService("//blp/refdata")
        request = refDataService.createRequest("ReferenceDataRequest")

        request.append("fields", "LAST_PRICE")
        for security in securities:
            request.append("securities", security)

        session.sendRequest(request)

        prices = []

        try:

            while(True):
                ev = session.nextEvent(500)
                if ev.eventType() == blpapi.Event.RESPONSE:
                    for msg in ev:
                        for securityData in msg.getElement("securityData").values():
                            fieldData = securityData.getElement("fieldData")
                            prices.append(fieldData.getElementAsFloat("LAST_PRICE"))
                    break

        finally:
            session.stop()

        return prices

# Tests
# =====

if __name__ == '__main__':
    bbg_wrapper = BloombergWrapper()
    print bb_wrapper.request(["INDU Index", "AAPL Equity", "GOOG Equity"])
