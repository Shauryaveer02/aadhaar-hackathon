export async function fetchSuggestions() {
  const response = await fetch("http://localhost:5000/api/suggest", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify([
      {
        aadhaar_number: "123456789012",
        age: 20,
        mobile_linked: false,
        address_changed: true
      }
    ])
  });

  return response.json();
}
