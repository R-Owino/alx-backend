/* Displays success message on connect to redis client
 * Displays error message on error
 * Subscribes to channel 'holberton school channel'
 * Displays message when it receives message on channel
 * If message is KILL_SERVER, it should unsubscribe and quit
 */

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
    console.log(message);
});
