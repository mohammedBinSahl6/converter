console.log("This little programme will execute a substraction and make a few observations. Let's get started!");

var a = prompt("Please choose a second number A: ");
var b = prompt("Please choose a second number B: ");
var c = a - b;

if (c > 10) {
    console.log("The result is bigger than 10");
}
else if (0 < c < 10) {
   console.log("The result is greater than 0 but not than 10");
}
else if (c == 0) {
    console.log("The result is zero");
} else {
    console.log("The result is a negative number");
}

console.log("You can try again!");