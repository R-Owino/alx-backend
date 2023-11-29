/* Adding tests to our job creator */

import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

// enter test mode w/o processing jobs
queue.testMode.enter();

describe('createPushNotificationsJobs', () => {
  // clear queue before each test
  beforeEach(() => {
    queue.testMode.clear();
  });

  // exit test mode and clear queue after each test
  after(() => {
    queue.testMode.exit();
  });

  // test the function
  it('display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('jobs', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    // create jobs
    createPushNotificationsJobs(jobs, queue);

    // check if jobs were created
    const jobsCreated = queue.testMode.jobs;
    jobsCreated.should.have.lengthOf(jobs.length);

    // check if jobs were created with the correct data
    queue.testMode.jobs.forEach((job) => {
      expect(job.type).to.equal('push_notification_code_3');
      expect(job.data).to.equal(jobs[index]);
    });
  });
});
