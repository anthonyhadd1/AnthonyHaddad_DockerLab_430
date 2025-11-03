pipeline {
    agent any

    triggers {
        // Auto check GitHub every 2 minutes
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/anthonyhadd1/AnthonyHaddad_DockerLab_430.git'
            }
        }

        stage('Build in Minikube Docker') {
            steps {
                bat '''
                REM === Switch Docker to Minikube ===
                call minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat

                REM === Build inside Minikube Docker ===
                docker build -t movie-app:latest -f "videostoreDOcker\\videostore (1)\\videostore\\Dockerfile" "videostoreDOcker\\videostore (1)\\videostore"
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                bat '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                kubectl rollout status deployment/movie-deployment
                '''
            }
        }
    }
}
