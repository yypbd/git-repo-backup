import os
import shutil
import zipfile
from datetime import datetime

import git
from git import InvalidGitRepositoryError, Tree
from tqdm import tqdm


class GitRepoBackup(object):
    def _get_files_from_tree(self, tree: Tree) -> list[str]:
        result = []
        for blob in tree.blobs:
            result.append(blob.path)

        for tree in tree.trees:
            result.extend(self._get_files_from_tree(tree))

        return result

    def _get_git_managed_file_list(self, repo_path: str) -> list[str]:
        repo = git.Repo(repo_path)
        tree = repo.head.commit.tree

        result = self._get_files_from_tree(tree)
        return result

    def backup(self, repo_path: str, dest_path: str, dest_type: str = 'zip', dest_name: str = '', add_timestamp: bool = True) -> str:
        if os.path.exists(repo_path) is False:
            return "[Error] git files - Repository path does not exist"
        if os.path.exists(dest_path) is False:
            return "[Error] git files - Destination path does not exist"

        try:
            file_list = self._get_git_managed_file_list(repo_path)
        except InvalidGitRepositoryError:
            return "[Error] git files - Invalid git repository"
        except Exception as e:
            return "[Error] git files - " + type(e).__name__

        # for file in file_list:
        #     print(file)

        if dest_name == '':
            dest_name = os.path.basename(repo_path)
        if add_timestamp:
            now = datetime.now()
            dest_name = dest_name + "_" + now.strftime("%Y%m%d%H%M%S")

        dest_path = os.path.join(dest_path, dest_name)

        if dest_type == 'zip':
            # compress
            zip_file_path = dest_path + ".zip"
            zip_file = zipfile.ZipFile(zip_file_path, 'w')

            with tqdm(total=len(file_list)) as pbar:
                for file in file_list:
                    filename_src = os.path.join(repo_path, file)
                    zip_file.write(filename_src, file, compress_type=zipfile.ZIP_DEFLATED)
                    pbar.update(1)

            zip_file.close()
        else:
            # copy files
            with tqdm(total=len(file_list)) as pbar:
                for file in file_list:
                    filename_src = os.path.join(repo_path, file)
                    filename_dest = os.path.join(dest_path, file)

                    dest_file_path = os.path.dirname(filename_dest)
                    if not os.path.exists(dest_file_path + "/"):
                        os.makedirs(dest_file_path, exist_ok=True)

                    shutil.copyfile(filename_src, filename_dest)
                    pbar.update(1)

        return "[Success] Backup completed"
