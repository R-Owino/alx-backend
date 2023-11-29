/* Create a queue with Kue
 * Loop thru the array of jobs
 */

import kue from 'kue';
const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// iterate thru jobs array
jobs.forEach(function (job) {
  // create a job
  const jobCreated = queue.create('push_notification_code_2', job).save((err) => {
    if (!err) console.log(`Notification job created: ${jobCreated.id}`);
  });

  // handle job events
  jobCreated.on('enqueue', function (id, type) {
    console.log(`Notification job created: ${jobCreated.id}`);
  }).on('complete', function (result) {
    console.log(`Notification job #${jobCreated.id} completed`);
  }).on('failed', function (errorMessage) {
    console.log(`Notification job #${jobCreated.id} failed: ${errorMessage}`);
  }).on('progress', function (progress, data) {
    console.log(`Notification job #${jobCreated.id} ${progress}% complete`);
  });
});
