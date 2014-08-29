'''
required:
 - wkhtmltopdf system package
 - pdfkit python package
'''
import pdfkit


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
    pdfkit.from_url(input, output)


if __name__ == '__main__':
    for name, link in links.items():
        try:
            create_pdf(link, __file__.split('.')[0] + '.' + name +'.03_pdf')
            print(link, 'ok')
        except Exception as err:
            print(link, 'err', err)
