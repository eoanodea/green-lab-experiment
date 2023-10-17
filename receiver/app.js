const express = require("express");
const app = express();
const port = 3000;
const fs = require("fs");
const path = require("path");
const csv = require("csv-parser");
const moment = require("moment");

// Create a CSV-formatted string
const csvRow = `"Date","Name","Value","Host"\n`;

// Append the data to a CSV file
const csvFilePath = path.join(__dirname, "data.csv");

// Clear the file if it already exists
if (fs.existsSync(csvFilePath)) {
  fs.unlinkSync(csvFilePath);
}

// Write the headers to the file
fs.appendFileSync(csvFilePath, csvRow);

// Middleware to parse JSON requests
app.use(express.json());

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  next();
});

// Define a route to handle POST requests with JSON data
app.post("/api/data", (req, res) => {
  // Access the JSON data from the request object
  const jsonData = req.body;

  if (jsonData) {
    // const data = JSON.stringify(jsonData);
    // console.log("check me", data, jsonData);
    const dataName = jsonData.metric;
    const dataValue = jsonData.value;
    const timestamp = moment().format("YYYY-MM-DD HH:mm:ss");
    const host = jsonData.host;

    // Create a new CSV-formatted row with the data
    const dataRow = `"${timestamp}","${dataName}","${dataValue}","${host}"\n`;
    fs.appendFile(csvFilePath, dataRow, (err) => {
      if (err) {
        console.error("Error writing to CSV file: ", err);
        res.status(500).json({ error: "Error writing to CSV file" });
      } else {
        console.log(`Data saved to CSV: ${dataRow}`);
        res.json({ message: "Data saved to CSV" });
      }
    });
  } else {
    // If no data is provided, send an error response
    res.status(400).json({ error: "No JSON data provided" });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
