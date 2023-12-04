import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodeBuildStep, CodePipelineSource, ShellStep
from my_pipeline.my_pipeline_app_stage import MyPipelineAppStage
import os
from dotenv import load_dotenv
from aws_cdk.pipelines import ManualApprovalStep

load_dotenv()
class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                        pipeline_name="CdkTreyTestPipeline",
                        synth=ShellStep("Synth",
                            input=CodePipelineSource.git_hub("lwfletch/cdk-test-pipeline", "main"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]
                        )
                    )
        
        pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account=os.environ.get('CDK_DEFAULT_ACCOUNT'), region="us-east-1")))
        
        # pipeline.add_pre(CodeBuildStep("unit tests", {
        #     commands: [
        #         "pytest -v"
        #     ]
        # }))
        

        testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "staging",
            env=cdk.Environment(account=os.environ.get('CDK_DEFAULT_ACCOUNT'), region="us-east-1")))

        testing_stage.add_pre(ManualApprovalStep('approval'))
        