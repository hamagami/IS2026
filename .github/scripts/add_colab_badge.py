import glob
import json
import os
import urllib.parse

REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = os.environ["GITHUB_REF_NAME"]

for filepath in glob.glob("**/*.ipynb", recursive=True):
  with open(filepath, "r", encoding="utf-8") as f:
    nb = json.load(f)

  # 日本語やスペースを含むファイル名でもリンクが壊れないようURLエンコード
  encoded_path = urllib.parse.quote(filepath)
  colab_url = f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/{encoded_path}"
  badge_md = f"[![Open In Colab](https://google.com)]({colab_url})"

  # すでにバッジが含まれている場合はスキップ
  if nb.get("cells") and badge_md in "".join(
      nb["cells"][0].get("source", [])
  ):
    continue

  new_cell = {
      "cell_type": "markdown",
      "metadata": {},
      "source": [badge_md],
  }
  nb["cells"].insert(0, new_cell)

  with open(filepath, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
    f.write("\n")
