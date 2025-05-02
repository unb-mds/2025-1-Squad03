import fs from 'fs';
import PdfParse from 'pdf-parse';

const pdfFile = fs.readFileSync('pdf-test.pdf');

PdfParse(pdfFile).then(function (data) {
    const text = data.text;
    const jsonData = { content: text };
    const outputFile = 'output.json';

    if (!fs.existsSync(outputFile)) {
        fs.writeFileSync(outputFile, JSON.stringify(jsonData, null, 2));
    } else {
        console.log(`${outputFile} already exists.`);
    }
}).catch(function (error) {
    console.error('Error parsing PDF:', error);
});