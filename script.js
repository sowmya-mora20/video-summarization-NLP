const form = document.getElementById('summaryForm');
const output = document.getElementById('output');
const doll = document.getElementById('clapDollContainer');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  // Hide clapping doll at start
  doll.style.display = 'none';
  output.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Generating summary...`;
  const url = form.url.value.trim();
  const lang = form.lang.value.trim() || 'en';
  const length = form.length.value;
  if (!url) {
    output.innerHTML = `<span style="color: red;"><i class="fas fa-exclamation-circle"></i> Please enter a valid YouTube URL.</span>`;
    return;
  }
  try {
    const response = await fetch(
      `/summary?url=${encodeURIComponent(url)}&lang=${encodeURIComponent(lang)}&length=${encodeURIComponent(length)}`
    );
    if (!response.ok) {
      const err = await response.json();
      output.innerHTML = `<span style="color: red;"><i class="fas fa-exclamation-triangle"></i> Error: ${
        err.error || 'Unknown error'
      }</span>`;
      return;
    }
    const data = await response.json();
    output.innerHTML = `
      <i class="fas fa-check-circle" style="color: green;"></i> <strong>Summary:</strong><br/><br/>
      ${data.summary}
    `;
    // Show clapping doll for 4 seconds
    doll.style.display = 'block';
    setTimeout(() => {
      doll.style.display = 'none';
    }, 4000);
  } catch (error) {
    output.innerHTML = `<span style="color: red;"><i class="fas fa-bug"></i> Request failed: ${error.message}</span>`;
  }
});
