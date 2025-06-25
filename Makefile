.PHONY: Build

deploy-infra:
	aws-vault exec bhavik -- sam build && \
	aws-vault exec bhavik --no-session -- sam deploy --guided

deploy-lambda:
	aws-vault exec bhavik -- sam build --template templateLambda.yaml && \
	aws-vault exec bhavik --no-session -- sam deploy --template templateLambda.yaml --stack-name resume-cloud-lambda --guided

deploy-site:
	aws-vault exec bhavik --no-session -- aws s3 sync ./resume-website s3://resume-cloud-project-website

copy-lambda-function:
	aws-vault exec bhavik --no-session -- aws s3 cp ./resume_function/resume_function.zip s3://resume-cloud-project-website

delete-infra:
	aws-vault exec bhavik -- sam delete --stack-name resume-cloud-project

delete-lambda-infra:
	aws-vault exec bhavik -- sam delete --stack-name resume-cloud-lambda

dynamodb-initial:
	aws-vault exec bhavik -- aws dynamodb batch-write-item --request-items file://dynamodb-initial.json