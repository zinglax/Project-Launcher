"""Create new Ubuntu Launcher."""
import os
import jinja2
from distutils.dir_util import copy_tree
import subprocess
import click


@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.argument('project')
def create(directory, project):
    """Create new Ubuntu Launcher.

    Usage: python project_laucher.py /new/launcher/path/ ProjectName

    Args:
        directory (TYPE): Where the launcher will be created.
        project (TYPE): The name of the project (or application).
    """
    working_directory = os.getcwd()
    stock_directory = os.path.join(working_directory, "stock")

    # Target Directory (Launching Folder)
    launcher_dir = os.path.join(directory, "launcher")

    template_vars = {
        "project_name": project,
        "terminal": "true",
        "icon200x200": os.path.join(launcher_dir, "200x200.png"),
        "launcher_script": os.path.join(launcher_dir, "launcher.sh"),
        "desktop_file_path": launcher_dir,
        "desktop_file": project + ".desktop",
    }

    # Creates Launching Folder
    os.makedirs(launcher_dir, exist_ok=True)

    # Copy Stock to Launching Folder
    copy_tree(src=stock_directory, dst=launcher_dir)

    # Jinja Environment
    template_loader = jinja2.FileSystemLoader(
        [os.path.join(working_directory, "templates")])
    jinja_env = jinja2.Environment(loader=template_loader)

    # Create project_launcher.desktop
    desktop_file = os.path.join(template_vars["desktop_file_path"],
                                template_vars["desktop_file"])
    with open(desktop_file, "w+") as f:
        f.write(
            jinja_env.get_template("project_launcher.desktop.jinja").render(
                template_vars))

    # Create Makefile
    make_file = os.path.join(template_vars["desktop_file_path"], "Makefile")
    with open(make_file, "w+") as f:
        f.write(jinja_env.get_template("Makefile.jinja").render(template_vars))

    # Create launcher.sh
    with open(template_vars["launcher_script"], "w+") as f:
        f.write(
            jinja_env.get_template("launcher.sh.jinja").render(template_vars))

    # Make launcher.sh executable
    subprocess.call(
        ['chmod 777 ' + template_vars["launcher_script"]], shell=True)


if __name__ == '__main__':
    create()
