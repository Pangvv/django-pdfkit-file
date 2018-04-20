#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdfkit
from django.core.files.storage import get_storage_class
from django.conf import settings

try:
    from StringIO import StringIO
except ImportError:
    from cStringIO import StringIO

render_pdf_option = getattr(settings, "RENDER_PDF", {})

options = {
    'page-size': render_pdf_option.get('page-size', 'A4'),
    # 'margin-top': '0.75in',
    # 'margin-right': '0.75in',
    # 'margin-bottom': '0.75in',
    # 'margin-left': '0.75in',
    # 'dpi': 220,
    'background': None,
    'encoding': "UTF-8",
    'print-media-type': None,
    'disable-smart-shrinking': None,
    'zoom': 3.0,
    'orientation': 'Portrait',
    'cache-dir': '/tmp/pdf',
    'window-status': 'ready_to_print',
    'javascript-delay': 1000,
    'disable-javascript': None,
    # 'custom-header' : [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'no-outline': None
}


def html2pdf(urls, **kwargs):
    _urls = urls
    out = pdfkit.from_url(_urls, False,
                          options=options)

    return out


def html2pdf_string(filename, strings, opt=options):
    storage = get_storage_class()
    s = storage()
    _filename = filename
    _strings = strings
    _options = opt
    out_pdf = pdfkit.from_string(_strings,
                                 False,
                                 options=_options)
    output = StringIO()
    output.write(out_pdf)
    s.save(name=_filename, content=output)
    output.close()
    return _filename


class RenderPDF(object):

    def __init__(self, *args, **kwargs):
        self.options = options
        storage = get_storage_class()
        self.s = storage()

    def _save_to_file(self, content, filename):
        _filename = filename
        output = StringIO()
        output.write(content)
        self.s.save(name=_filename, content=output)
        output.close()
        return _filename

    def html2pdf_from_string(self, string, filename):
        out_pdf = pdfkit.from_string(string, False, options=self.options)
        return self._save_to_file(content=out_pdf,
                                  filename=filename)


if __name__ == "__main__":
    # urls = list()
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5ab7830e6c856923a8c71ba5.md")
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5a8e40e5c4a59a7623e933d3.md")
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5a8e42d4c4a59a787c7388f7.md")
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5a8e352ac4a59a73a8852e54.md")
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5a8e36f7c4a59a73a8852e55.md")
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5a8e374cc4a59a7623e933cb.md")
    # urls.append("http://v.coolsite360.com/documents/doc-021724019383/5a8e37a6c4a59a73a8852e56.md")
    # print (urls)
    # pdfkit.from_url(urls, "out.pdf", options=options)
    # pdfkit.from_url(['https://www.epub360.com/', 'http://www.coolsite360.com/'],
    #                 'out.pdf')
    html2pdf_string('/tmp/test.pdf', strings=["<html><h1>测试</h1><html>"])
