my @nums = "input.txt".IO.slurp.lines>>.Int;

say @nums.combinations(2).grep(*.sum == 2020).[0].reduce({$^a * $^b});
say @nums.combinations(3).grep(*.sum == 2020).[0].reduce({$^a * $^b});
