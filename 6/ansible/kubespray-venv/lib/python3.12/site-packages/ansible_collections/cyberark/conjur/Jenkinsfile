#!/usr/bin/env groovy

pipeline {
  agent { label 'executor-v2' }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '30'))
  }

  triggers {
    cron(getDailyCronString())
  }

  stages {
    stage('Validate') {
      parallel {
        stage('Changelog') {
          steps { parseChangelog() }
        }
      }
    }

    stage('Run conjur_variable unit tests') {
      steps {
        sh './dev/test_unit.sh -r'
        publishHTML (target : [allowMissing: false,
          alwaysLinkToLastBuild: false,
          keepAll: true,
          reportDir: 'tests/output/reports/coverage=units/',
          reportFiles: 'index.html',
          reportName: 'Ansible Coverage Report',
          reportTitles: 'Conjur Ansible Collection report'])
      }
    }

    stage('Run integration tests with Conjur Open Source') {
      stages {
        stage('Ansible v8 (core 2.15) - latest') {
          stages {
            stage('Deploy Conjur') {
              steps {
                sh './dev/start.sh -v 8'
              }
            }
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    sh './ci/test.sh -d -t conjur_variable'
                    junit 'tests/conjur_variable/junit/*'
                  }
                }

                stage('Testing conjur_host_identity role') {
                  steps {
                    sh './ci/test.sh -d -t conjur_host_identity'
                    junit 'roles/conjur_host_identity/tests/junit/*'
                  }
                }
              }
            }
          }
        }

        stage('Ansible v7 (core 2.14)') {
          when {
            anyOf {
              branch 'main'
              buildingTag()
            }
          }
          stages {
            stage('Deploy Conjur') {
              steps {
                sh './dev/start.sh -v 7'
              }
            }
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    sh './ci/test.sh -d -t conjur_variable'
                    junit 'tests/conjur_variable/junit/*'
                  }
                }

                stage('Testing conjur_host_identity role') {
                  steps {
                    sh './ci/test.sh -d -t conjur_host_identity'
                    junit 'roles/conjur_host_identity/tests/junit/*'
                  }
                }
              }
            }
          }
        }

        stage('Ansible v6 (core 2.13)') {
          when {
            anyOf {
              branch 'main'
              buildingTag()
            }
          }
          stages {
            stage('Deploy Conjur') {
              steps {
                sh './dev/start.sh -v 6'
              }
            }
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    sh './ci/test.sh -d -t conjur_variable'
                    junit 'tests/conjur_variable/junit/*'
                  }
                }

                stage('Testing conjur_host_identity role') {
                  steps {
                    sh './ci/test.sh -d -t conjur_host_identity'
                    junit 'roles/conjur_host_identity/tests/junit/*'
                  }
                }
              }
            }
          }
        }
      }
    }

    stage('Run integration tests with Conjur Enterprise') {
      stages {
        stage('Deploy Conjur Enterprise') {
          steps {
            sh './dev/start.sh -e -v 8'
          }
        }
        stage('Run tests') {
          parallel {
            stage("Testing conjur_variable lookup plugin") {
              steps {
                sh './ci/test.sh -d -t conjur_variable'
                junit 'tests/conjur_variable/junit/*'
              }
            }

            stage("Testing conjur_host_identity role") {
              steps {
                sh './ci/test.sh -d -t conjur_host_identity'
                junit 'roles/conjur_host_identity/tests/junit/*'
              }
            }
          }
        }
      }
    }

    stage('Build Release Artifacts') {
      when {
        anyOf {
            branch 'main'
            buildingTag()
        }
      }

      steps {
        sh './ci/build_release'
        archiveArtifacts 'cyberark-conjur-*.tar.gz'
      }
    }

    stage('Publish to Ansible Galaxy') {
      when {
        buildingTag()
      }

      steps {
        sh 'summon ./ci/publish_to_galaxy'
      }
    }
  }

  post {
    always {
      cleanupAndNotify(currentBuild.currentResult)
    }
  }
}