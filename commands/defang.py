'''
author: contrxl
date: jan 8 2024
version: 0.1
'''
import click

@click.command()
@click.argument("url", type=click.STRING)


def defang(url):
	'''This will defang a provided URL.'''
	defang = url.replace("https", "hxxps")
	defang_2 = defang.replace(".", "[.]")
	defang_final = defang_2.replace("://", "[://]")
	print("Defanged URL: " + defang_final)