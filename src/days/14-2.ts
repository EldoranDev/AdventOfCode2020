import { } from '../lib/input';

const R_MEM = /mem\[([0-9]*)\] = ([0-9]*)/;

export default function (input: string[]) {
    let mask: string = "";
    let mem: Record<string, number> = {};

    for (let i = 0; i < input.length; i++) {
        if (input[i].includes('mask')) {
            mask = input[i].replace('mask = ', '');
        } else {
            let match = R_MEM.exec(input[i]);
            let bin = Number(match[1]).toString(2).padStart(mask.length, '0');
            
            let addresses = getMemoryArray(mask, bin);

            for (let add of addresses) {
                mem[add] = Number(match[2]);
            }
        }
    }

    return Object.values(mem).reduce((sum, m) => sum + m, 0);
};

function getMemoryArray(mask: string, address: string, current: string = ""): string[] {
    if (current.length === mask.length) {
        return [Number.parseInt(current, 2).toString() ];
    }

    let addresses = [];

    if (mask.charAt(current.length) === 'X') {
        addresses.push(...getMemoryArray(mask, address, current + "0"));
        addresses.push(...getMemoryArray(mask, address, current + "1"));
    } else if (mask.charAt(current.length) === '0') {
        addresses.push(...getMemoryArray(mask, address, current + address.charAt(current.length)));
    } else {
        addresses.push(...getMemoryArray(mask, address, current + "1"));
    }

    return addresses;
}