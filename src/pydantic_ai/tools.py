from .. import tools as t


def clone_repo(ssh_url: str) -> str:
    return t.clone_repo(ssh_url)

if __name__ == "__main__":
    print(clone_repo("git@github.com:anforsm/helloworld.git"))
