# Pronto.ai Take home Assignment

## Problem Requirements

- The program should take one argument: `git_dir`: directory in which to assess git status.
- Your program should print the following things:
  - active branch (branch name)
  - whether repository files have been modified (boolean)
  - whether the current head commit was authored in the last week (boolean)
  - whether the current head commit was authored by Rufus (boolean)

## Running Instructions

- Have Python 3.9+ installed on your machine.
- Clone the repository to your local machine : `git clone https://github.com/reubenabraham/ProntoAssignment.git`
- Navigate to the repository location, then follow instructions [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to install `venv`, create a virtual environment (`python3 -m venv env`) and activate the virtual environment (`source env/bin/activate`).
- From within the virtual environment, install requirements `pip install -r requirements.txt`
- `pip freeze` to confirm you have `GitPython` installed.
- Run `python3 main.py _full_path_to_repository_` - output is printed to stdout.