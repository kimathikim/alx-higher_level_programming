#!/usr/bin/node
exports.callMeMobyi = function (x, theFunction) {
  for (let index = x; index > 0; index--) {
    theFunction.call();
  }
};
