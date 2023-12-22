export function hello(event: string) {
	console.log(`Received event: ${JSON.stringify(event)}`);
	return event;
}
