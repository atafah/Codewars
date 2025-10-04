export class Challenge {
  static solution(n: number): number {
    if (n < 0) return 0;
    
    let i: number = 3;
    let sum: number = 0;
    while (i < n){
      if (i % 3 === 0 || i % 5 === 0){
        sum += i
      }
      i++;
    }
    return sum;
  }
}