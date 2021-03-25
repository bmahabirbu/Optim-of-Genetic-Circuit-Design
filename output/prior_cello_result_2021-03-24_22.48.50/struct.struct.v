module struct (input a, b, c, output x);

	wire \$n7_0;
	wire \$n8_0;
	wire \$n9_0;
	wire \$n5_0;
	wire \$n6_0;

	not (\$n6_0, b);
	not (\$n5_0, c);
	nor (\$n8_0, \$n5_0, \$n6_0);
	not (\$n9_0, \$n8_0);
	not (\$n7_0, a);
	nor (x, \$n7_0, \$n9_0);

endmodule
