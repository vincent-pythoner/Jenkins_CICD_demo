pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building on branch: ${env.BRANCH_NAME}"
                // 执行构建指令，例如 `mvn clean install`
            }
        }
        stage('Test') {
            steps {
                echo "Running tests on branch: ${env.BRANCH_NAME}"
                // 执行测试指令，例如 `pytest --maxfail=1 --disable-warnings --cov=.`
            }
        }
    }
    post {
        success {
            echo "Build and tests completed successfully."
        }
        failure {
            echo "Build or tests failed!"
        }
    }
}

