
         function loginUser() {
            let role = document.getElementById("role").value;

            if (role === "") {
                alert("Please select a role!");
                return;
            }

            if (role === "admin") {
                window.location.href = "admin/dashboard.html";
            } 
            else if (role === "doctor") {
                window.location.href = "doctor/dashboard.html";
            } 
            else if (role === "patient") {
                window.location.href = "patient/dashboard.html";
            }
        }
    