/* Contains array with blacklisted phone numbers
 * Contains function sendNotification
   * If phoneNumber is not blacklisted, it prints a success message to console
   * If phoneNumber is blacklisted, it prints <phoneNumber> is blacklisted
 */

import kue from 'kue';
const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

// Process jobs
queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
