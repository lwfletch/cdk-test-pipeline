#!/usr/bin/env python3
import aws_cdk as cdk
from my_pipeline.my_pipeline_stack import MyPipelineStack
import os
from dotenv import load_dotenv

load_dotenv()

app = cdk.App()
MyPipelineStack(app, "TreyPipelineStack",
    env=cdk.Environment(account=os.environ.get('CDK_DEFAULT_ACCOUNT'), region="us-east-1")
)

app.synth()
