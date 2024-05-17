#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import click

@click.group()
def cli():
    pass

@cli.command()
def setup():
    click.echo("Select an option:")
    click.echo("1. Uninstall and destroy previous environment")
    click.echo("2. Install and set up a new fresh environment")
    click.echo("3. Use previous configuration")
    click.echo("4. Exit")
    option = click.prompt("Enter option", type=int)
    if option == 1:
        teardown()
    elif option == 2:
        install()
    elif option == 3:
        click.echo("Using previous configuration...")
    elif option == 4:
        click.echo("Exiting...")
    else:
        click.echo("Invalid option.")

def install():
    click.echo("Setting up the project structure...")
    # Create notebooks directory
    os.makedirs("notebooks", exist_ok=True)

    # Write sample notebook content
    with open("notebooks/sample_notebook.ipynb", "w") as f:
        f.write("""{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}""")

    # Write Conda environment file
    with open("environment.yml", "w") as f:
        f.write("""name: my_notebook_env
channels:
  - conda-forge
dependencies:
  - python=3.8
  - jupyterlab
  - graphviz
  - matplotlib
  - networkx
  - requests
  - pip
  - pip:
    - gcp-diagrams""")

    # Write requirements file
    with open("requirements.txt", "w") as f:
        f.write("""jupyterlab
graphviz
matplotlib
networkx
requests
gcp-diagrams""")
    click.echo("Project structure set up successfully.")

def teardown():
    click.echo("Tearing down the project structure...")
    # Remove notebooks directory
    subprocess.run(["rm", "-rf", "notebooks"])

    # Remove environment files
    subprocess.run(["rm", "-f", "environment.yml", "requirements.txt"])
    click.echo("Project structure torn down successfully.")

if __name__ == "__main__":
    setup()
