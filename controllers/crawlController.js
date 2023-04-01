const Item = require('../models/Item');
const { StatusCodes } = require('http-status-codes');
const path = require('path');
const {spawn, spawnSync} = require("child_process");

const websites = new Map([
    ["amazon" ,  "./fetching/amazon.py"],
    ["jumia" , "./fetching/jumia.py"],
    ["noon" , "./fetching/noon.py"],
    ["select" , "./fetching/_select.py"],
    ["olx" , "./fetching/olx.py"],
    ["carrefour" , "./fetching/carrefour.py"],
    ["spinney" , "./fetching/spinney.py"],
    ["hyperone" , "./fetching/hyperone.py"],
    ["gourmet" , "./fetching/gourmet.py"],
    ["max" , "./fetching/max.py"],
    ["h&m" , "./fetching/h&m.py"],
    ["bershka" , "./fetching/bershka.py"],
    ["zara" , "./fetching/zara.py"]
])



async function fetchWebsite(website, searchQuery) {
    const script =  spawnSync("python" ,[path.join(__dirname, websites.get(website)), searchQuery])
    if(script.error){
        console.log(error);
    }else{
        return script.output.toString();
    }  
}

const crawl = async (req, res) => {
    const { search: search= 'playstation', cat: category = 'amazon' } = req.params;
    fetchWebsite(category, search)
    .then((result) => {
        console.log(result + ' method crawl');
        res.status(StatusCodes.OK).json({ result });
    })
    .catch((error) =>{
        console.log(error);
    });  
}

module.exports = {crawl};