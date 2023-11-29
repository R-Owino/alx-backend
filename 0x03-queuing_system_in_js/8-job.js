/* Contains a function createPushNotificationsJobs */

import kue from 'kue';
const queue = kue.createQueue();

function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  jobs.forEach(function (job) {
    const jobCreated = queue.create('push_notification_code_3', job).save((err) => {
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
}

module.exports = createPushNotificationsJobs;
