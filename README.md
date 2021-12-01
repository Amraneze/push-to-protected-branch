# Push to a protected branch in Github

Github action to add files, commit and push them to a protected branch in a Github repository.

## Inputs

`* mandatory`

| Name | Default | Description | Example |
| ------------- | ------------- | ------------- | ------------- |
| `repository`* | | Your github respository's name | `push-to-protected-branch`
| `create_tag` | `false` | If you want to create a tag version | `true`
| `branch_name` | `main` | Your repository protected branch that you want to push to it | `master`
| `tag_version` | | The version that should be used to tag the release | `0.0.1`
| `github_token`* | | The Github PAT to be use on requests to the github api | `${{ secrets.GITHUB_TOKEN }}`
| `commit_message`* | | The message to be used as the commit message | `ci: build version v0.0.1 - [actions skip]`
| `files_to_commit`* | | Comma-separated list of files path. | `package.json,build.gradle`

>PS: Adding `[actions skip]` will not trigger an automatic build

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
      - name: Bump project's version
        id: version
        run: |
          PACKAGE_VERSION=$(node -p -e "require('./package.json').version")
          echo ::set-output name=TAG::${PACKAGE_VERSION}
      - name: Push files and tag
        uses: Amraneze/push-to-protected-branch@latest
        with:
          repository: ${{ github.repository }}
          branch_name: ${{ github.ref_name }}
          github_token: ${{ secrets.TOKEN }}
          commit_message: 'ci: build version v${{ steps.version.outputs.TAG }}'
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
      - name: Bump project's version
        id: version
        run: |
          PACKAGE_VERSION=$(node -p -e "require('./package.json').version")
          echo ::set-output name=TAG::${PACKAGE_VERSION}
      - name: Push files and tag
        uses: Amraneze/push-to-protected-branch@latest
        with:
          repository: ${{ github.repository }}
          create_tag: true
          branch_name: ${{ github.ref_name }}
          tag_version: ${{ steps.version.outputs.TAG }}
          github_token: ${{ secrets.TOKEN }}
          commit_message: 'ci: build version v${{ steps.version.outputs.TAG }}'
          files_to_commit: 'package.json,CHANGELOG.md,README.md'

```

### With Github App's access token

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    name: Build & tag version
    steps:
      ...
      - name: Bump project's version
        id: version
        run: |
          PACKAGE_VERSION=$(node -p -e "require('./package.json').version")
          echo ::set-output name=TAG::${PACKAGE_VERSION}
      - name: Generate token for GitHub App
        id: generate-access-token
        uses: getsentry/action-github-app-token@@v1.0.6
        with:
          app_id: ${{ secrets.GITHUB_APP_ID }}
          private_key: ${{ secrets.GITHUB_APP_PRIVATE_KEY }}
      - name: Push files and tag
        uses: Amraneze/push-to-protected-branch@latest
        with:
          repository: ${{ github.repository }}
          branch_name: ${{ github.ref_name }}
          github_token: ${{ steps.generate-access-token.outputs.token }}
          commit_message: 'ci: build version v${{ steps.version.outputs.TAG }}'
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
