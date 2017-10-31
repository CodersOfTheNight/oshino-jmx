import shutil
import os.path
from urllib.request import urlopen 

REPO = 'http://central.maven.org/maven2'
VERSION = 267
URL = ('{repo}/org/jmxtrans/jmxtrans/{version}/jmxtrans-{version}-all.jar'
        .format(version=VERSION,
                repo=REPO))

OUTPUT = 'lib/jmxtrans-all.jar'


def fetch_jar():
    if not os.path.exists('lib/'):
        os.makedirs('lib/')

    if os.path.exists(OUTPUT):
        print('Found JMXTrans. Skipping download')
        return

    print('Downloading JMXTrans package. Be patient')

    req = urlopen(URL)
    with open(OUTPUT, 'wb') as fp:
        shutil.copyfileobj(req, fp)


if __name__ == '__main__':
    fetch_jar()
