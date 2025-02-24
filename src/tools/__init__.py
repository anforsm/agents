import os
import git

BASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".resources")
os.makedirs(BASE_PATH, exist_ok=True)

def clone_repo(ssh_url):
    clone_dir = BASE_PATH

    # Determine default clone directory if not provided
    repo_name = os.path.basename(ssh_url).replace('.git', '')
    clone_dir = os.path.join(clone_dir, repo_name)

    # Clone the repository
    repo = git.Repo.clone_from(ssh_url, clone_dir)
    return repo_name

def ls(path):
    dir = os.path.join(BASE_PATH, path)
    return os.popen(f"ls {dir}").read()

def cat(path):
    file_path = os.path.join(BASE_PATH, path)
    return os.popen(f"cat {file_path}").read()

def write_file(path, content):
    file_path = os.path.join(BASE_PATH, path)
    with open(file_path, 'w') as file:
        file.write(content)
    return file_path

if __name__ == "__main__":
    clone_repo("git@github.com:anforsm/helloworld.git")
