// setup input form
document.getElementById("prediction-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    // Here is the inputs
    const age = document.getElementById("age").value;
    const bmi = document.getElementById("bmi").value;
    const smoker = document.getElementById("smoker").checked ? 1 : 0;

    // URL for API
    const apiUrl = `http://localhost:5000/predict/${age}/${bmi}/${smoker}`;

    // Handling errors and fetching
    try {
      const response = await fetch(apiUrl);
      const data = await response.json();
      document.getElementById("result").textContent = `Predicted Health Insurance Cost: ${data.insurance_cost.toFixed(2)}`;
    } catch (error) {
      console.error("Error fetching data from the API:", error);
      document.getElementById("result").textContent = "Error: Unable to fetch prediction.";
    }
  });
  
