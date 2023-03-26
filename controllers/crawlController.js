const Item = require('../models/Item');
const { StatusCodes } = require('http-status-codes');
const path = require('path');
const {spawn} = require("child_process");

const websites = new Map([
    ["amazon" ,  "./fetching/amazon.py"],
    ["Jumia" , "./fetching/jumia.py"],
    ["Noon" , "./fetching/noon.py"],
    ["Select" , "./fetching/_select.py"],
    ["Olx" , "./fetching/olx.py"],
    ["Carrefour" , "./fetching/carrefour.py"],
    ["Spinney" , "./fetching/spinney.py"],
    ["Hyperone" , "./fetching/hyperone.py"],
    ["Gourmet" , "./fetching/gourmet.py"],
    ["Max" , "./fetching/max.py"],
    ["H&M" , "./fetching/h&m.py"],
    ["Bershka" , "./fetching/bershka.py"],
    ["Zara" , "./fetching/zara.py"]
])



async function fetchWebsite(website, searchQuery) {
    const script =  spawn("python" ,[path.join(__dirname, websites.get(website)), searchQuery])
    console.log("fetch website has been called " + websites.get(website) + searchQuery);    
    script.stdout.on('data' , (data) =>{
        dataJson = data.toString()
        console.log(dataJson);
    })
    script.on('close',(code) =>{
        console.log(`ended ${website} ${code}`);
    })
    
}

const crawl = async (req, res) => {
    const { search: search= 'playstation', cat: category = 'amazon' } = req.params;
    const result = await fetchWebsite(category, search);
    console.log(result);


    
    res.status(StatusCodes.OK).json({ result });
}

module.exports = {crawl};