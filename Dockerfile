FROM python:3.9-alpine

LABEL "com.github.actions.name"="Commit and push it to a protected branch"
LABEL "com.github.actions.description"="Add files, commit and push the commit to a protected branch by Github hooks using Github API"
LABEL "com.github.actions.icon"="git-branch"
LABEL "com.github.actions.color"="green"

WORKDIR /action/workspace

COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY main.py .
COPY src ./src

CMD ["/action/workspace/main.py"]
ENTRYPOINT ["python3", "-u"]