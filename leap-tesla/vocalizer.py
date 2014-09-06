import os

class Vocalizer(object):
    def vocalize(self, statement):
        os.system("say '%s'" % statement)

if __name__ == '__main__':
    vocalizer = Vocalizer()
    vocalizer.vocalize("Hello world.")
