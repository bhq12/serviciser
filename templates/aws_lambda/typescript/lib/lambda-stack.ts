import { Duration, Stack, StackProps } from "aws-cdk-lib";
import { Effect, PolicyStatement } from "aws-cdk-lib/aws-iam";
import { Function, Runtime, Code } from "aws-cdk-lib/aws-lambda";
import { Queue } from "aws-cdk-lib/aws-sqs";
import { SqsEventSource } from "aws-cdk-lib/aws-lambda-event-sources";
import { Construct } from "constructs";
import { join } from "path";

export class LambdaStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props);

		const queue = new Queue(this, "LambdaQueue", {
			visibilityTimeout: Duration.seconds(300),
		});

		const lambda = new Function(this, "HelloLambdaFunction", {
			runtime: Runtime.NODEJS_18_X,
			code: Code.fromAsset(join(__dirname, "../src/")),
			handler: "hello-function.hello",
		});

		const queueEventSource = new SqsEventSource(queue);

		lambda.addEventSource(queueEventSource);

		lambda.addToRolePolicy(new PolicyStatement({
			effect: Effect.ALLOW,
			actions: ['sqs:ReceiveMessage', 'sqs:DeleteMessage'],
			resources: [queue.queueArn]
		}));


	}
}
