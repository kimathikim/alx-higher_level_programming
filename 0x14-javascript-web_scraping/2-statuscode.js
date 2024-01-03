#!/usr/bin/node
/**
 * This script makes an HTTPS GET request to a specified URL and logs the response code.
 */

const https = require('https');
const args = process.argv.slice(process.argv.length - 1);

https
  .get(args[0], (res) => {
    console.log('code: '.concat(res.statusCode));
  })
  .on('error', (err) => {
    console.log('code: '.concat(err.statusCode));
  });
