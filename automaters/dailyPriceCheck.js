function runDailyFunction() {
    // Your code here
  }
  
  function scheduleDailyFunction() {
    const now = new Date();
    const millisTill6pm = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 18, 0, 0, 0) - now;
    if (millisTill6pm < 0) {
        millisTill6pm += 86400000; // it's after 6pm, try 6pm tomorrow.
    }
    setTimeout(function(){
      runDailyFunction();
      setInterval(runDailyFunction, 24 * 60 * 60 * 1000); // repeat every 24 hours
    }, millisTill6pm);
  }
  
  module.exports = scheduleDailyFunction;