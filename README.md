
# cdk-ec2-cheap

This project deploys a single AWS EC2 instance. It creates a VPC with one public subnet to remove the need for a NAT instance. It also adds the necessary SSM configuration to be able to connect to the instance.

### Prerequisites
cdk

poetry (requirements.txt is provided for pip install)

awscli (to connect to instance)

## Use
Simply update `USERDATA` and `INSTANCE_TYPE` in [ec2_cheap/stack.py](ec2_cheap/stack.py) and then run `cdk deploy`

In roughly 3-4 minutes, the stack will complete and output the SSM command to connect to your instance.
```
...snip...
 ✅  EC2Stack

✨  Deployment time: 201.8s

Outputs:
EC2Stack.SSMConnect = aws ssm start-session --target i-0a75fb4f9798ca3d5
...snip...
```

## Remove
`cdk destroy`

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

#### Resources Created
```
AWS::CDK::Metadata
AWS::EC2::Instance
AWS::EC2::InternetGateway
AWS::EC2::Route
AWS::EC2::RouteTable
AWS::EC2::SecurityGroup
AWS::EC2::Subnet
AWS::EC2::SubnetRouteTableAssociation
AWS::EC2::VPC
AWS::EC2::VPCGatewayAttachment
AWS::IAM::InstanceProfile
AWS::IAM::Policy
AWS::IAM::Role
AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
AWS::SSM::Parameter::Value<String>
```