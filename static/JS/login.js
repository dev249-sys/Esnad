document.getElementById('blockchainForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const response = await fetch('http://localhost:5000/getData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            uname: document.querySelector('input[name="uname"]').value,
            psw: document.querySelector('input[name="psw"]').value
        })
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
});
