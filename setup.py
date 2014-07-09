from setuptools import setup

setup(
    name='changeorg',
    version='0.1',
    description="A python module to interact with the change.org API",
    long_description="""
Changeorg - a python module to interact with the change.org API
---------------------------------------------------------------
        """,
    classifiers=[
        ],
    keywords='change.org',
    author='Michael Bauer',
    author_email='michael.bauer@okfn.org',
    url='http://github.com/mihi-tr/changeorg',
    license='BSD',
    py_modules=['changeorg'],
    zip_safe=False,
    tests_require=[],
    install_requires=['requests'],
    entry_points=\
    """ """,
)
