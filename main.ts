import fs from 'fs';
import PdfParse from 'pdf-parse';

const pdfFile = fs.readFileSync('seu_historico.pdf');


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


    
    const regex = /([A-ZÀ-Ú\s\d]+)\s+Dr(?:a)?\. .*?\(\d+h\)[\s\S]*?(\d{2}(?:APR|REP|TRANC|REPMF|REPF|REP|CANC|DIS)[A-Z]+[\d]+),0([A-Z#\-]+)/g;

    const materias: { nome: string; status: string; mencao: string }[] = [];

    let match;

    while ((match = regex.exec(text)) !== null) {
        const nome = match[1].trim().replace(/\s+/g, ' ');
        let statusRaw = match[2];

        let status;
        if (statusRaw.includes('APR')) {
        status = 'APR'; // Aprovado(a) por média
        } else if (statusRaw.includes('REP')) {
        if (statusRaw.includes('REPMF')) {
            status = 'REPMF'; // Reprovado(a) por média e falta
        } else if (statusRaw.includes('REPF')) {
            status = 'REPF'; // Reprovado(a) por falta
        } else {
            status = 'REP'; // Reprovado(a) por média
        }
        } else if (statusRaw.includes('CANC')) {
        status = 'CANC'; // Cancelado
        } else if (statusRaw.includes('DISP')) {
        status = 'DISP'; // Dispensado(a)
        } else if (statusRaw.includes('MATR')) {
        status = 'MATR'; // Matriculado(a)
        } else if (statusRaw.includes('TRANC')) {
        status = 'TRANC'; // Trancado
        } else if (statusRaw.includes('CUMP')) {
        status = 'CUMP'; // Cumpriu (ganhou o componente por aproveitamento)
        } else {
        status = 'DESCONHECIDO'; // Caso nenhuma das siglas seja encontrada
        }

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