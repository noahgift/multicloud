import click

def logic(name):
    if name == "Marco":
        return "Polo"
    else:
        return "No Match"

@click.command()
@click.option("--name")
def marco(name):
    """This is a Marco Polo function"""
    
    result = logic(name)
    click.echo(result)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    marco()