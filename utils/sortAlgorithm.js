const { json } = require("express");


function calculateStandardDeviation(numbers, mean) {
    //Calculate the sum of squared differences
    const squaredDifferencesSum = numbers.reduce((sum, num) => {
      const difference = num - mean;
      return sum + (difference * difference);
    }, 0);
  
    //Calculate the variance
    const variance = squaredDifferencesSum / (numbers.length-1);
  
    //Calculate the standard deviation
    const standardDeviation = Math.sqrt(variance);
  
    return standardDeviation;
  }


function calculateHuberMean(data, tuningParameter) {
const sortedData = data.slice().sort((a, b) => a - b);
console.log(sortedData);
const n = sortedData.length;
const median = (n % 2 === 0) ? (sortedData[n/2 - 1] + sortedData[n/2]) / 2 : sortedData[Math.floor(n/2)];
console.log(median);
let sum = 0;
let count = 0;
for (let i = 0; i < n; i++) {
    const residual = Math.abs(sortedData[i] - median);
    console.log(residual);
    if (residual <= tuningParameter) {
    sum += sortedData[i];
    count++;
    } else {
    sum += (tuningParameter * Math.sign(sortedData[i] - median));
    count++;
    }
}
console.log(sum + " " + count);
return sum / count;
}
  
function calculateMean(prices){
    const mean = prices.reduce((sum, num) => sum + num, 0) / prices.length;
    return mean;
}

function calculateTrimmedMean(data, trimPercentage) {
    const sortedData = data.slice().sort((a, b) => a - b);
    const trimCount = Math.round(sortedData.length * trimPercentage);
    const trimmedData = sortedData.slice(trimCount, sortedData.length - trimCount);
    const trimmedMean = trimmedData.reduce((sum, value) => sum + value, 0) / trimmedData.length;

    return trimmedMean;
  }

function normalizeValues(data) {
    const minValue = Math.min(...data);
    const maxValue = Math.max(...data);
    const normalizedData = [];
  
    for (let i = 0; i < data.length; i++) {
      const normalizedValue = (data[i] - minValue) / (maxValue - minValue);
      normalizedData.push(normalizedValue);
    }
  
    return normalizedData;
  }

function calculateGeometricMean(data) {
    const n = data.length;
    let product = 1;
  
    for (let i = 0; i < n; i++) {
      product *= data[i];
    }
  
    const geometricMean = Math.pow(product, 1 / n);
    return geometricMean;
  }

function prioritizeTopFourBystoreName(data){
  let sortedList = {};

  // Iterate through each item in the JSON list
  data.forEach((item) => {
    const shopName = item.Shop; // Get the store name of the current item

    // If the store name does not exist in the sorted list, initialize it as an empty array
    if (!sortedList[shopName]) {
      sortedList[shopName] = [];
    }

    // Push the current item to the corresponding store's array in the sorted list
    sortedList[shopName].push(item);
  });

  for (const shop in sortedList) {
    sortedList[shop] = sortedList[shop].slice(0, 4); // Take the first four items
  }

  // Flatten the sorted list into a single array
  const flattenedList = Object.values(sortedList).flat();
  flattenedList.sort(() => Math.random() - 0.5);
  
  for (const shop in sortedList) {
    sortedList[shop] = sortedList[shop].slice(0, 5); // Take the first four items
  }
  const remainingItems = data.filter((item) => !flattenedList.includes(item));
  remainingItems.sort(() => Math.random() - 0.5);
  // Add the remaining items to the sorted list in no particular order
  const finalList = flattenedList.concat(remainingItems);

  return finalList;
}

function algorithmSort(jsonresult){

    const jsonSortedResult = prioritizeTopFourBystoreName(jsonresult)
    //console.log(jsonresult);
    return jsonSortedResult;
}

module.exports = {algorithmSort};