import click
from iparser import IPArser

@click.command()
@click.argument("path")
@click.pass_context
def main(ctx, path: str):
    IPArser.parse(path)

def start():
    main(obj={})