document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll("form[id^='form-']");

  forms.forEach((form) => {
    const formId = form.id.split("-")[1]; 
    const taskInput = document.getElementById(`taskInput-${formId}`);
    const statusSelect = document.getElementById(`statusSelect-${formId}`);
    const submitBtn = document.getElementById(`submitBtn-${formId}`);

    const originalTask = taskInput.value;
    const originalStatus = statusSelect.value;

    const checkChanges = () => {
      const currentTask = taskInput.value;
      const currentStatus = statusSelect.value;

      if (currentTask !== originalTask || currentStatus !== originalStatus) {
        submitBtn.style.display = "inline"; 
      } else {
        submitBtn.style.display = "none"; 
      }
    };
    taskInput.addEventListener("input", checkChanges);
    statusSelect.addEventListener("change", checkChanges);
    submitBtn.style.display = "none";
  });
});
