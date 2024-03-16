const dropArea = document.getElementById('drop-area');
const videoInput = document.getElementById('video-input');

dropArea.addEventListener('click', () => videoInput.click());

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false);
  document.body.addEventListener(eventName, preventDefaults, false); // Prevent default behavior for the whole document body.
});

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false);
});

['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false);
});

function highlight() {
  dropArea.classList.add('highlight');
}

function unhighlight() {
  dropArea.classList.remove('highlight');
}

dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
  let dt = e.dataTransfer;
  let files = dt.files;
  videoInput.files = files;
  document.getElementById('file-form').submit();
}
