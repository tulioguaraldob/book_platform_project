const button = document.getElementById('submit-button');
const dataInput = document.getElementById('data');

button.addEventListener('click', async () => {
    const data = dataInput.value;

    try {
        const response = await fetch('https://8000-tulioguaral-bookplatfor-ogcyobr9sly.ws-us117.gitpod.io/contas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const responseData = await response.json();
        console.log(responseData);
        // Handle the response data here, for example, display it on the page
    } catch (error) {
        console.error('Error:', error);
        // Handle errors here, for example, display an error message to the user
    }
});