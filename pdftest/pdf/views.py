#!/usr/bin/python
# -*- coding: utf-8 -*-
from render_pdf import RenderPDF
from django.http import HttpResponse


# Create your views here.


def html2pdf(request):
    render = RenderPDF()
    # filename = render.html2pdf_from_string(string_list=["<html><h1>test</h1></html>"],
    #                                        filename='test.pdf')
    filename = render.html2pdf_from_url(['http://test.coolsite360.com/documents/doc-021724019383/5acb0fb8c4a59a33cae3fbb4.md'],
                                        filename='test.pdf')

    return HttpResponse(filename)
