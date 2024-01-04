console.log('Script started.');

function validate_form(){
    var messageElements = document.querySelectorAll('.message-part span');
    messageElements.forEach(function (messageElement) {
        console.log(messageElement.innerHTML);
    });
    console.log(messages);

}