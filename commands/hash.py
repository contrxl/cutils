'''
author: contrxl
date: jan 25 2024
'''

import click
import hashlib
from colorama import Fore, Back, Style, init
from sys import stdout

init(autoreset=True)
@click.command()
@click.argument("mode", type=click.STRING)
@click.argument("string", type=click.STRING)

def hash(string, mode):
    if mode == "md5":
        print(f"Hash digest: {hashlib.md5(b"(string)").hexdigest()}") 
    if mode == "sha1":
        print(f"Hash digest: {hashlib.sha1(b"(string)").hexdigest()}") 
    if mode == "sha224":
        print(f"Hash digest: {hashlib.sha224(b"(string)").hexdigest()}")
    if mode == "sha256":
        print(f"Hash digest: {hashlib.sha256(b"(string)").hexdigest()}")
    if mode == "sha384":
        print(f"Hash digest: {hashlib.sha384(b"(string)").hexdigest()}")
    if mode == "sha512":
        print(f"Hash digest: {hashlib.sha512(b"(string)").hexdigest()}")
    if mode == "sha3_224":
        print(f"Hash digest: {hashlib.sha3_224(b"(string)").hexdigest()}")
    if mode == "sha3_256":
        print(f"Hash digest: {hashlib.sha3_256(b"(string)").hexdigest()}")
    if mode == "sha3_384":
        print(f"Hash digest: {hashlib.sha3_384(b"(string)").hexdigest()}")
    if mode == "sha3_512":
        print(f"Hash digest: {hashlib.sha3_512(b"(string)").hexdigest()}")
    else:
        print("\n" + Fore.WHITE + Back.RED + "Not a valid hash type!", end="\n")