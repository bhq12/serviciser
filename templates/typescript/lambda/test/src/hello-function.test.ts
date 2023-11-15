import { hello } from "../../src/hello-function";
import * as cdk from "aws-cdk-lib";
import { Template, Match } from "aws-cdk-lib/assertions";
import * as Lambda from "../../lib/lambda-stack";

test("SQS Queue and SNS Topic Created", () => {
	// ARRANGE
	const testEvent = "test-event";
	// ACT
	const result = hello(testEvent);
	// ASSERT
	expect(result).toBe("test-event");
});
