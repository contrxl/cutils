'''
author: contrxl
date: jan 8 2024
version: 0.1
'''

from commands import decode
from commands import encode
from commands import defang
import click
import base64

@click.group(help="A program to decode or encode strings.")

def cli():
	pass

cli.add_command(decode.decode)
cli.add_command(encode.encode)
cli.add_command(defang.defang)

if __name__ == '__main__':
	cli()