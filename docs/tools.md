---
hide:
  - navigation
  - tags
---

<h1></h1>

# Cheat Code For Tools
 
## Git
 
- git basic

```
git config --global user.email MY_NAME@example.com

git config --global user.name "MY_NAME"

git clone {url}
 
git branch -a (list of  branch)

git checkout {branch name}

git add .

git status

git commit -am "UPD"

git push origin <branch name>
```

- fetch git user name

```
git config user.name

git config user.email
```

- git create new branch name

```
git checkout -b <branch_name>
```

- undo add 

```
git reset
```

- uncommit

```
git reset HEAD^
```

- git push
```
git push origin <branch name>
 
git push -f origin <branch name>
 
git fetch
```

- for pushing into new repositories

```
git add .
git commit -am "UPD"
git branch {branch name} ##create new branch
git remote add origin {gitcloneurl}  ##add git remote url  
##add git credentials
git push origin {branch name}

```
- merge branch

```
vscode > 
git clone 
git checkout main branch
git pull
git checkout feature branch
git merge main branch ## if you want to update feature branch with main
## you will get merge conflicts in vscode
## resolve merge conflicts

git commit
git push feature branch
 
git merge {branch name}  "enter the branch which you have to merge into your branch"
```

- rebase 

```
git rebase {branch name}
```

- show commit history

```
git log

git log -p -1 #to show last commit
```

- to delete branch

```
git branch --delete <branchname>
```

### git using python

- get current branch name

```
os.system('git rev-parse --abbrev-ref HEAD')
```

- get repository name

```
os.system("git remote get-url origin")
```

- git commit without verify
 
```
git commit –no-verify –m "message"
```

## Docker

- pull images

```
docker pull <image name>
```

- display images

```
docker images
```

- display all containers

```
docker ps -a
```

- run container
```
docker run -it <repository-name> bash
```

- work on container
```
docker exec -it <container_id> bash
```

- stop container
```
docker stop <container_id>
```

- remove container

```
docker rm <container_id>
```

- kill container

```
docker kill <container_id>
```

- check containers with runnning

```
docker ps

docker container ls
```

- to remove image

```
docker container ls

docker rmi <image_id>

docker image rm <image_name>
```

- Remove all unused containers, volumes, networks and images

```
docker system prune -a --volumes
```

- to push images in docker hub

```
docker container ls

docker commit <container_id> imuser/ansible-server(any iimage name)

docker images( to chechk)

docker login

docker push imuser/ansible-server(we can give any iimage name)
```

## Python

### Create Env

- create virtual environment runnning

```
python -m venv venv
```
 
- start environment based on your command line tool, e.g.

```
.\venv\Scripts\activate
```

- check installed modules
```
pip list
```

- create requirement.txt file

```
pip freeze > requirements.txt
```

- install all relevant modules via pip

```
pip install -r requirements.txt
```

- install python package for local development and usage:

```
python -m pip install -e .
```