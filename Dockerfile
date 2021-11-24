FROM python:3.8-slim-buster

LABEL "com.github.actions.name"="Commit and push it to a protected branch"
LABEL "com.github.actions.description"="Add files, commit and push the commit to a protected branch by Github hooks using Github API"
LABEL "com.github.actions.icon"="git-branch"
LABEL "com.github.actions.color"="green"

WORKDIR /action/workspace

COPY requirements.txt .
COPY ./push-to-protected-branch/src/main.py .

RUN groupadd -r github && useradd -r -g github github
RUN python3 -m pip install --no-cache-dir -r requirements.txt \
    && apt-get -y update \
    && apt-get -y install --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

USER github

CMD ["/action/workspace/main.py"]
ENTRYPOINT ["python3", "-u"]
