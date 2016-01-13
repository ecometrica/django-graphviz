#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-graphviz',
    version='0.1.1',
    description='Django Graphviz extension',
    author='gsoftware@free.fr',
    author_email='gsoftware@free.fr',
    url='http://code.google.com/p/django-graphviz/',
    packages=['graphviz', 'graphviz.management', 'graphviz.management.commands', 'graphviz.migrations'],
    package_data={'graphviz': ['graphviz/templates/graphviz/*.dot']},
    zip_safe=False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: End Users/Desktop', 
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Database'
    ]
)
