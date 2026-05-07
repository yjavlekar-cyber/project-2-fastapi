pipeline{
    agent any
        stages{
            stage('Build') {
                sh "docker build -t my-project-2"
            }
            stage('Deploy') {
                sh "docker compose down || true"
                sh "docker run -d -p 8085:8000 my-project-2"
            }
        }
}