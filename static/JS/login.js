const storedEmail = "dev.esnad@gmail.com";
const storedPassword = "esnadgroup";

function login() {
    const email = document.getElementById("uname").value;
    const password = document.getElementById("psw").value;
    const resultDiv = document.getElementById("result");

    if (email === storedEmail && password === storedPassword) {
        resultDiv.innerHTML = "<p>تم تسجيل الدخول بنجاح!</p>";
        window.location.href = "/log";
    } else {
        resultDiv.innerHTML = "<p>فشل في تسجيل الدخول. تأكد من البريد الإلكتروني وكلمة المرور.</p>";
    }

    // Return false to prevent form submission
    return false;
}
