
my @lines = "input.txt".IO.lines;

# @lines.map({
# 	if $^a ~~ / (\d+) '-' (\d+) ' ' (.) ': ' (.*) / {
# 		return $3.comb($2.Str).elems ~~ ($0.Int)..($1.Int);
# 	}
# 	return False
# });

say @lines.map(* ~~ / (\d+) '-' (\d+) ' ' (.) ': ' (.*) /)
	.grep({ $3.comb($2.Str).elems ~~ ($0.Int)..($1.Int) })
	.elems;

say @lines.map(* ~~ / (\d+)'-'(\d+) ' ' (.) ': ' (.*) /)
	.grep({ ($3.substr($0, 1) == $3) != ($3.substr($1, 1) == $3) })
	.elems;


