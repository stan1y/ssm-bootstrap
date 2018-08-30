# Example service for ssm-bootstrap

This is an simplistic example of ssm-bootstrap functionality. 
`Dockerfile` will build a simple web app listening on 8080 and displaying it's
current environment variables and list of files in the `/app` folder.

# Storing settings in AWS SSM for example service

To prepare settings for the example service you need to know a ECS cluster name.
With the name know you can build a path to the environment variables settings for
the example service. The service can be configured to use any `ContainerName` but
in the examples below it is assumed that service name is **example-service** and 
cluster name is **example-cluster**. You need to substitute your values for the 
commands below to configure SSM.

    $ aws ssm put-parameter --type SecureString \
        --name /example-cluster/example-service/DB_CONN \
        --value "SERVER=example.com;SSL=true;SSLMode=require;DATABASE=mydb;UID=wikiuser;PWD=SeCrEt!"

The SSM bootstrap code needs access to the ECS container metadata file. It must be enabled in the `ecs.config` on your ECS instances. The ECS tasks using SSM bootstrap must have SSM and potentially KMS functions allowed their roles. KMS access would require grants to access to encryption keys used for parameter values.
