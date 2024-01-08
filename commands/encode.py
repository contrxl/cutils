'''
author: contrxl
date: jan 8 2024
version: 0.1
'''
import click
import base64

@click.command()
@click.argument("string", type=click.STRING)
@click.option("-o", "--output", type=click.File(mode="r"), help="Output string to a file in the current directory.")

def encode(string, output):
	"""This will encode any provided string."""
	string_bytes = string.encode("ascii")
	if output:
		file_object = open(output + ".txt", "w")
		b64_out = (base64.b64encode(string_bytes))
		b64_file = file_object.write("String encodes to: " + b64_out.decode("ascii"))
	else:
		b64_out = (base64.b64encode(string_bytes).decode("ascii"))
		print("String encodes to: " + b64_out)
	