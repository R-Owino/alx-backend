/* Create a queue with Kue
 * Loop thru the array of jobs and does the following for each object:
  * Create a new job to the queue push_notification_code_2 with the current object
  * Log to the console `Notification job created: JOB_ID` on no error
  * Log to the console `Notification job JOB_ID completed` on job completion
  * Log to the console `Notification job JOB_ID failed: ERROR_MESSAGE` on job failure
  * Log to the console `Notification job JOB_ID ${progress}% complete` on job progress
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
  jobCreated.on('enqueue', () => {
    console.log(`Notification job created: ${jobCreated.id}`);
  }).on('complete', (result) => {
    console.log(`Notification job #${jobCreated.id} completed`);
  }).on('failed', (errorMessage) => {
    console.log(`Notification job #${jobCreated.id} failed: ${errorMessage}`);
  }).on('progress', (progress) => {
    console.log(`Notification job #${jobCreated.id} ${progress}% complete`);
  });
});
