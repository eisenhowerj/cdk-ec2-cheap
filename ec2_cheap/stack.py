from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

INSTANCE_TYPE = "c5.xlarge"
USERDATA = """
#!/bin/bash

echo "Hello"
"""


class EC2Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
            self,
            "CheapVPC",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="cheap-public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24
                )
            ],
            max_azs=1,
        )

        ssm_role = iam.Role(
            self,
            "SSMRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )
        ssm_role.add_to_policy(
            iam.PolicyStatement(
                resources=["*"],
                actions=[
                    "ssmmessages:*",
                    "ssm:UpdateInstanceInformation",
                    "ec2messages:*",
                ],
            )
        )

        instance = ec2.Instance(
            self,
            "CheapEC2",
            allow_all_outbound=True,
            instance_name="cheap-instance",
            instance_type=ec2.InstanceType(INSTANCE_TYPE),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            role=ssm_role,
            user_data=ec2.UserData.for_linux(shebang=USERDATA),
            vpc=vpc,
        )

        CfnOutput(
            self,
            "SSMConnect",
            description="AWS CLI command to connect to instance",
            value=f"aws ssm start-session --target {instance.instance_id}",
        )
