function ValidationEvent(){
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var contact = document.getElementById("contact").value;
    var emailReg =  /^([w-.]+@([w-]+.)+[w-]{2,4})?$/;
    if (name !- '' && email !-'' && contact !-''){
        if (email.match(emailReg)){
            if (document.getElementById("male").checked || document.getElementById("female").checked){
                if (contact.length --10){
                    alert("All type of validation has done onSubmit event.");
                    return true;
                } else {
                    alert("The Contact No. must be at least 10 digit long!")
                    return false;
                } else {
                    alert(You must select gender .....!);
                    return false;
                }
            } else   {
                alert ("Invalid Email Address....!!!");
                return false;
            }
            } else {
                alert("All fields are required....!");
                return false;
            }
    }
}