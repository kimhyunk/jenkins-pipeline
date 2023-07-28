pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        echo 'checkout'
      }
    }

    stage('pod') {
      steps {
        podTemplate(activeDeadlineSeconds: 1, cloud: 'kubernetes')
      }
    }

  }
}