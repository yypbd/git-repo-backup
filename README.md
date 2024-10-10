# Git Repo Backup

## Description

GitRepoBackup is a utility for backup only files managed by git repositories.

## Features

- Backup files managed by git repositories
- Copy files to a directory
- Compress files to a zip file

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
