import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pifttt',
    version='0.0.1',
    author='Daniel Matias Ferrer',
    author_email='controlledflame@gmail.com',
    description='A Python package to simplify sending requests to IFTTT webhooks.',
    license='MIT',
    keywords='IFTTT webhooks',
    url='https://github.com/xassbit/pifttt',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
    ],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
    ],
)
