import urllib.request
import json


def read(url):
    with urllib.request.urlopen(url) as entrada:
        data = json.loads(entrada.read().decode())
        print(data.get('manufacturer') + ': ' +
              '(' + data.get('model') + ': ' + data.get('version') + ')')


if __name__ == '__main__':

    def sony():
        read('http://tv.globoplay.com.br/native/Sony/Unicorn-2019/' +
             'apps/globoplay/versiondata.json')

    def iora():
        read('http://tv.globoplay.com.br/native/Panasonic/Iora-2019/' +
             'apps/globoplay/versiondata.json')

    def iris():
        read('http://tv.globoplay.com.br/native/Panasonic/Iris-2019/' +
             'apps/globoplay/versiondata.json')

    def tcl():
        read('http://tv.globoplay.com.br/native/TCL/S4900/' +
             'apps/globoplay/versiondata.json')

iora()
iris()
tcl()
sony()
