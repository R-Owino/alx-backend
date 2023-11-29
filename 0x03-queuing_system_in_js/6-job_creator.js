/* Creating a queue with Kue */

import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234556789',
    message: 'Wassup!',
};

// Create a queue and add a job to it
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

// Listen for job completion
job.on('complete', () => console.log('Notification job completed'));

// Listen for job failure
job.on('failed', () => console.log('Notification job failed'));
