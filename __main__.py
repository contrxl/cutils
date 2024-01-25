'''
author: contrxl
date: jan 25 2024
'''

from commands import decode
from commands import encode
from commands import defang
from commands import hash
import click

@click.group(help="A program to decode or encode strings.")
@click.version_option("0.1.0", prog_name="cyutils")

def cli():
	pass

cli.add_command(hash.hash)
cli.add_command(decode.decode)
cli.add_command(encode.encode)
cli.add_command(defang.defang)

if __name__ == '__main__':
	cli()