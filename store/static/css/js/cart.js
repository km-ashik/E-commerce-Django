// Select the elements
const checkoutBtn = document.getElementById("checkout-btn");
const successPopup = document.getElementById("success-popup");
const closePopup = document.getElementById("close-popup");

// Show popup on "Proceed to Checkout" click
checkoutBtn.addEventListener("click", (e) => {
    e.preventDefault(); // Prevent form submission or page reload
    successPopup.style.display = "flex";
});

// Close popup on "Close" button click
closePopup.addEventListener("click", () => {
    successPopup.style.display = "none";
});
