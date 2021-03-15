import setuptools

long_description = """
Python interface to communicate with HaveIBeenPwned.com.
"""

setuptools.setup(
    name='hibp-zetsumeishi',
    version='0.1.2',
    author='zetsumeishi',
    author_email='olivier.loustaunau@gmail.com',
    description='Python interface to communicate with HaveIBeenPwned.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zetsumeishi/hibp',
    packages=setuptools.find_packages(exclude=('tests',)),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
