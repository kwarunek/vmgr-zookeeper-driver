import io
import re
from os.path import join, dirname, abspath
from setuptools import setup, find_packages


def read(name):
    here = abspath(dirname(__file__))
    return io.open(
        join(here, name), encoding='utf8'
    ).read()


setup(
    name="vmgr",
    version="0.2.0",
    author='Dreamlab - PaaS KRK',
    author_email='paas-support@dreamlab.pl',
    url='https://github.com/Dreamlab/vmgr',
    description='Runtime and lock management for Vmgr',
    long_description='%s\n%s' % (
        read('README.rst'),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=read('requirements.txt').split('\n'),
    zip_safe=False,
    entry_points={
        'vmgr.driver.runtime': ['ZookeeperDriver = vmgr_zookeeper_driver:ZookeeperDriver'],
    },
    keywords=['vmgr', 'zookeeper', 'runtime', 'lock'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Development Status :: 4 - Beta'
    ]
)
