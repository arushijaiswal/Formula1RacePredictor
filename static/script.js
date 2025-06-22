const form = document.getElementById('predictForm');

form.addEventListener('submit', async function (e) {
  e.preventDefault();

  const formData = new FormData(form);
  const params = new URLSearchParams(formData);

  const response = await fetch('/predict', {
    method: 'POST',
    body: params
  });

  const data = await response.json();

  const resultDiv = document.getElementById('result');
  resultDiv.classList.remove('d-none');
  resultDiv.innerText = `🏎️ Predicted Finishing Position: ${data.prediction}`;

  document.getElementById('chart').innerHTML = data.chart;
});
document.getElementById('resetButton').addEventListener('click', function () {
  document.getElementById('result').classList.add('d-none');
  document.getElementById('chart').innerHTML = '';
  form.reset();
});
document.getElementById('predictButton').addEventListener('click', function () {    
  form.dispatchEvent(new Event('submit'));
});
document.getElementById('predictButton').disabled = false;  