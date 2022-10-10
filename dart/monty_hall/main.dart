import 'dart:core';
import 'dart:io';
import 'dart:math';

int zero_count = 0, one_count = 0, two_count = 0;
int guy_a = 0, guy_b = 0, guy_hall = 0;

int pick(List doors) {
	int len	= doors.length;
	if (len > 1) {
		return doors[Random().nextInt(len)];
	} else if (len == 1) {
		return doors[0];
	} else {
		throw Exception ("Doors length is ${len}");
	}
}

void register_award (aw_n) {
	switch (aw_n) {
		case 0: {zero_count++;}
			break;
		case 1: {one_count++;}
			break;
		case 2: {two_count++;}
			break;
		default: {throw Exception('No real award were provided');}
			break;
	}
}

void main(List <String> args) {
	print("Monty Hall Simulation!");
	if (args.length > 0) {
		print("We gonna run it ${args[0]} times");
	} else {
		print("How many executions do you want to?");
	}
	int? deftimes = args.length > 0 ? int.parse(args[0]) : int.parse(stdin.readLineSync()!);
	int turn = 0;
	while (turn < deftimes) {
		//	Sort a door to hold the award
		var possibilities = [0, 1, 2];
		int award = pick(possibilities);
		register_award(award);
		var goats = [0,1,2];
		goats.remove(award);
		//	User A would pick one of three doors
		int a_pref = pick(possibilities);
		possibilities.remove(a_pref);
		goats.remove(a_pref);
		//	Monty Hall reveals one door that is neither picked, nor award		
		int hall_pref = pick(goats);
		possibilities.remove(hall_pref);
		//	User B takes the remaining door
		int b_pref = pick(possibilities);
		//	Prepare for next round
		if (a_pref == award) {
			guy_a++;
		}
		if (b_pref == award) {
			guy_b++;
		}
		if (hall_pref == award) {
			guy_hall++;
			throw Exception ('Hall picked the right one');
		}
		turn++;
	}
	print("Result\tZeros\tOnes\tTwos\n\t${zero_count}\t${one_count}\t${two_count}");
	print("Result\tGuy_A\tGuy_B\tHall\n\t${guy_a}\t${guy_b}\t${guy_hall}");
}
