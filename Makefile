.PHONY: Build

build:
	sam build

deploy-infra:
	aws-vault exec bhavik --no-session -- sam deploy -- guided

deploy-site:
	aws-vault exec bhavik --no-session -- aws s3 sync ./resume-website s3://resume-cloud-project-website

delete-infra:
	aws-vault exec bhavik sam delete -- stack-name resume-cloud-project