#!/bin/perl

# Get file name
my $zipfile = $ARGV[0];
my $resname = $zipfile;
$resname =~ s/.zip/.pdf/;
# Send command to bash
my $num = 100000;
my $output;

while ($num < 1000000) {
	$output = `7za e $zipfile -p $num`;
	# Check if extraction were successful
	print $num . "\n";
	if (-e $resname) {
		print "Success with $num\n";
		last;
	} else {
		$num++;
	}
}

