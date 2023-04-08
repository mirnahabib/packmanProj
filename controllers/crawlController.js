const Item = require('../models/Item');
const { StatusCodes } = require('http-status-codes');
const path = require('path');
const {spawnSync} = require("child_process");

const categorizedWebsites = new Map([
    ["general" ,  "./fetching/generalFetch.py"],
    ["grocery" , "./fetching/groceryFetch.py"],
    ["clothes" , "./fetching/clothesFetch.py"]
])


async function fetchWebsite(category, searchQuery) {
    const script =  spawnSync("python" ,[path.join(__dirname, categorizedWebsites.get(category)), searchQuery])
    if(script.error){
        console.log('fetch website error ' + error);
    }else{
        return script.output.toString();
    }  
}

const crawlbyCategory = async (req, res) => {
    const { search: search = 'playstation 5', cat: category = 'general' } = req.params;
    fetchWebsite(category, search)
    .then((result) => {
        console.log(result);
        result = result.slice(1,-1);
        jsonresult = JSON.parse(result);
        res.status(StatusCodes.OK).json({ jsonresult});
    })
    .catch((error) =>{
        console.log('crawl method error: ' + error);
    });  

}



module.exports = {crawlbyCategory};