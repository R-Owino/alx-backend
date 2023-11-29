import redis from 'redis';
import { promisify } from 'util';

// 1. create an array listProducts
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// 2. create a function getItemByID
function getItemByID (id) {
  const item = listProducts.find(item => item.id === id);
  return item;
}

// 3. create express server listening on port 1245
const express = require('express');
const app = express();
const port = 1245;

// 4. create a route GET /list_products
app.get('/list_products', (req, res) => {
  res.send(listProducts);
});

// 5. create a redis client to connect to the server
const client = redis.createClient();

// promisify the redis client get/set methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// create a function reserveStockById
function reserveStockById (id, stock) {
  return setAsync(`item.${id}`, stock);
}

// create a function getCurrentReservedStockById
async function getCurrentReservedStockById (id) {
  const stock = await getAsync(`item.${id}`);
  return stock;
}

// 6. create a route GET /list_products/:itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemByID(itemId);
  const currentReservedStock = await getCurrentReservedStockById(itemId);
  if (item) {
    item.reservedStock = currentReservedStock;
    res.send(item);
  } else {
    res.status(404).send({ status: 'Product not found' });
  }
});

// 7. create a route GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemByID(itemId);
  const currentReservedStock = await getCurrentReservedStockById(itemId);
  if (item) {
    if (item.stock > currentReservedStock) {
      reserveStockById(itemId, Number(currentReservedStock) + 1);
      res.send({ status: 'Reserved' });
    } else {
      res.send({ status: 'Not enough stock available' });
    }
  } else {
    res.status(404).send({ status: 'Product not found' });
  }
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
