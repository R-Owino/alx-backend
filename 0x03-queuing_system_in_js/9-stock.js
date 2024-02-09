import redis from 'redis';
import { promisify } from 'util';

// create express server listening on port 1245
const express = require('express');
const app = express();
const port = 1245;

// create a redis client to connect to the server
const client = redis.createClient();

// create an array listProducts
const listProducts = [
  { itemId: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { itemId: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { itemId: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { itemId: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

// create a function getItemByID
function getItemById(id) {
  return listProducts.filter((product) => product.itemId == id)[0];
}

// create a route GET /list_products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// create a function reserveStockById
async function reserveStockById(itemId, stock) {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(`item.${itemId}`, stock);
}

// create a function getCurrentReservedStockById
async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

// create a route GET /list_products/:itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) {
    await reserveStockById(itemId, product.stock);
    product.currentQuantity = product.stock;
  } else product.currentQuantity = currentStock;
  res.json(product);
});

// create a route GET /reserve_product/:itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId)

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const  currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock === null) {
    await reserveStockById(itemId, product.initialAvailableQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  } else if (currentStock > 0) {
    await reserveStockById(itemId, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId });
  } else res.json({ status: 'Not enough stock available', itemId })
});

app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});
