'''
author: contrxl
date: jan 8 2024
version: 0.1

Script to decode/encode stuff.
'''
import base64
import click

'''
@click.group ("carver") instatiates group class.
@click.argument("carve") passes argument.
@click.pass_context tells group to use the context, without this the context is not visible.

Group is named "carver" and cli argument is initially "carve"
'''

@click.group("carver")
@click.argument("carve")
@click.option("-b64", "--base64", help="Specify base64 as the string to decode.")
@click.pass_context


def carver(carve, ctx):
	print("Hello")

def b64_carve(b64: str, ctx):
	if b64 is not None:
	#	b64_in = input("Enter base64:")
		b64_out = (base64.b64decode(b64).decode('utf-8'))
		b64_print = print("Decoded b64: " + b64_out)


def main():
	carver(prog_name="carver")

if __name__ == '__main__':
	main()
