pipeline{
    agent any
        stages{
            stage('Build') {
                sh "docker build -t my-project-2" #to build the image
            }
            stage('Deploy') {
                sh "docker compose down || true" #to stop old containers
                sh "docker run -d -p 8085:8000 my-project-2" #command to run the container
            }
        }
}