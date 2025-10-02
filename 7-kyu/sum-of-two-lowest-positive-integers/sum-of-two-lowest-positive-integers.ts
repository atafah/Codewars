export function sumTwoSmallestNumbers(numbers:Array<number>):number {  
  const sortedAsc:Array<number> = numbers.sort((a, b) => a-b);
  return (sortedAsc[0] + sortedAsc[1]);
}