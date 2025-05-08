import fs from 'fs';
import PdfParse from 'pdf-parse';

const pdfFile = fs.readFileSync('seu_historico_aqui');


PdfParse(pdfFile).then(function (data) {

    const text = data.text;
    //console.log(text);
    const inicioChaveCurso = "Dados do Vínculo do(a) Discente";
    const inicioCurso = text.indexOf("Dados do Vínculo do(a) Discente");
    const fimCurso = text.indexOf("2028.1 / 2031.1");

    if (inicioCurso !== -1 && fimCurso !== -1) {
        const cursoExtraido = text.substring(inicioCurso + inicioChaveCurso.length, fimCurso);
        console.log("Trecho extraído:", cursoExtraido);
    }
    
    const inicioChaveCurriculoCurso = "Ano/Período de Integralização:";
    const inicioCurriculo = text.indexOf("Ano/Período de Integralização:");
    const fimCurriculo = text.indexOf("Reconhecimento do Curso");
    
    if (inicioCurriculo !== -1 && fimCurriculo !== -1) {
        const cursoExtraido = text.substring(inicioCurriculo + inicioChaveCurriculoCurso.length, fimCurriculo);
        console.log("Trecho extraído:", cursoExtraido);
    }


    
    const regex = /([A-ZÀ-Ú\s\d]+)\s+Dr(?:a)?\. .*?\(\d+h\)[\s\S]*?(\d{2}(?:APR|REP)[A-Z]+[\d]+),0([A-Z#\-]+)/g;

    const materias: { nome: string; status: string; mencao: string }[] = [];

    let match;

    while ((match = regex.exec(text)) !== null) {
        const nome = match[1].trim().replace(/\s+/g, ' ');
        const status = match[2].includes('APR') ? 'APR' : 'REP';
        const mencao = match[3].replace(/[^A-Z]/g, '');



        const materia = { nome, status, mencao };

        materias.push(materia);

        console.log(`Matéria: ${nome}`);
        console.log(`Status: ${status}`);
        console.log(`Menção: ${mencao}`);
        console.log('-------------------------');


    }

    
    fs.writeFileSync('materias.json', JSON.stringify(materias, null, 2));
    console.log('Dados extraídos com sucesso!');
}).catch((err) => {
    console.error('Erro ao processar o PDF:', err);
}); 





//const pdfFile = fs.readFileSync('testepdf2.pdf');

/*
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
}); */