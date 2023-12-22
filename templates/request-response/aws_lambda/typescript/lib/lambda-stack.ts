import { Duration, Stack, StackProps } from "aws-cdk-lib";
import { Function, Runtime, Code } from "aws-cdk-lib/aws-lambda";
import { RestApi, LambdaIntegration } from "aws-cdk-lib/aws-apigateway";
import { Construct } from "constructs";
import { join } from "path";

export class LambdaStack extends Stack {
	constructor(scope: Construct, id: string, props?: StackProps) {
		super(scope, id, props);

		const lambda = new Function(this, "HelloLambdaFunction", {
			runtime: Runtime.NODEJS_18_X,
			code: Code.fromAsset(join(__dirname, "../src/")),
			handler: "hello-function.hello",
		});

		const apiGateway = new RestApi(this, "HelloApi", {});

		let apiResourcePath = apiGateway.root.addResource("api");

		apiResourcePath.addMethod("GET", new LambdaIntegration(lambda));
	}
}
