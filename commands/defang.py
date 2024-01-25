'''
author: contrxl
date: jan 25 2024
'''
import click

@click.command()
@click.argument("url", type=click.STRING)
@click.option("-xh", "--xhttps", is_flag=True, help="Replace HTTPS with HXXPS")
@click.option("-xd", "--xdot", is_flag=True, help="Replace . with [.]")
@click.option("-xs", "--xslash", is_flag=True, help="Replace :// with [://]" )

def defang(url, xhttps, xdot, xslash):
	'''This will defang a provided URL.\n
	If no option is provided, all options will apply.\n
	Example Usage: cyutils defang -xh -xd https://example.com'''
	if xhttps and not xdot and not xslash:
		defang = url.replace("https", "hxxps").replace("http", "hxxp")
		print("Defanged URL: " + defang)
	if xdot and not xhttps and not xslash:
		defang = url.replace(".", "[.]")
		print("Defanged URL: " + defang)
	if xslash and not xhttps and not xdot:
		defang = url.replace("://", "[://]")
		print("Defanged URL: " + defang)
	if xhttps and xdot:
		defang = url.replace("https", "hxxps").replace("http", "hxxp").replace(".", "[.]")
		print("Defanged URL: " + defang)
	if xhttps and xslash:
		defang = url.replace("https", "hxxps").replace("http", "hxxp").replace("://", "[://]")
		print("Defanged URL: " + defang)
	if xdot and xslash:
		defang = url.replace(".", "[.]").replace("://", "[://]")
		print("Defanged URL: " + defang)
	if xhttps and xslash and xdot:
		defang = url.replace("https", "hxxps").replace("http", "hxxp").replace(".","[.]").replace("://", "[://]")
		print("Defanged URL: " + defang)
	elif not xhttps and not xdot and not xslash:
		defang = url.replace("https", "hxxps").replace("http", "hxxp").replace(".","[.]").replace("://", "[://]")
		print("Defanged URL: " + defang)