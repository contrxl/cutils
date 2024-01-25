'''
author: contrxl
date: jan 8 2024
'''
import click
import base64
from util import url_in

@click.command()
@click.argument("mode", type=click.STRING)
@click.argument("string", type=click.STRING)
@click.option("-o", "--output", type=click.STRING, help="Output string to a file in the current directory.")

def encode(string, output, mode):
	"""This will encode any provided string\n
	To encode strings containing quotation marks please use triple quotes: '''example_with_quotes'''\n
	Accepted modes: b64, url """

	string_bytes = string.encode("ascii")
	if mode == "b64":
		if output:
			file_object = open(output + ".txt", "w")
			b64_bytes = (base64.b64encode(string_bytes))
			b64_string = b64_bytes.decode("ascii")
			b64_file = file_object.write("String encodes to: " + b64_out.decode("ascii"))
		else:
			b64_out = (base64.b64encode(string_bytes).decode("ascii"))
			print("String encodes to: " + b64_out)
	if mode == "url":
		if output:
			file_object = open(output + ".txt", "w")
			url_out = file_object.write("URL encodes to: " + string.translate(url_in.url_list))
		else:
			print("URL encodes to: " + string.translate(url_in.url_list))

	