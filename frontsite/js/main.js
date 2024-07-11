document.getElementById('carForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const formData = {
        make: document.getElementById('make').value,
        model: document.getElementById('model').value,
        year: document.getElementById('year').value,
        mileage: document.getElementById('mileage').value,
        color: document.getElementById('color').value
    };
    
    try {
        const response = await fetch('https://api.example.com/evaluate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();

        generatePDF(result);

    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
});

function generatePDF(data) {
    const doc = new jsPDF();
    doc.text(`Car Evaluation`, 10, 10);
    doc.text(`Make: ${data.make}`, 10, 20);
    doc.text(`Model: ${data.model}`, 10, 30);
    doc.text(`Year: ${data.year}`, 10, 40);
    doc.text(`Mileage: ${data.mileage}`, 10, 50);
    doc.text(`Color: ${data.color}`, 10, 60);
    doc.text(`Evaluation: ${data.evaluation}`, 10, 70);

    doc.save('car_evaluation.pdf');
}
