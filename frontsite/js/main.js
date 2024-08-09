document.addEventListener('DOMContentLoaded', function () {
    // Variáveis para manipulação do DOM
    const form = document.getElementById('car-form');
    const steps = document.querySelectorAll('.formbold-steps ul li');
    const stepContents = document.querySelectorAll('.formbold-form-step-1, .formbold-form-step-2, .formbold-form-step-3');
    const precoPrevistoElement = document.getElementById('preco-previsto');
    const submitBtn = document.getElementById('submit-btn');
    const novaAvaliacaoBtn = document.getElementById('nova-avaliacao');
    const p_preco = document.querySelector('preco-test');
    let currentStep = 0;

    // Função para avançar para o próximo passo
    function nextStep() {
        if (currentStep < steps.length - 1) {
            steps[currentStep].classList.remove('active');
            stepContents[currentStep].classList.remove('active');
            currentStep++;
            steps[currentStep].classList.add('active');
            stepContents[currentStep].classList.add('active');

            // Alterar o texto do botão na última etapa
            if (currentStep === steps.length - 1) {
                submitBtn.textContent = 'Avaliar';
            }
        }
    }

    // Função para voltar ao passo anterior
    function previousStep() {
        if (currentStep > 0) {
            steps[currentStep].classList.remove('active');
            stepContents[currentStep].classList.remove('active');
            currentStep--;
            steps[currentStep].classList.add('active');
            stepContents[currentStep].classList.add('active');

            // Alterar o texto do botão de volta ao padrão se não estiver na última etapa
            if (currentStep < steps.length - 1) {
                submitBtn.textContent = 'Próximo Passo';
            }
        }
    }

    // Manipulação dos botões "Próximo Passo" e "Voltar"
    document.querySelector('.formbold-btn').addEventListener('click', function () {
        if (currentStep === steps.length - 2) {
            // Se estiver na penúltima etapa, muda o texto do botão para 'Avaliar'
            submitBtn.textContent = 'Avaliar';
        }
        nextStep();
    });

    document.querySelector('.formbold-back-btn').addEventListener('click', previousStep);

    // Envio do formulário para a API somente na última etapa
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Evita o envio padrão do formulário

        if (currentStep === steps.length - 1) {
            // Captura os dados necessários do formulário
            const data = {
                marca: form.elements['marca'].value,
                modelo: form.elements['modelo'].value,
                transmissao: form.elements['transmissao'].value,
                combustivel: form.elements['combustivel'].value,
                ano: parseInt(form.elements['ano'].value, 10),
                quilometragem: parseInt(form.elements['quilometragem'].value, 10),
                moto_size: parseFloat(form.elements['moto_size'].value)
            };
            // Função para formatar o preço com separadores de milhar e vírgula para centavos
            function formatCurrency(amount) {
                // Adiciona separadores de milhar e formata o número com vírgula como separador decimal
                return amount.toLocaleString('pt-PT', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
            }
            // Envio dos dados para a API
            fetch('http://localhost:5000/prever_preco', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => response.json())
                .then(data => {
                    // Verificar o conteúdo da resposta
                    console.log('Resposta da API:', data);

                    var preco = data.preco_previsto;
                    preco = formatCurrency(preco);

                    // Atualiza o valor previsto no DOM
                    precoPrevistoElement.innerHTML = `De acordo com as características do seu veículo, o preço previsto é de <span class="preco">${preco} KZ</span>.`;

                    // Altera o texto do botão "Avaliar" para "Nova Avaliação"
                    submitBtn.textContent = 'Nova Avaliação';

                    // Avança para a última etapa automaticamente
                    while (currentStep < 2) {
                        nextStep();
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                });
        }
    });

    // Manipulação do botão "Nova Avaliação"
    novaAvaliacaoBtn.addEventListener('click', function () {
        form.reset();
        currentStep = 0; // Voltar para o passo inicial
        steps.forEach(step => step.classList.remove('active'));
        stepContents.forEach(content => content.classList.remove('active'));
        steps[0].classList.add('active');
        stepContents[0].classList.add('active');
        submitBtn.textContent = 'Próximo Passo';
    });
});