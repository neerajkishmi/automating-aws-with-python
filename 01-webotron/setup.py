from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Neeraj Kishmi',
    author_email='neeraj.kishmi@gmail.com',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/neerajkishmi/automating-aws-with-python/tree/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
