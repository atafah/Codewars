export class Kata {
  static getCount(str: string): number {
    let count: number = 0;
    for (let c of str){
      if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u')
      {
        count++;
      }
    }
    return count;
  }
}