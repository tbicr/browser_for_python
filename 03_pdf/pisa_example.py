'''
required:
 - pisa python package
 - reportlab 2x python package
 - html5lib python package
 - pil python package
 - pypdf python package
'''
import urllib2
import StringIO

from ho import pisa


links = {
    'bender': 'https://developer.cdn.mozilla.net/media/uploads/demos/v/i/viniciusdacal/9e8803e30a5507dc979275c9be583ab0/pure-css3-bender-fut_1382371135_demo_package/index.html',
    'homer': 'https://developer.cdn.mozilla.net/media/uploads/demos/b/e/bernarddeluna/98993ebf9a834ed591bc860f9b08df5b/pure-css3-homer_1342534433_demo_package/index.html',
    'kyle': 'https://developer.cdn.mozilla.net/media/uploads/demos/F/r/Francis/1eb04da6a24a03b1c46b08529dd7d316/pure-css3-kyle-brofl_1387324513_demo_package/index.html',
    'tw': 'http://www.subcide.com/experiments/fail-whale/',
    'py': 'https://www.python.org/',
    'py-ru': 'http://python.su/',
    'py-ch': 'http://python.cn/',
}


def create_pdf(input, output):
    html  = urllib2.urlopen(input).read()
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
    if not pdf.err:
        with open(output, 'wb') as file:
            file.write(result.getvalue())


if __name__ == '__main__':
    for name, link in links.items():
        try:
            create_pdf(link, __file__.split('.')[0] + '.' + name +'.03_pdf')
            print(link, 'ok')
        except Exception as err:
            print(link, 'err', err)

