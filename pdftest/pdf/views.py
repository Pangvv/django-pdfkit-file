#!/usr/bin/python
# -*- coding: utf-8 -*-
from render_pdf import RenderPDF
from django.http import HttpResponse

# Create your views here.


def html2pdf(request):


    render = RenderPDF()
    filename = render.html2pdf_from_string(string="<html><h1>test</h1></html>", filename='test.pdf')

    return HttpResponse(filename)
