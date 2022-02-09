import aws_cdk as cdk

from ec2_cheap.stack import EC2Stack

app = cdk.App()
EC2Stack(
    app,
    "EC2Stack",
)

app.synth()
