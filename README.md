# Push to a protected branch in Github

Github action to add files, commit and push them to a protected branch in a Github repository.

## Inputs

`* mandatory`

| Name | Default | Description | Example |
| ------------- | ------------- | ------------- | ------------- |
| `repository`* | | Your github respository's name | `push-to-protected-branch`
| `create_tag` | `false` | If you want to create a tag version | `true`
| `branch_name` | `main` | Your repository protected branch that you want to push to it | `master`
| `github_user` | | Your Github user | `Amraneze`
| `tag_version` | | The version that should be used to tag the release | `0.0.1`
| `github_token`* | | The Github secret token to be use on requests to the github api | `${{ secrets.GITHUB_TOKEN }}`
| `commit_message`* | | The message to be used as the commit message | `ci: build version v0.0.1`
| `files_to_commit`* | | Comma-separated list of files path. | `package.json,build.gradle`

## Example

An example of how to use this github action:

### Without creating a tag version

```yaml
name: Build

on:
  workflow_dispatch:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    name: Build & tag version
    steps:
      ...
      - name: Push files and tag
        uses: Amraneze/push-to-protected-branch@v1
        with:
          repository: 'push-to-protected-branch'
          branch_name: 'master'
          github_token: ${{ secrets.TOKEN }}
          commit_message: 'ci: build version v${BUILD_VERSION}'
          files_to_commit: 'package.json,CHANGELOG.md,README.md'

```

### With a tag version

```yaml
name: Build

on:
  workflow_dispatch:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    name: Build & tag version
    steps:
      ...
      - name: Push files and tag
        uses: Amraneze/push-to-protected-branch@v1
        with:
          repository: 'push-to-protected-branch'
          create_tag: true
          branch_name: 'master'
          tag_version: '0.0.1'
          github_token: ${{ secrets.TOKEN }}
          commit_message: 'ci: build version v${BUILD_VERSION}'
          files_to_commit: 'package.json,CHANGELOG.md,README.md'

```

>Note: If you are using `${{ secrets.GITHUB_TOKEN }}` instead of your own generated token, then you should specify the user of the repository `github_user`. Example:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    name: Build & tag version
    steps:
      - name: Push files and tag
        uses: Amraneze/push-to-protected-branch@v1
        with:
          repository: 'push-to-protected-branch'
          branch_name: 'master'
          github_user: 'Amraneze'
          github_token: ${{ secrets.TOKEN }}
          commit_message: 'ci: build version v${BUILD_VERSION}'
          files_to_commit: 'package.json,CHANGELOG.md,README.md'

```

## Requirements
You should install [Peotry](https://python-poetry.org) and run this following command to add git hooks:

```
peotry install
pre-commit install
```

## Building
For building the project you can use peotry cli to do so, for that you can run this command `peotry build`

## Contributions
We would :heart: contributions to improve this action. Please feel free to do so.
