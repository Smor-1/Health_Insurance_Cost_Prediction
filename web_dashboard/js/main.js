// setup input form
document.getElementById("prediction-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  // Here are the inputs
  const age = document.getElementById("age").value;
  const bmi = document.getElementById("bmi").value;
  const smoker = document.getElementById("smoker").checked ? 1 : 0;

  // URL for API
  const apiUrl = `http://localhost:5500/predict`;

  // Data to send
  const data = {
      age: age,
      bmi: bmi,
      smoker: smoker
  };

  // Options for fetch
  const options = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
  };

  // Handling errors and fetching
  try {
    const response = await fetch(apiUrl, options);
    const prediction = await response.json();
    document.getElementById("result").textContent = `Predicted Health Insurance Cost: ${prediction.insurance_cost.toFixed(2)}`;
  } catch (error) {
    console.error("Error fetching data from the API:", error);
    document.getElementById("result").textContent = "Error: Unable to fetch prediction.";
  }
});
