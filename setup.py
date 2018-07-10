from setuptools import setup

DESCRIPTION = "A Django HTML TO PDF"

LONG_DESCRIPTION = None

version = '0.2'

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='django-pdfkit',
    version=version,
    packages=['render_pdf'],
    author='jiaxin',
    author_email='edison7500@gmail.com',
    url='https://github.com/edison7500/django-pdfkit-file.git',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    install_requires=['pdfkit >=0.6.1'],
    classifiers=CLASSIFIERS,
    zip_safe=False,
)

__author__ = 'edison7500'
