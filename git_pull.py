# conda install GitPython
import git

repos = [
    "enigma_codex/",
    "eRODev/",
    "essencera/",
    "essencero_restoration/",
    "mtg_toolkit/",
    "python_projects/",
]


for i in range(0, len(repos)):
    repo_dir = "D:\\repos\\" + repos[i]
    print("Pulling: " + repos[i])
    g = git.cmd.Git(repo_dir)
    g.pull()
