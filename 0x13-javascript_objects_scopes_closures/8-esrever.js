#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev[i] = list[list.length - 1 - i];
  }
  return rev;
};
