from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
import os
from dotenv import load_dotenv
from aws_cdk.pipelines import ManualApprovalStep

load_dotenv()
env = os.environ.get('CDK_ENV')
from constructs import Construct

class PythonCdkLambdaTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'ft_gamification_docebo_awarded_badges_insert_{0}'.format(env),
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambdas'),
            handler='ft_gamification_docebo_awarded_badges_insert.lambda_handler',
        )
        
        my_lambda = _lambda.Function(
            self, 'ft_gamification_badge_aug_{0}'.format(env),
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambdas'),
            handler='ft_gamification_badge_aug.lambda_handler',
        )
        
        my_lambda = _lambda.Function(
            self, 'ft_gamification_badge_update_{0}'.format(env),
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambdas'),
            handler='ft_gamification_badge_update.lambda_handler',
        )
        