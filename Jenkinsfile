pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'dhivyadharshini2106/unigo'
        APP_PORT = '5000'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker build -t unigo-test .
                    docker run --rm unigo-test python -m pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                    docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                        -u "$DOCKER_USERNAME" \
                        --password-stdin

                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop unigo || true
                    docker rm unigo || true

                    docker run -d \
                        --restart unless-stopped \
                        -p ${APP_PORT}:5000 \
                        --name unigo \
                        ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl -f http://localhost:${APP_PORT}/health
                '''
            }
        }
    }

    post {
        success {
            echo 'UniGo CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'UniGo pipeline failed. Check the failed stage logs.'
        }
    }
}
