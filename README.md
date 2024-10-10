# Git Repo Backup

## Description


## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# simple default
python main.py backup --repo_path=<repo_path> --dest_path=<dest_path>

# to directory with no timestamp
python main.py backup --repo_path=<repo_path> --dest_path=<dest_path> --dest_type=dir --dest_name=backup_filename --add_timestamp=False
```
