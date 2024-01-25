'''
author: contrxl
date: jan 25 2024
'''
import click
import base64
import urllib.parse

@click.command()
@click.argument("mode", type=click.STRING)
@click.argument("string", type=click.STRING)
@click.option("-o", "--output", type=click.STRING, help="Provide a filename to output to in current directory. File will be a .txt")

def decode(string, mode, output):
	"""This will decode any provided string.\n
	Accepted modes: b64, hex, url"""
	if mode == "b64":
		if output:
			file_object = open(output + ".txt", "w")
			b64_out = (base64.b64decode(string).decode('utf-8'))
			b64_file = file_object.write("String decodes to: " + b64_out)
		else:
			b64_out = (base64.b64decode(string).decode('utf-8'))
			print("String decodes to: " + b64_out)
	if mode == "url":
		if output:
			file_object = open(output + ".txt", "w")
			url_out = file_object.write("URL decodes to: " + urllib.parse.unquote(string))
		else:
			url_transl = print("URL decodes to: " + urllib.parse.unquote(string))
	if mode == "hex":
		if output:
			file_object = open(output + ".txt", "W")
			hex_out = file_object.write("String decodes to: " + bytes.fromhex(string).decode('utf-8'))
		else:
			hex_out = bytes.fromhex(string).decode('utf-8')
			print(hex_out)