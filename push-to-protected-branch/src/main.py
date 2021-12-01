#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Commit and push it to a protected branch in Github """

import os
from os.path import dirname, join

from github import Github
from github import InputGitTreeElement
from dotenv import load_dotenv

ENCODING = "utf-8"

if __name__ == "__main__":
    # expose env variables if exists (for local dev)
    dotenv_path = join(dirname(__file__), ".env")
    load_dotenv(dotenv_path)

    github = Github(os.getenv("INPUT_GITHUB_TOKEN"))
    repository = github.get_repo(os.getenv("INPUT_REPOSITORY"))
    file_to_add = str(os.getenv("INPUT_FILES_TO_COMMIT")).split(",")
    origin_ref = repository.get_git_ref(f'heads/{os.getenv("INPUT_BRANCH_NAME")}')
    origin_sha = origin_ref.object.sha

    # Create a tag version
    if os.getenv("INPUT_CREATE_TAG"):
        repository.create_git_ref(
            f'refs/tags/{os.getenv("INPUT_TAG_VERSION")}', origin_sha
        )

    base_tree = repository.get_git_tree(origin_sha)
    element_list = list()
    for entry in file_to_add:
        with open(entry, "rb") as input_file:
            data = input_file.read().decode(ENCODING)
        element = InputGitTreeElement(entry, "100644", "blob", data)
        element_list.append(element)
    tree = repository.create_git_tree(element_list, base_tree)
    parent = repository.get_git_commit(origin_sha)
    commit = repository.create_git_commit(
        os.getenv("INPUT_COMMIT_MESSAGE"), tree, [parent]
    )
    origin_ref.edit(commit.sha)
