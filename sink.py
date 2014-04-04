from datetime import datetime
from smtpd import SMTPServer
import asyncore

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'), self.no)
        with open(filename, 'w') as fh:
            fh.write(data)
        print('%s saved.' % filename)
        self.no += 1

def main():
    foo = EmlServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    print("Running!")
    main()
