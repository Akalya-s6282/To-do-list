document.addEventListener("DOMContentLoaded", () => {
  // Find all forms with ID starting with "form-"
  const forms = document.querySelectorAll("form[id^='form-']");

  forms.forEach((form) => {
    const formId = form.id.split("-")[1];  // Extract unique ID
    const taskInput = document.getElementById(`taskInput-${formId}`);
    const statusSelect = document.getElementById(`statusSelect-${formId}`);
    const submitBtn = document.getElementById(`submitBtn-${formId}`);

    // Store original values
    const originalTask = taskInput.value;
    const originalStatus = statusSelect.value;

    // Function to check if form has changed
    const checkChanges = () => {
      const currentTask = taskInput.value;
      const currentStatus = statusSelect.value;

      if (currentTask !== originalTask || currentStatus !== originalStatus) {
        submitBtn.style.display = "inline";  // Show button
      } else {
        submitBtn.style.display = "none";  // Hide button
      }
    };

    // Attach event listeners
    taskInput.addEventListener("input", checkChanges);
    statusSelect.addEventListener("change", checkChanges);

    // Hide the button initially if unchanged
    submitBtn.style.display = "none";
  });
});
