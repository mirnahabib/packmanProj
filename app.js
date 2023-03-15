const express = require('express')
const {items} = require('./data')
const app = express();

app.get('/', (req, res) => {
  console.log('client request received')
  res.status(200).send('Home Page')
})

app.get('/api/v1/query', (req, res) => {
  console.log(req.query)
  const { search } = req.query
  let sortedItems = [...items]

  if (search) {
    sortedItems = sortedItems.filter((item) => {
      return item.name.includes(search)
    })
    if (sortedItems.length < 1) {
      return res.status(200).send('no products matched your search');
    }
  }
  res.status(200).json(sortedItems)
})

app.get('/about', (req, res) => {
  res.status(200).send('About Page')
})

app.all('*', (req, res) => {
  res.status(404).send('<h1>404 Not Found!</h1>')
})

app.listen(5000, () => {
  console.log('server is listening on port 5000...')
})
