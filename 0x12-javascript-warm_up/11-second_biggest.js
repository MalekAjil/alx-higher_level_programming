#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = 0;
  let smax = 0;
  for (let i = 2; i < process.argv.length; i++) {
    const x = parseInt(process.argv[i]);
    if (x > smax) {
      smax = x;
    }
    if (smax > max) {
      const t = max;
      max = smax;
      smax = t;
    }
  }
  console.log(smax);
}
