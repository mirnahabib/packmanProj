const {spawn} = require("child_process")

const websites = new Map([
    ["Amazon" , "./fetching/amazon.py"],
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


async function fetchWebsite(website,searchQuery) {
    const script =  spawn("python3" ,[websites.get(website),searchQuery])
        
    script.stdout.on('data' , (data) =>{
        dataJson = data.toString()
        console.log(dataJson);
    })
    script.on('close',(code) =>{
        console.log(`ended ${website} ${code}`);
    })
    
}


fetchWebsite("Amazon", "playstation 5")
fetchWebsite("Jumia", "playstation 5")
// fetchWebsite("Noon", "playstation 5")
// fetchWebsite("Olx", "playstation 5")
// fetchWebsite("Carrefour" , "chocolate")
// fetchWebsite("Max","jacket")
// fetchWebsite("H&M","jacket")
// fetchWebsite("Zara","jacket")


