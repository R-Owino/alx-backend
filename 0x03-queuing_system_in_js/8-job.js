/* Contains a function createPushNotificationsJobs */

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
      const job = queue.create('push_notification_code_3', jobData)
          .on('complete', function() {
              console.log(`Notification job ${this.id} completed`);
          })
          .on('failed', function(errorMessage) {
              console.log(`Notification job ${this.id} failed: ${errorMessage}`);
          })
          .on('progress', function(progress) {
              console.log(`Notification job ${this.id} ${progress}% complete`);
          });

      job.save((err) => {
          if (!err) console.log(`Notification job created: ${job.id}`);
      });
  });
}

module.exports = createPushNotificationsJobs;
