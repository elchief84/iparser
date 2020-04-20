import click

@click.group()
@click.option("--ssid", help="WiFi network name.")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="WiFi password.")
@click.pass_context
def main(ctx, ssid: str, security: str = "", password: str = ""):
    print("cli")

@main.command()
@click.pass_context
def echo(phrase):
    print(phrase)

def start():
    main(obj={})

if __name__ == "__main__":
    start()