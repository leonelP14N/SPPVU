document.getElementById('carForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('make', document.getElementById('make').value);
    formData.append('model', document.getElementById('model').value);
    formData.append('year', document.getElementById('year').value);
    formData.append('mileage', document.getElementById('mileage').value);
    formData.append('color', document.getElementById('color').value);
    formData.append('image1', document.getElementById('image1').files[0]);
    formData.append('image2', document.getElementById('image2').files[0]);
    formData.append('image3', document.getElementById('image3').files[0]);
    formData.append('image4', document.getElementById('image4').files[0]);

    try {
        const response = await fetch('http://localhost:5000/evaluate', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log('Evaluation result:', result);

        // Optionally handle the PDF generation here or elsewhere in your app
        // generatePDF(result);

    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
});
