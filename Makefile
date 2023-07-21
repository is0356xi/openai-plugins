default:
	echo "Please use 'make gen' for generating the schemas"

gen:
	datamodel-codegen --input openapi.yaml --input-file-type openapi --output schemas.py