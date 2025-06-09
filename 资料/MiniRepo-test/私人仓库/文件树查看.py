from flask import Flask, render_template
import os
from git import Repo

app = Flask(__name__)

REPO_BASE_PATH = "./repos/user1/testrepo"  # 这是 clone 后的非裸仓库路径


@app.route("/repo/<repo_name>/tree/<path:tree_path>")
@app.route("/repo/<repo_name>/tree/", defaults={"tree_path": ""})
def browse_tree(repo_name, tree_path):
    repo_path = os.path.join(REPO_BASE_PATH)
    print(repo_path)
    repo = Repo(repo_path)
    commit = repo.head.commit
    tree = commit.tree

    # 导航到子目录
    parts = tree_path.strip("/").split("/") if tree_path else []
    for part in parts:
        tree = tree / part

    items = []
    for item in tree:
        items.append({
            "name": item.name,
            "type": "tree" if item.type == "tree" else "blob",
            "path": os.path.join(tree_path, item.name)
        })

    return render_template("tree.html", items=items, repo=repo_name, tree_path=tree_path)


@app.route("/repo/<repo_name>/blob/<path:file_path>")
def view_file(repo_name, file_path):
    repo = Repo(REPO_BASE_PATH)
    commit = repo.head.commit
    tree = commit.tree

    # 导航到文件 blob
    parts = file_path.strip("/").split("/")
    blob = tree
    for part in parts:
        blob = blob / part

    content = blob.data_stream.read().decode("utf-8", errors="ignore")
    return render_template("file.html", content=content, file_path=file_path)


if __name__ == '__main__':
    app.run(debug=True)
