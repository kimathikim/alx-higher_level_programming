#!/usr/bin/node

const Leng = process.argv;
if (Leng.length < 3) {
  console.log('No arguments');
} else if (Leng.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
