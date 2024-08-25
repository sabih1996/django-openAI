from aws_cdk import (
    core,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ecr as ecr
)

class EcsServiceStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, cluster: ecs.Cluster, repository: ecr.Repository, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define Task Definition
        task_definition = ecs.FargateTaskDefinition(self, "DjangoAppTaskDef")

        # Add Container
        container = task_definition.add_container(
            "DjangoAppContainer",
            image=ecs.ContainerImage.from_ecr_repository(repository),
            environment={"DJANGO_SETTINGS_MODULE": "config.settings.production"}
        )
        container.add_port_mappings(ecs.PortMapping(container_port=8000))

        # Define Fargate Service with ALB
        ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "DjangoAppFargateService",
            cluster=cluster,
            task_definition=task_definition
        )
