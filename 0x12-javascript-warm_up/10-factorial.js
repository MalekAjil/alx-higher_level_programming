#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial(x) {
  if (x <= 1) {
    return(1);
  } else {
    return(x * factorial(x - 1));
  }
}
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
