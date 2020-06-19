from setuptools import setup, find_packages
import logging
logger = logging.getLogger(__name__)

name = 'alime'
package_name = name
version = '0.1.0'

try:
    with open('README.md', 'r') as f:
        long_desc = f.read()
except:
    logger.warning('Could not open README.md.  '
                   'long_description will be set to None.')
    long_desc = None

setup(
    name = package_name,
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'alime=alime.__main__:main',
        ]},
    version = version,
    description = 'Animated anti-bot email obfuscation for your website',
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    author = 'Casey Duckering',
    url = f'https://github.com/cduck/{name}',
    download_url = f'https://github.com/cduck/{name}/archive/{version}.tar.gz',
    keywords = ['html', 'css', 'email', 'scrape'],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: IPython',
        'Framework :: Jupyter',
    ],
    install_requires = [
    ],
)

