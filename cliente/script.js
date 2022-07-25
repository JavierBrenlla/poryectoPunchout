var xml = ''



let xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       console.log(xhr.responseText);
    }
};

xhr.open('POST', 'http://127.0.0.1:8000/punchout/', true)