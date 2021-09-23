int: max=180;

var 1..max: a;
var 1..max: b;
var 1..max: c;
constraint a+b+c = 180;
constraint 360 mod a = 0;
constraint 360 mod b = 0;
constraint 360 mod c = 0;
constraint a <= b /\ b <= c;

solve satisfy;

