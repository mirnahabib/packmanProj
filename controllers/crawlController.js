const Item = require('../models/Item');
const { StatusCodes } = require('http-status-codes');
const path = require('path');
const {spawnSync} = require("child_process");

const categorizedWebsites = new Map([
    ["general" ,  "./fetching/generalFetch.py"],
    ["grocery" , "./fetching/groceryFetch.py"],
    ["clothes" , "./fetching/clothesFetch.py"],
    ["used", "./fetching/usedFetch.py"]
])


async function fetchWebsite(category, searchQuery) {
    return new Promise((resolve) => {
    const script =  spawnSync("python" ,[path.join(__dirname, categorizedWebsites.get(category)), searchQuery])
    if(script.error){
        console.log('Fetch website error: ' + error);
    }else{
        resolve(script.output.toString());
    }  
    });
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
        console.log('Crawlbycategory method error: ' + error);
    });  

}

const crawlbyCategoryandUsed = async (req, res) => {
    const { search: search, cat: category } = req.params;
    Promise.all([fetchWebsite('used', search), fetchWebsite(category, search)])
    .then(results =>{
        shopsResult = JSON.parse(results[1].slice(1,-1));
        usedResult = JSON.parse(results[0].slice(1,-1));
        const jsonresult = usedResult.concat(shopsResult);
        console.log(JSON.stringify(jsonresult));
        res.status(StatusCodes.OK).json({ jsonresult});
    })
    .catch((error) =>{
        console.log('CrawlbycategoryandUsed method error: ' + error);
    });  
}


module.exports = {crawlbyCategory, crawlbyCategoryandUsed};