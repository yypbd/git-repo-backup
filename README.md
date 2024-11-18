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

## Options

| option        | Type    | Value         | Description                                                                          |
|---------------|---------|---------------|--------------------------------------------------------------------------------------|
| repo_path     | String  |               | Git repository path.                                                                 |
| dest_path     | String  |               | Directory where backup files will be stored.                                         |
| dest_type     | Enum    | zip<br>dir    | zip : Compress to zip file.<br>dir : copy files to a directory<br> * Default is zip. |
| dest_name     | String  | Optional      | * Default is repo_path's name.                                                       |
| add_timestamp | Boolean | True or False | Adds the current time to the backup file or path.<br>* Default is True.              |
| add_untracked | Boolean | True or False | Adds untracked files<br>* Default is False.                                          |
