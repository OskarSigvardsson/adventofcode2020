
my @parts = "test.txt".IO.slurp.split("\n\n")>>.trim>>.split("\n");

my Int @ticket = @parts[1][1].split(",")>>.Int;
my @nearby = @parts[2][1..*]>>.split(",").map(*>>.Int);
my @ranges = @parts[0]
	.map(* ~~ /(\d+) '-' (\d+) ' or ' (\d+) '-' (\d+)/)
	.map({ ($0..$1, $2..$3) })
    .reduce({ |$^a, |$^b });
	
say @ticket;
say @nearby;
say @ranges;

say @nearby.reduce({ |$^a, |$^b }).grep(!(* ~~ @ranges.any)).sum;

my @valid = @nearby.grep({ $^a.grep(!(* ~~ @ranges.any)).elems > 0});

say @valid.map(-> @ns {
				say @ns
	# @ns.map(-> $n {
	# 	zip(1..*, @ranges).grep(-> $i, $r {
	# 			say $n;
	# 		if $n ~~ $r { $i }
	# 	})
	# })
});
