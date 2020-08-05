function sendMail(contactForm) {
    emailjs.send("gmail-ms4", "ms4_contact", {
        "from_name": contactForm.username.value,
        "from_email": contactForm.email.value,
        "contact_request": contactForm.message.value
        })
        .then(function(response) {
            console.log("SUCCESS", response.status, response.text);
            window.location.href = "/pages/success/"; //Redirect to success message
        },function(error) {
            console.log("FAILED", error);
            window.location.href = "/pages/error/"; //Redirect to error message
        }
    );
    return false; // To block from loading a new page
}