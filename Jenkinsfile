pipeline {
  agent {
    kubernetes {
      yaml '''
apiVersion: v1
kind: Pod
spec:
  volumes:
  - name: docker-socket
    emptyDir: {}
  containers:
  - name: docker
    image: docker:19.03.1
    readinessProbe:
      exec:
        command: [sh, -c, "ls -S /var/run/docker.sock"]
    command:
    - sleep
    args:
    - 99d
    volumeMounts:
    - name: docker-socket
      mountPath: /var/run
  - name: docker-daemon
    image: docker:19.03.1-dind
    securityContext:
      privileged: true
    volumeMounts:
    - name: docker-socket
      mountPath: /var/run
  - name: git
    image: alpine/git:latest
    command:
    - sleep
    args:
    - 99d
'''
      defaultContainer 'docker'
    }

  }
  stages {
    stage('Checkout') {
      steps {
        container(name: 'docker') {
          checkout scm
        }

      }
    }

    stage('Build') {
      steps {
        container(name: 'docker', shell: 'cd docker; ./build-and-push-docker-registry.sh')
      }
    }

    stage('unit test') {
      steps {
        container(name: 'docker')
      }
    }

    stage('push') {
      steps {
        container(name: 'docker')
      }
    }

  }
  post {
    always {
      echo 'This will always run'
    }

    success {
      echo 'This will run only if the pipeline succeeds'
    }

    failure {
      echo 'This will run only if the pipeline fails'
    }

  }
}