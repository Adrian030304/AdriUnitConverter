const formBody = document.querySelector('.form-body');
const toUnit = document.getElementById('to-unit');
const fromUnit = document.getElementById('from-unit');
const errorMsg = document.getElementById('error');
const inputVal = document.getElementById('val');
const resetBtn = document.getElementById('reset');

if (formBody !== null) {
    formBody.addEventListener('submit', (e) => {
        console.log(e)
        e.preventDefault();
        formBody.submit();

    })
}

if (inputVal !== null) {
    inputVal.addEventListener('input', (e) => {
        let str = e.target.value;

        const isValid = /^(\d+(\.\d*)?|\.\d+)$/.test(str);
        if (str && (!isValid)) {
            errorMsg.style.display = 'block';
        } else {
            errorMsg.style.display = 'none';
        }
    })
}