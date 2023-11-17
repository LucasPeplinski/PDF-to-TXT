import argparse
import os
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PDF to text or XML')
    parser.add_argument('directory', help='The directory containing the PDF files.')
    parser.add_argument('-t', '--text', help='Generate text output.', action='store_true')
    parser.add_argument('-x', '--xml', help='Generate XML output.', action='store_true')

    args = parser.parse_args()

    if args.text:
        os.system("python3 ./Scripts/script_plaintext.py " + args.directory)

    if args.xml:
        os.system("python3 ./Scripts/script_xml.py " + args.directory)
