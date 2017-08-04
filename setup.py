from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='hal_cocalc',
    version='0.1',
    packages=['hal_cocalc'],
    description='CoCalc kernel for Jupyter',
    long_description=readme,
    author='Hal Snyder',
    author_email='hsnyder@sagemath.com',
    url='https://github.com/DrXyzzy/cc-ker',
    classifiers=[
        'Intended Audience :: CoCalc Developers',
        'License :: OSI Approved :: GPLv3',
        'Programming Language :: Python :: 3',
        'Topic :: Mathematics :: Server',
    ],
)