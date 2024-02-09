import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

// create express server listening on port 1245
const express = require('express');
const app = express();
const port = 1245;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;

// create a function reserveSeat
async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

// create a function getCurrentAvailableSeats
async function getCurrentAvailableSeats() {
    const availableSeats = await getAsync('available_seats');
    return availableSeats;
}

const queue = kue.createQueue();

// create a route GET /reserve_seat
app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: availableSeats });
});

// create a route GET /reserve_seat
app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' });
        return;
    }

    const job = queue.create('reserve_seat', {}).save((err) => {
        if (!err) res.json({ status: 'Reservation in process'});
        else res.json({ status: 'Reservation failed' });
    });

    job.on('complete', () => {
        console.log(`Seat reservation job #${job.id} completed`);
    }).on('failed', () => {
        console.log(`Seat reservation job #${job.id} failed: ${err}`);
    });
});

//
app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        let availableSeats = await getCurrentAvailableSeats();
        availableSeats--;
        if (availableSeats >= 0) {
            await reserveSeat(availableSeats);
            done();
        } else {
            done(new Error('Not enough seats available'));
        }

        if (availableSeats === 0) {
            reservationEnabled = false;
        }
    });
    res.json({ status: 'Queue processing' });
});

app.listen(port, async () => {
    console.log(`app listening at http://localhost:${port}`);
    await reserveSeat(50);
});