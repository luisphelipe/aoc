export const p = (...data: any) => console.log(...data);

export const pj = (data: any) => p(JSON.stringify(data, null, 4));

export const pm = (matrix: any[][], separator = ' ') =>
    matrix.forEach((line) => p(line.join(separator)));

export const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));
