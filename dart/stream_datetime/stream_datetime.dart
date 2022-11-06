import 'dart:io';

mystream () async *{
	while (true) {
		yield "${DateTime.now().toLocal()}";
		sleep(Duration(seconds:1));
	}
}

void main() {
	mystream().listen((value) {
		print(value);
	});
}
