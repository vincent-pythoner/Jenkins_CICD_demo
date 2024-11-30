pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                git 'https://github.com/vincent-pythoner/Jenkins_CICD_demo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    // 使用 Dockerfile 构建 Docker 镜像
                    sh 'docker build -t your_dockerhub_username/jenkins_pipeline:latest .'
                }
            }
        }
        stage('Pytest in Docker') {
            steps {
                script {
                    echo 'Running Pytest in Docker container...'
                    // 运行容器并执行 Pytest 测试
                    sh '''
                        docker run --rm \
                            -v $PWD:/app \
                            -w /app \
                            your_dockerhub_username/jenkins_pipeline:latest \
                            pytest --maxfail=1 --disable-warnings --cov=src src/tests/ --html=report.html
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to production...'
                    // 部署到生产环境的步骤
                    // 在这里添加你的部署脚本（例如，推送镜像到生产、部署到服务器等）
                    // 例如：sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
    post {
        success {
            echo 'Build succeeded!'
            // Archive the HTML report
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            // Publish HTML report (ensure you have the HTML Publisher Plugin installed)
            publishHTML(target: [
                reportName: 'pytest HTML Report',
                reportDir: '.',
                reportFiles: 'report.html',
                alwaysLinkToLastBuild: true,
                keepAll: true,
                allowMissing: false
            ])
        }
        failure {
            echo 'Build failed!'
            // Actions to perform on failure
        }
        always {
            echo 'Cleaning up after pipeline run...'
            // 清理任何中间步骤，停止并移除 Docker 容器等
            sh 'docker system prune -af'
        }
    }
}
