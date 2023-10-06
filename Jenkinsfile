pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Pull the Docker image
                script {
                    docker.image('nekiwanuka/fgf-app-drepo').pull()
                }
            }
        }

        stage('Test') {
            steps {
                // Run tests for your Django application within the Docker container
                script {
                    docker.image('nekiwanuka/fgf-app-drepo').inside('-p 8000:8000') {
                        sh 'python manage.py test'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Run the Docker container
                script {
                    docker.image('nekiwanuka/fgf-app-drepo').run('-p 8000:8000 -d')
                }
            }
        }
    }
}
