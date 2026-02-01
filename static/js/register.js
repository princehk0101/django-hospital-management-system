
        function registerUser() {
            let role = document.getElementById("role").value;

            if (role === "") {
                alert("Please select a role to register!");
                return;
            }

            if (role === "patient") {
                window.location.href = "patient/dashboard.html";
            }
            else if (role === "doctor") {
                window.location.href = "doctor/dashboard.html";
            }
            else {
                alert("Invalid role selected!");
            }
        }
    