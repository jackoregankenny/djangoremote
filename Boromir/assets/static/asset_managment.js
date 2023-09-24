document.addEventListener('DOMContentLoaded', function() {
    // Get CSRF Token from form
    console.log("I'm here")
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  
    // Enable inline editing when the "Edit" button is clicked
    document.querySelectorAll('.edit-button').forEach(function(button) {
      button.addEventListener('click', function() {
        const id = this.getAttribute('data-id');
        document.querySelectorAll(`#row_${id} .editable`).forEach(function(cell) {
          const text = cell.textContent.trim();
          const field = cell.getAttribute('data-field');
          cell.innerHTML = `<input type="text" class="border p-1" name="${field}" value="${text}">`;
        });
        // Show the "Save" button and hide the "Edit" button
        document.querySelector(`#row_${id} .edit-button`).classList.add('hidden');
        document.querySelector(`#row_${id} .save-button`).classList.remove('hidden');
      });
    });
  
    // Implement saving logic when the "Save" button is clicked
    document.querySelectorAll('.save-button').forEach(function(button) {
      button.addEventListener('click', function() {
        const id = this.getAttribute('data-id');
        const formData = new FormData();
        formData.append('id', id);
  
        // Collect updated data from the input fields
        document.querySelectorAll(`#row_${id} .editable input`).forEach(function(input) {
          formData.append(input.name, input.value);
        });
  
        // Send AJAX POST request to update the asset
        fetch('/mod/update_asset/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': csrfToken,
          },
          body: formData
        })
        .then(response => response.json())
        .then(data => {
          if (data.status === 'success') {
            // Update the UI to reflect the saved changes
            document.querySelectorAll(`#row_${id} .editable input`).forEach(function(input) {
              const text = input.value;
              const field = input.name;
              input.parentElement.innerHTML = text;
            });
        
            // Switch back to the "Edit" button
            document.querySelector(`#row_${id} .save-button`).classList.add('hidden');
            document.querySelector(`#row_${id} .edit-button`).classList.remove('hidden');
         
            // Update the UI to reflect the saved changes
            // ... (This could include reverting the input fields back to plain text)
          }
        });
      });
    });
  
    // Implement deleting logic when the "Delete" button is clicked
    document.querySelectorAll('.delete-button').forEach(function(button) {
      button.addEventListener('click', function() {
        if (confirm('Are you sure you want to delete this asset?')) {
          const id = this.getAttribute('data-id');
  
          // Send AJAX DELETE request to remove the asset
          fetch(`/mod/delete_asset/?id=${id}`, {
            method: 'DELETE',
            headers: {
              'X-CSRFToken': csrfToken,
            }
          })
          .then(response => response.json())
          .then(data => {
            if (data.status === 'success') {
              // Remove the row from the table
              document.querySelector(`#row_${id}`).remove();
            }
          });
        }
      });
    });
  });