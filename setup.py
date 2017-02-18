from setuptools import setup

setup(name='Shellcoding',
    version='0.0.1',
    description='Shellcoding library for assembly shellcode writing.',
    url="https://github.com/0x00-0x00/shellcoding.git",
    author="zc00l",
    author_email="andre.marques@fatec.sp.gov.br",
    license="MIT",
    packages=['shellcoding'],
    package_dir={'shellcoding': 'src'},
    package_data={'shellcoding': ['src/*']},
    scripts=['bin/shellcoding'],
    zip_safe=False)

