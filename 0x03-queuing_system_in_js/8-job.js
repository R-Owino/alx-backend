/* Contains a function createPushNotificationsJobs */

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  jobs.forEach(function (job) {
    const currentJob = queue.create('push_notification_code_3', job);

    // handle job events using 'once' to ensure they are executed only once
    currentJob.save((err) => {
      if (!err) console.log(`Notification job created: ${currentJob.id}`);
    });

    currentJob.once('enqueue', () => {
      console.log(`Notification job created: ${currentJob.id}`);
    }).once('complete', (result) => {
      console.log(`Notification job #${currentJob.id} completed`);
    }).once('failed', (errorMessage) => {
      console.log(`Notification job #${currentJob.id} failed: ${errorMessage}`);
    }).on('progress', (progress) => {
      console.log(`Notification job #${currentJob.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
