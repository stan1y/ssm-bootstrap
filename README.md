# AWS SSM Parameter Store bootstraping for ECS Tasks
## Secrets management for Docker containers without volume mounts.

Automatically expose your AWS SSM Parameter Store settings to ECS tasks regardless of the runtime.

## SSM Bootstrap for ECS Services

See [blog post](www.endlessinsomnia.com/post/ssm-bootstrap) for usage and description and 
refer [example](tree/master/example) for how to use it in your infrastructure.


### :octocat: Build docker image

Use base image with SSM bootstrap to build your service image.

```Dockerfile
FROM stan1y/ssm-bootstrap:node-alpine-latest
...
...
```

### :hammer: Setup AWS ECS 

Configure ECS task definition to be executed on a ECS cluster.

```yaml
ExampleTask:
    Type: AWS::ECS::TaskDefinition
    Properties:
        ContainerDefinitions:
            - Name: example-service # The name of the service 
              Image: ...
              Essential: true
              PortMappings:
                - ContainerPort: 8080
              ...

ExampleCluster:
    Type: AWS::ECS::Cluster
    Properties:
        ClusterName: example-cluster # The name of the ECS cluster for parameter names

ExampleService:
    Type: AWS::ECS::Service
    Properties:
        TaskDefinition: !Ref ExampleTask
        Cluster: !Ref ExampleCluster
        ...
```

### :shipit: Setup AWS EC2 Parameter Store

Put your configuration settings into SSM, encrypt as needed.

```
$ aws ssm put-parameter --type String --name /example-cluster/GLOBAL_VAR --value "The Global"
$ aws ssm put-parameter --type SecureString --name /example-cluster/example-service/THE_SECRET --value "Bananas"
```

### :unicorn: Auto-Magic

Your container's environment would be populated with variables `GLOBAL_VAR` and `THE_SECRET` when
you run your image on ECS EC2 host.

