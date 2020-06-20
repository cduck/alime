import argparse
import sys

from .generate import Alime


def main():
    parser = argparse.ArgumentParser(
        description=
        'Generate animated anti-bot email obfuscation HTML+CSS+JS for your '
        'website.  https://github.com/cduck/alime',
        epilog=
        'The files alime-example.html, alime.css, and alime.js will be written '
        'to the current directory.\n'
        'More options are available from the Python code.')
    parser.add_argument('email', type=str, help=
        'The email address to obfuscate')
    args = parser.parse_args()

    gen = Alime(email=args.email)
    gen.save()

if __name__ == '__main__':
    # Fix executable name in help when run with `python3 -m alime`
    if len(sys.argv) >= 1 and sys.argv[0].endswith('__main__.py'):
        sys.argv[0] = 'python -m alime'
    main()
