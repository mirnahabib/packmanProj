const Item = require('../models/Item');
const { StatusCodes } = require('http-status-codes');
const path = require('path');
const {spawn} = require("child_process");

const categorizedWebsites = new Map([
    ["electronics" ,  "./fetching/electronicsFetch.py"],
    ["grocery" , "./fetching/groceryFetch.py"],
    ["clothingMen" , "./fetching/clothesFetch.py"],
    ["clothingWomen" , "./fetching/clothesFetchW.py"],
    ["other" , "./fetching/allFetch.py"],
    ["cosmetics" , "./fetching/cosmeticsFetch.py"],
    ["videogames" , "./fetching/videogamesFetch.py"],
    ["toys" , "./fetching/toysFetch.py"],
    ["furniture" , "./fetching/furnitureFetch.py"],
    ["used", "./fetching/usedFetch.py"]

])


async function fetchWebsite(category, searchQuery) {
return new Promise((resolve, reject) => {
    const script = spawn('python', [path.join(__dirname, categorizedWebsites.get(category)), searchQuery]);

    script.stdout.on('data', (data) => {
    resolve(data.toString());
    });

    script.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
    reject(new Error(`Python script error: ${data}`));
    });

    script.on('close', (code) => {
    if (code !== 0) {
        reject(new Error(`Python script exited with code ${code}`));
    }
    //resolve();
    });
});
}


const crawlbyCategory = async (req, res) => {
    const { search: search = 'playstation 5', cat: category = 'general' } = req.params;
    fetchWebsite(category, search)
    .then((result) => {
        //console.log(result);
        jsonresult = JSON.parse(result);
        jsonresult.sort(() => Math.random() - 0.5);
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
        shopsResult = JSON.parse(results[1]);
        usedResult = JSON.parse(results[0]);
        const jsonresult = usedResult.concat(shopsResult);
        jsonresult.sort(() => Math.random() - 0.5);
        //console.log(JSON.stringify(jsonresult));
        res.status(StatusCodes.OK).json({ jsonresult});
    })
    .catch((error) =>{
        console.log('CrawlbycategoryandUsed method error: ' + error);
    });  
}


module.exports = {crawlbyCategory, crawlbyCategoryandUsed};
