import click
from iparser import IPArser

@click.group(invoke_without_command=True)
@click.option("--output", "-o", help="custom output folder")
@click.option("--no-output", "-no", help="disable json output", is_flag=True)
@click.argument("path")
@click.pass_context
def main(ctx, path: str, output: str, no_output: str):
    IPArser.parse(path, output, no_output)

@main.command()
@click.pass_context
def icons(ctx, path: str, out: str):
    IPArser.extractIcon(path, out)

def start():
    main(obj={})