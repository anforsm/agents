import os
import git

def clone_repo(ssh_url):
    current_dir = os.path.abspath(__file__)
    clone_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), ".resources")

    # Determine default clone directory if not provided
    repo_name = os.path.basename(ssh_url).replace('.git', '')
    clone_dir = os.path.join(clone_dir, repo_name)

    # Clone the repository
    repo = git.Repo.clone_from(ssh_url, clone_dir)
    return repo_name

def ls(path):
    current_dir = os.path.abspath(__file__)
    work_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), ".resources")
    dir = os.path.join(work_dir, path)

    return os.popen(f"ls {dir}").read()



if __name__ == "__main__":
    clone_repo("git@github.com:anforsm/helloworld.git")
