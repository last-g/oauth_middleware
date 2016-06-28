from __future__ import division, unicode_literals, print_function, absolute_import

from setuptools import setup, find_packages

setup(
    name='oauth_middleware',
    version=0.1,  # TODO: Do not forget to update in __init__
    description="Simple flask_oauthlib based middleware for WSGI app to preform oauth",
    author="Last G",
    author_email='sergei.azovskov@zalando.de',
    packages=find_packages(),
    requires=[
        'flask',
        'flask_oauthlib',
        'werkzeug',
        'six'
    ]
)