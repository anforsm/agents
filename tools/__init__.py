import os
import git

def clone_repo(ssh_url):
    current_dir = os.path.abspath(__file__)
    clone_dir = os.path.join(os.path.dirname(current_dir), ".resources")
    print(clone_dir)

    try:
        # Determine default clone directory if not provided
        if clone_dir is None:
            repo_name = os.path.basename(ssh_url).replace('.git', '')
            clone_dir = os.path.join(os.getcwd(), repo_name)
        
        # Clone the repository
        repo = git.Repo.clone_from(ssh_url, clone_dir)
        
        print(f"Repository cloned successfully to {clone_dir}")
        return clone_dir
    except git.GitCommandError as e:
        print(f"Git error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    clone_repo("git@github.com:anforsm/helloworld.git")