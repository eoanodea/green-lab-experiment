const express = require("express");
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Define a route to handle GET requests with JSON data
app.get("/api/data", (req, res) => {
  // Access the JSON data from the request object
  const jsonData = req.query.data; // Assuming the JSON data is passed as a query parameter

  if (jsonData) {
    // Respond with a JSON object
    res.json({ message: "Received JSON data", data: jsonData });
    console.log("message: " + jsonData);
  } else {
    // If no data is provided, send an error response
    res.status(400).json({ error: "No JSON data provided" });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
