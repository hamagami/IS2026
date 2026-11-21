name: Add Colab Badge

on:
  push:
    paths:
      - '**.ipynb'

permissions:
  contents: write

jobs:
  add-badge:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Add Colab badge to notebooks
        env:
          GITHUB_REPOSITORY: ${{ github.repository }}
          GITHUB_REF_NAME: ${{ github.ref_name }}
        run: python .github/scripts/add_colab_badge.py

      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@://github.com"
          git add '*.ipynb'
          git diff --staged --quiet || (git commit -m "Add Open in Colab badge" && git push)
