# Project-Launcher
A Ubuntu Desktop Launcher - Skeleton of a Launcher for a New Project

## Purpose
Help set up a new projects work station, configuration, and or any other actionable items when starting work on a project. 

- Start Django.
- vagrant up
- Start Flask site.
- A developers environment
- logging

## Templates
#### launcher.sh.jinja
    - project_name # Name of the project (visible name).

#### project_launcher.desktop.jinja
    - terminal # Show termial (true or false).
    - icon200x200 # path to the launchers icon.
    - project_name # Name of the project (visible name).
    - launcher_script # Script launching command.

#### Makefile.jinja
    - desktop_file_path # Path to the .desktop file.
    - desktop_file # Name of the .desktop file.