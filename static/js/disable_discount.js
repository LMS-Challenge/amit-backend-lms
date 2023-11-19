document.addEventListener('DOMContentLoaded', function() {
    // Function to toggle the disabled state of the discount field
    function toggleDiscount(disabled) {
      const discountField = document.querySelector('discount');
      if (discountField) {
        discountField.disabled = disabled;
      }
    }

    // Get the checkbox input and attach an event listener
    const newPriceCheckbox = document.querySelector('new_price');
    if (newPriceCheckbox) {
      newPriceCheckbox.addEventListener('change', function() {
        // When the state changes, toggle the discount field
        toggleDiscount(!newPriceCheckbox.checked);
      });

      // Initial state check on page load
      toggleDiscount(!newPriceCheckbox.checked);
    }
  });
