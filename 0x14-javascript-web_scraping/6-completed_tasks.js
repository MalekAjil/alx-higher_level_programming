#!/usr/bin/node
const request = require('request');

function starwarsCount (url) {
  request(url, (err, res, content) => {
    if (err) {
      console.error(`Error: ${err.message}`);
    } else if (res.statusCode === 200) {
      const tasksList = JSON.parse(content);
      const userCompleted= {};
      tasksList.forEach((task) => {
	if (task.completed) {
          const uId = task.userId;
	  userCompleted[uId] = (userCompleted[uId] || 0) + 1;
        }
      });
      console.log(userCompleted);
    } else {
      console.error(`Error: ${res.statusCode}`);
    }
  });
}

const url = process.argv[2];
starwarsCount(url);
