#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let x = 0; x < list.length; x++) {
    revList[x] = list[list.length - 1 - x];
  }
  return revList;
};
