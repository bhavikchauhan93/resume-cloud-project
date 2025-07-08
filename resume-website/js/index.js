const visitsCount = document.getElementById('visitor-count');

async function counterUpdate() {
  const url = "Enter Api Gateway end point Url here";
  
  fetch(url)
  .then(response => response.json())
  .then(data => visitsCount.innerHTML = `Visits: ${data.Counter}`)
  .catch(error => console.error('Error:', error));
}
counterUpdate();