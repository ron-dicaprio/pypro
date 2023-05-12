# How-To-Use-JenkinsPipline-In-Docker
## pull jenkins image
```sh
# docker pull jenkins/jenkins:lts
# docker run CMD
docker run \
  -u root \
  -dit \
  --name docker-jenkins \
  -p 9000:8080 \
  -p 50000:50000 \
  -v /var/jenkins-data:/var/jenkins_home \
  -v /usr/bin/docker:/usr/bin/docker \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```
![我的啊实打实的](https://www.jenkins.io/doc/book/resources/tutorials/setup-jenkins-01-unlock-jenkins-page.jpg) 
