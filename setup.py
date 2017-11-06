from distutils.core import setup

setup_req = ['numpy']
install_req = ['numpy']

setup(
    name = 'imhelp',
    packages = ['imhelp'],
    install_requires=install_req,
    setup_requires=setup_req,
    version = '0.0.1',
    description = 'General Image Helper Functions',
    author = 'Julian Tanke',
    url='https://github.com/justayak/imhelp'
)
